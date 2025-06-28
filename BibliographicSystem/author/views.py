from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from BibliographicSystem.author.models import Author


class AuthorHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'author_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user
        context['author_degree_choices'] = Author.degree
        return context