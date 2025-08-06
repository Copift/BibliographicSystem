from django.contrib import messages
from django.shortcuts import render, redirect

from BibliographicSystem.app.models.conference import Conference
from BibliographicSystem.app.models.journal import Journal
from BibliographicSystem.app.models.publication import Publication


def add(request):
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
                                                 abstract=abstract, year=year, doi=doi, url=url,
                                                 # Временное значение, будет обновлено ниже
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
                                                       location=request.POST.get("location"),
                                                       start_date=request.POST.get("start_date"),
                                                       end_date=request.POST.get("end_date"),
                                                       status=request.POST.get("status", "international"))

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