"""
URL configuration for BibliographicSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from BibliographicSystem import views
from BibliographicSystem.author.views import AuthorHomeView
from BibliographicSystem.views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', views.index, name='index'),

    path('author/', AuthorHomeView.as_view(), name='author_home'),
    path('admin/', admin.site.urls),
]
