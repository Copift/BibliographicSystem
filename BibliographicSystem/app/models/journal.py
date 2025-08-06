from django.db import models

from BibliographicSystem.app.models.publication import Publication


class Journal(models.Model):
    QUARTILE_CHOICES = [
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),
        ('N/A', 'Не определен'),
    ]

    WHITELIST_LEVELS = [
        ('1', 'Уровень 1'),
        ('2', 'Уровень 2'),
        ('3', 'Уровень 3'),
        ('4', 'Уровень 4'),
        ('none', 'Не в списке'),
    ]

    #title = models.CharField("Название (рус)", max_length=255,blank=True,null=True)
    title = models.CharField(
        "Название (англ)",
        max_length=255,
        blank=True
    )
    quartile = models.CharField(
        "Квартиль",
        max_length=3,
        choices=QUARTILE_CHOICES,
        default='N/A'
    )
    whitelist_level = models.CharField(
        "Уровень белого списка",
        max_length=10,
        choices=WHITELIST_LEVELS,
        default='none'
    )
    website = models.URLField("Сайт журнала", blank=True)
    publications = models.ManyToManyField(
        Publication,
        related_name='journals',
        blank=True,
        verbose_name="Публикации"
    )

    class Meta:
        verbose_name = "Журнал"
        verbose_name_plural = "Журналы"
        ordering = ['title']

    def __str__(self):
        return self.title