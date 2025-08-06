import requests
from django.http import JsonResponse


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

