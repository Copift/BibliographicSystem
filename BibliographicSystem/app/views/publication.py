# author.py
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, ListView

import requests
from django.http import JsonResponse
from BibliographicSystem.app.models.conference import Conference
from BibliographicSystem.app.models.journal import Journal
from BibliographicSystem.app.models.publication import Publication



class PublicationListView(ListView):
    model = Publication
    template_name = 'publication/publication_list.html'
    context_object_name = 'publications'
    paginate_by = 10
    ordering = ['-year', '-added_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(abstract__icontains=search_query) | Q(
                doi__icontains=search_query) | Q(authors__last_name__icontains=search_query) | Q(
                authors__first_name__icontains=search_query)).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication/publiation_detail.html'
    context_object_name = 'publication'



@require_http_methods(["GET", "POST"])
def add_publication(request):
    if request.method == "GET":
        return render(request, "publication/add_publication.html")

    if request.method == "POST":
        try:
            # Извлекаем данные из формы
            publication_type = request.POST.get("publication_type")
            title = request.POST.get("title")  # единое поле title
            abstract = request.POST.get("abstract")
            year = int(request.POST.get("year"))
            doi = request.POST.get("doi")
            url = request.POST.get("url")

            # Валидация обязательных полей
            if not publication_type or not title or not year:
                raise ValueError("Заполните все обязательные поля")

            # Создаем публикацию
            publication = Publication.objects.create(publication_type=publication_type, title=title,
                # используем единое поле
                abstract=abstract, year=year, doi=doi, url=url, # Временное значение, будет обновлено ниже
                journal_or_conference="Temp")

            # Обработка журнала
            if publication_type == "journal":
                journal_option = request.POST.get("journal_option")

                if journal_option == "existing":
                    journal_id = request.POST.get("existing_journal")
                    journal = Journal.objects.get(id=journal_id)
                else:
                    # Создаем новый журнал
                    journal = Journal.objects.create(title=request.POST.get("journal_title"),  # единое поле
                        quartile=request.POST.get("quartile", "N/A"),
                        whitelist_level=request.POST.get("whitelist_level", "none"),
                        website=request.POST.get("journal_website"))

                # Обновляем публикацию
                publication.journal_or_conference = journal.title
                publication.save()
                publication.journals.add(journal)

            # Обработка конференции
            elif publication_type in ["conference", "proceedings"]:
                conference_option = request.POST.get("conference_option")

                if conference_option == "existing":
                    conference_id = request.POST.get("existing_conference")
                    conference = Conference.objects.get(id=conference_id)
                else:
                    # Создаем новую конференцию
                    conference = Conference.objects.create(title=request.POST.get("conference_title"),
                        location=request.POST.get("location"), start_date=request.POST.get("start_date"),
                        end_date=request.POST.get("end_date"), status=request.POST.get("status", "international"))

                # Обновляем публикацию
                publication.journal_or_conference = conference.title
                publication.save()
                publication.conferences.add(conference)

            messages.success(request, "Публикация успешно добавлена!")
            return redirect("author_home")

        except Exception as e:
            messages.error(request, f"Ошибка при добавлении публикации: {str(e)}")
            # Возвращаем пользователя на форму с сохранением введенных данных
            context = {"form_data": request.POST, "error": str(e)}
            return render(request, "publication/add_publication.html", context)
    return None







def fetch_doi_data(request):
    doi = request.GET.get("doi")
    if not doi:
        return JsonResponse({"error": "DOI не указан"}, status=400)

    try:
        # Используем API CrossRef
        response = requests.get(f"https://api.crossref.org/works/{doi}")
        response.raise_for_status()
        data = response.json()["message"]

        # Парсим нужные данные
        result = {"title": data.get("title", [""])[0],
            "year": data.get("published-print", {}).get("date-parts", [[None]])[0][0],
            "abstract": data.get("abstract", ""), "doi": doi, "url": data.get("URL", ""), "authors": []}

        # Обработка авторов
        for author in data.get("author", []):
            given = author.get("given", "")
            family = author.get("family", "")
            if given or family:
                result["authors"].append(f"{family} {given}".strip())

        return JsonResponse(result)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



def journal_list_api(request):
    journals = Journal.objects.all().values("id", "title_ru", "title_en")
    # Преобразуем в список словарей
    journals_list = list(journals)
    # Добавляем отображаемое название
    for journal in journals_list:
        journal["display_name"] = journal["title_ru"] or journal["title_en"]
    return JsonResponse(journals_list, safe=False)


def conference_list_api(request):
    conferences = Conference.objects.all().values("id", "title")
    # Преобразуем в список словарей
    conferences_list = list(conferences)
    return JsonResponse(conferences_list, safe=False)