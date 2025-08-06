from django.http import JsonResponse

from BibliographicSystem.app.models.conference import Conference


def conference_list_api(request):
    conferences = Conference.objects.all().values("id", "title")
    # Преобразуем в список словарей
    conferences_list = list(conferences)
    return JsonResponse(conferences_list, safe=False)