from django.shortcuts import render


def add_publication(request):
        return render(request, "publication/add_publication.html")