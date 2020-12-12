from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    #movie_set = relacja_zwrotna // directed
    #movie_set

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return f"/person/{self.id}"

class Movie(models.Model):
    title = models.CharField(max_length=20)
    year = models.IntegerField()
    directed_by = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='directed')
    actors = models.ManyToManyField(Person, related_name='played_in')

    def __str__(self):
        return f"{self.title} {self.year}"

    def get_detail_url(self):
        return f"/movie/{self.id}"

