from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Movie(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField()
    directed_by = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} {self.year}"

