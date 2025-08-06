from django.db import models

from BibliographicSystem.publication.models import Publication


class Conference(models.Model):
    STATUS_CHOICES = [
        ('regional', 'Региональная'),
        ('national', 'Всероссийская'),
        ('international_part', 'С международным участием'),
        ('international', 'Международная'),
    ]

    title = models.CharField("Название", max_length=500)
    location = models.CharField("Место проведения", max_length=255)
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата завершения")
    status = models.CharField(
        "Статус",
        max_length=20,
        choices=STATUS_CHOICES
    )
    publications = models.ManyToManyField(
        Publication,
        related_name='conferences',
        blank=True,
        verbose_name="Публикации"
    )

    class Meta:
        verbose_name = "Конференция"
        verbose_name_plural = "Конференции"
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} ({self.start_date.year})"