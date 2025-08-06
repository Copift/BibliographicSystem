from django.urls import path, include

from BibliographicSystem.app.api.v1.conference.list import conference_list_api
from BibliographicSystem.app.api.v1.journals.list import journal_list_api
from BibliographicSystem.app.api.v1.publication.add import add
from BibliographicSystem.app.api.v1.publication.fetchDoi import fetch_doi_data

api_patterns = [

    path("/journals/", journal_list_api, name="fetch_jourlanl_data"),
    path("/conferences/", conference_list_api, name="fetch_conference_data"),
    path("/fetch_doi_data/", fetch_doi_data, name="fetch_doi_data"),
    path('/add_publication', add, name='add_publication_api'),
]
api_v1=[
    path("/v1",include(api_patterns)),
]
