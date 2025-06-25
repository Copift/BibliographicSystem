from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    patronymic = models.CharField(max_length=200)
    annotation=models.CharField(max_length=400,default="_")


    def __str__(self):
        return self.username