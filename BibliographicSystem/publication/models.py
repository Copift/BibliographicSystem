from django.db import models

from BibliographicSystem.author.models import Author


class Publication(models.Model):
    PUBLICATION_TYPES = [
        ('journal', 'Статья в журнале'),
        ('conference', 'Тезисы конференции'),
        ('proceedings', 'Материалы конференции'),
    ]

    publication_type = models.CharField(
        "Тип публикации",
        max_length=20,
        choices=PUBLICATION_TYPES
    )
    journal_or_conference = models.CharField(
        "Журнал/Конференция",
        max_length=255
    )
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
    article_url = models.URLField("Ссылка на статью", blank=True)
    authors = models.ManyToManyField(
        Author,
        related_name='publications',
        verbose_name="Авторы"
    )

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ['-year', 'title_ru']

    def __str__(self):
        return f"{self.title_ru} ({self.year})"