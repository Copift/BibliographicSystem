from django.views.generic import DetailView

from BibliographicSystem.app.models.publication import Publication


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication/publiation_detail.html'
    context_object_name = 'publication'
