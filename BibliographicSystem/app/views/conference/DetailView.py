from django.views.generic import DetailView

from BibliographicSystem.app.models.conference import Conference


class ConferenceDetailView(DetailView):
    model = Conference
    template_name = 'conference/conference_detail.html'
    context_object_name = 'conference'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем публикации с сортировкой по году
        context['publications'] = self.object.publications.all().order_by('-year')
        return context
