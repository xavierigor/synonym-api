from django.urls import path

from synonyms.views import SynonymList


urlpatterns = [
    path('synonyms', SynonymList.as_view())
]
