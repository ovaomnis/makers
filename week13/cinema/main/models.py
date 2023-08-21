from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=24)
    age = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    release = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')