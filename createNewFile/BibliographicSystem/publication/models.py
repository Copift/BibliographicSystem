from django.db import models

from BibliographicSystem.author.models import Author
from BibliographicSystem.journal.models import Journal
from BibliographicSystem.conference.models import Conference


class Publication(models.Model):
    title_ru = models.CharField("Название (рус)", max_length=500)
    title_en = models.CharField(
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
    journal = models.ForeignKey(
        Journal,
        on_delete=models.CASCADE,
        related_name='publications',
        null=True,
        blank=True,
        verbose_name="Журнал"
    )
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name='publications',
        null=True,
        blank=True,
        verbose_name="Конференция"
    )

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ['-year', 'title_ru']

    def __str__(self):
        return f"{self.title_ru} ({self.year})"
