from django.http import JsonResponse

from BibliographicSystem.app.models.journal import Journal


def journal_list_api(request):
    journals = Journal.objects.all().values("id", "title_ru", "title_en")
    # Преобразуем в список словарей
    journals_list = list(journals)
    # Добавляем отображаемое название
    for journal in journals_list:
        journal["display_name"] = journal["title_ru"] or journal["title_en"]
    return JsonResponse(journals_list, safe=False)

