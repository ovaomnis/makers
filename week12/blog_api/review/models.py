from django.db import models
from django.contrib.auth import get_user_model

from post.models import Post

User = get_user_model()


# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.first_name} -> {self.post.title}'


class Like(models.Model):
    author = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.first_name} liked post: {self.post.title}'


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()
    author = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='ratings', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.first_name} rated as {self.rating} for post {self.post.title}'

