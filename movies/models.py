from django.db import models
from django.contrib.auth.models import User
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=30, default=True)
    description = models.TextField()
    date_released = models.CharField(max_length=20)
    instructions = models.TextField()
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    actors = models.ForeignKey(Actor, on_delete=models.CASCADE, default=True)
    genre = models.TextField()

    def __str__(self):
        return self.title

