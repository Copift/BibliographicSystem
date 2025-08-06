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
from django.urls import path

from BibliographicSystem import settings
from BibliographicSystem.author.views import AuthorHomeView, update_author_profile, author_profile, login_view
from BibliographicSystem.conference.views import ConferenceDetailView
from BibliographicSystem.journal.views import JournalDetailView
from BibliographicSystem.publication.views import fetch_doi_data, journal_list_api, conference_list_api, \
    add_publication, PublicationListView, PublicationDetailView



urlpatterns = [path('author/update/', update_author_profile, name='update_author_profile'),
                  path('author_home/', AuthorHomeView.as_view(), name='author_home'),
                  path('author/<int:pk>/', author_profile, name='author_profile'),

                  path('login/', login_view, name='login'), path('admin/', admin.site.urls),

                  path("api/journals/", journal_list_api, name="fetch_jourlanl_data"),
                  path("api/conferences/", conference_list_api, name="fetch_conference_data"),
                  path("fetch_doi_data/", fetch_doi_data, name="fetch_doi_data"),

                  path('add_publication', add_publication, name='add_publication'),
                  path('', PublicationListView.as_view(), name='publication_list'),
                  path('publications/<int:pk>/', PublicationDetailView.as_view(), name='publication_detail'),

                  path('conferences/<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail'),

                  path('journals/<int:pk>/', JournalDetailView.as_view(), name='journal_detail'), ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
