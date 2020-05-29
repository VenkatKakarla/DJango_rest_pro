from rest_framework import serializers
from request_res_app.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Snippet
        fields=['id','title','code','linenos','language','style']