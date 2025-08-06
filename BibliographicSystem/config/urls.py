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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import index
from django.urls import path, include

from BibliographicSystem.app.api.urls import api_v1
from BibliographicSystem.app.api.v1.conference.list import conference_list_api
from BibliographicSystem.app.api.v1.journals.list import journal_list_api
from BibliographicSystem.app.api.v1.publication.fetchDoi import fetch_doi_data
from BibliographicSystem.app.views.author.HomeView import AuthorHomeView
from BibliographicSystem.app.views.author.LoginView import login_view
from BibliographicSystem.app.views.author.ProfileView import author_profile
from BibliographicSystem.app.views.author.UpdateView import update_author_profile
from BibliographicSystem.app.views.conference.DetailView import ConferenceDetailView
from BibliographicSystem.app.views.journal.DetailView import JournalDetailView
from BibliographicSystem.app.views.publication.AddView import add_publication
from BibliographicSystem.app.views.publication.DetailView import PublicationDetailView
from BibliographicSystem.app.views.publication.ListView import PublicationListView
from BibliographicSystem.config import settings


author_url=[
                    path('author/update/', update_author_profile, name='update_author_profile'),
                    path('author/<int:pk>/', author_profile, name='author_profile'),


]
index_url=[
                    path('', PublicationListView.as_view(), name='publication_list'),
                    path('login/', login_view, name='login'),
                    path('admin/', admin.site.urls),
                    path('author_home/', AuthorHomeView.as_view(), name='author_home'),
]
urlpatterns = [


                  path("/api",include(api_v1)),
                  path('',include(index_url)),
                  path('publications/<int:pk>/', PublicationDetailView.as_view(), name='publication_detail'),
                  path('conferences/<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail'),
                  path('journals/<int:pk>/', JournalDetailView.as_view(), name='journal_detail'), ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
