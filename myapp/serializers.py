from rest_framework import serializers
from myapp.models import Person, Language


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Person
        fields=['name','addr','phone']

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Language
        fields=['name','version']