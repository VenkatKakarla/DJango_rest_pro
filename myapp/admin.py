from django.contrib import admin

# Register your models here.
from myapp.models import Person, Language

admin.site.register(Person)
admin.site.register(Language)