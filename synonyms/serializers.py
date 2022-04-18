from rest_framework import serializers


class SynonymSerializer(serializers.Serializer):
    meaning = serializers.CharField(allow_null=True)
    synonyms = serializers.ListField()

    class Meta:
        fields = ('meaning', 'synonyms')


class ResponseSerializer(serializers.Serializer):
    query = serializers.CharField()
    results = SynonymSerializer()

    class Meta:
        fields = ('query', 'results')
