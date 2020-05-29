from django.urls import path
from Serializer_app import views

urlpatterns=[
    path('snippets/',views.snippet_list),
    path('snippets/<int:pk>/',views.snippet_detail),
]