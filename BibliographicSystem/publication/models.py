from django.db import models

from BibliographicSystem.author.models import Author


class Publication(models.Model):

    title = models.CharField(
        "Название (англ)",
        max_length=500,
        blank=True
    )
    abstract = models.TextField("Аннотация", blank=True)
    year = models.PositiveIntegerField("Год публикации")
    doi = models.CharField("DOI", max_length=100, blank=True)
    added_date = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True
    )
    url = models.URLField("Ссылка на статью", blank=True)
    authors = models.ManyToManyField(
        Author,
        related_name='publications',
        verbose_name="Авторы"
    )

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ['title' ]

    def __str__(self):
        return f"{self.title} ({self.year})"