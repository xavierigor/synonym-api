from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import SYNONYM_API_BASE_URL
from synonyms.constants import PARAM_NOT_SPECIFIED_ERROR


class SynonymList(APIView):

    def _fetch_synonyms(self, term):
        import requests
        from bs4 import BeautifulSoup

        url = SYNONYM_API_BASE_URL + term
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        synonym_sets = soup.select('#page #content div .s-wrapper')

        formatted_dict = dict(term=term, results=[])
        for synonym_set in synonym_sets:
            meaning = synonym_set.select_one('.sentido')
            if meaning is not None and meaning.text[-1] == ':':
                # If meaning exists and last character is a colon,
                # remove colon
                meaning = meaning.text[:len(meaning.text)-1]

            synonyms = [synonym.text for synonym in synonym_set.select('.sinonimos .sinonimo')]
            formatted_dict['results'].append({
                'meaning': meaning,
                'synonyms': synonyms
            })

        return formatted_dict

    def get(self, request, format=None):
        term = request.query_params.get('term', None)
        if term is None:
            return Response({"message": PARAM_NOT_SPECIFIED_ERROR}, status=status.HTTP_400_BAD_REQUEST)

        synonyms = self._fetch_synonyms(term=term)
        return Response(synonyms)
