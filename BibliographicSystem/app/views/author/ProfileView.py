from django.shortcuts import get_object_or_404, render

from BibliographicSystem.app.models.author import Author


def author_profile(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author/public_author.html', {'author': author})
