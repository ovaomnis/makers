from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.film.models import Film

User = get_user_model()


# Create your models here.
class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.author.get_full_name()} -> {self.film}"


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.author.get_full_name()} -> {self.film}"


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='rating')
    rate = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ], default=1)

    def __str__(self):
        return f"{self.author.get_full_name()}: {self.rate} -> {self.film}"

