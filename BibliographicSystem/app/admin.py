from BibliographicSystem.app.models.author import Author

from django.contrib import admin

from BibliographicSystem.app.models.publication import Publication


@admin.register(Author)
class PublicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass