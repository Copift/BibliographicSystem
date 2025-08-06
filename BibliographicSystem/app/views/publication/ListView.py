from django.db.models import Q
from django.views.generic import ListView

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