from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    patronymic = models.CharField(max_length=200)
    position = models.CharField("Должность", max_length=255,null=True,blank=True)
    stake = models.FloatField(
        "Доля ставки",
        null=True, blank=True

    )
    degree = models.CharField(
        "Учёная степень",
        max_length=200,
        default='none'
    )
    degree_year = models.PositiveIntegerField(
        "Год присуждения степени",
        null=True,
        blank=True
    )
    contract_start = models.DateField("Дата начала договора",null=True,blank=True)
    contract_end = models.DateField("Дата окончания договора",null=True,blank=True)
    photo = models.ImageField(
        "Фото",
        upload_to='avatars/',
        null=True,
        blank=True
    )
    annotation = models.TextField("Аннотация", blank=True)
    email = models.EmailField("Электронная почта")

    # Ссылки на профили
    scopus_url = models.URLField("Scopus", blank=True)
    wos_url = models.URLField("Web of Science", blank=True)
    rinz_url = models.URLField("РИНЦ", blank=True)
    scholar_url = models.URLField("Google Scholar", blank=True)
    orcid_url = models.URLField("ORCID", blank=True)

    def __str__(self):
        return self.username