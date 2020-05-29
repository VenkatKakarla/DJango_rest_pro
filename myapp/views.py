from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from myapp.models import Person, Language
from myapp.serializers import PersonSerializer, LanguageSerializer


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly,

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = permissions.IsAuthenticated,