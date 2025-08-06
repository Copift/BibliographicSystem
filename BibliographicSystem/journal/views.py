from django.views.generic import DetailView

from BibliographicSystem.journal.models import Journal


class JournalDetailView(DetailView):
    model = Journal
    template_name = 'journal/journal_detail.html'
    context_object_name = 'journal'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем публикации с сортировкой по году
        context['publications'] = self.object.publications.all().order_by('-year')
        return context