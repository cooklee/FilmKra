from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField()
    directed_by = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

