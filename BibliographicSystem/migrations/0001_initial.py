# Generated by Django 5.2.3 on 2025-06-28 08:49

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('patronymic', models.CharField(max_length=200)),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('stake', models.FloatField(blank=True, null=True, verbose_name='Доля ставки')),
                ('degree', models.CharField(default='none', max_length=200, verbose_name='Учёная степень')),
                ('degree_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Год присуждения степени')),
                ('contract_start', models.DateField(blank=True, null=True, verbose_name='Дата начала договора')),
                ('contract_end', models.DateField(blank=True, null=True, verbose_name='Дата окончания договора')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='employees/', verbose_name='Фото')),
                ('annotation', models.TextField(blank=True, verbose_name='Аннотация')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('scopus_url', models.URLField(blank=True, verbose_name='Scopus')),
                ('wos_url', models.URLField(blank=True, verbose_name='Web of Science')),
                ('rinz_url', models.URLField(blank=True, verbose_name='РИНЦ')),
                ('scholar_url', models.URLField(blank=True, verbose_name='Google Scholar')),
                ('orcid_url', models.URLField(blank=True, verbose_name='ORCID')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_type', models.CharField(choices=[('journal', 'Статья в журнале'), ('conference', 'Тезисы конференции'), ('proceedings', 'Материалы конференции')], max_length=20, verbose_name='Тип публикации')),
                ('journal_or_conference', models.CharField(max_length=255, verbose_name='Журнал/Конференция')),
                ('title_ru', models.CharField(max_length=500, verbose_name='Название (рус)')),
                ('title_en', models.CharField(blank=True, max_length=500, verbose_name='Название (англ)')),
                ('abstract', models.TextField(blank=True, verbose_name='Аннотация')),
                ('year', models.PositiveIntegerField(verbose_name='Год публикации')),
                ('doi', models.CharField(blank=True, max_length=100, verbose_name='DOI')),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('article_url', models.URLField(blank=True, verbose_name='Ссылка на статью')),
                ('authors', models.ManyToManyField(related_name='publications', to=settings.AUTH_USER_MODEL, verbose_name='Авторы')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['-year', 'title_ru'],
            },
        ),
    ]
