from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=123)
    addr=models.CharField(max_length=123)
    phone=models.IntegerField()


class Language(models.Model):
    name=models.CharField(max_length=123)
    version=models.CharField(max_length=123)