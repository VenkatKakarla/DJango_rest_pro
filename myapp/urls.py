from django.urls import path,include
from rest_framework import routers

from myapp.views import PersonView, LanguageView
router=routers.DefaultRouter()
router.register('Person',PersonView)
router.register('Language',LanguageView)

urlpatterns=[
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
]