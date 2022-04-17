import requests
from bs4 import BeautifulSoup
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import SYNONYM_API_BASE_URL


class SynonymList(APIView):

    def _fetch_synonyms(self, query):
        url = SYNONYM_API_BASE_URL + slugify(query)
        webpage = requests.get(url)

        soup = BeautifulSoup(webpage.text, 'html.parser')
        synonym_sets = soup.select('#page #content div .s-wrapper')

        result = dict(query=query, results=[])
        for synonym_set in synonym_sets:
            meaning = synonym_set.select_one('.sentido')
            if meaning is not None and meaning.text[-1] == ':':
                # If meaning exists and last character is a colon,
                # remove colon
                meaning = meaning.text[:len(meaning.text)-1]

            synonyms = [synonym.text for synonym in
                        synonym_set.select('.sinonimos .sinonimo')]
            result['results'].append({
                'meaning': meaning,
                'synonyms': synonyms
            })

        return result

    def get(self, request):
        query = request.query_params.get('query', None)
        if not query:
            raise ValidationError('"query" query parameter is required')

        synonyms = self._fetch_synonyms(query=query)
        return Response(synonyms)
