from BibliographicSystem.author.models import Author

from django.contrib import admin

from BibliographicSystem.publication.models import Publication


@admin.register(Author)
class PublicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass