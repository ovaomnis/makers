from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(User,
                              related_name='posts',
                              verbose_name='Владелец поста',
                              on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=70)
    description = models.TextField('Описание', blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="images/")
    views = models.PositiveIntegerField("Просмотры", default=0)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Последнее обновление", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)


class Comment(models.Model):
    owner = models.ForeignKey(User, related_name='my_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} | {self.post.title}'


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    is_like = models.BooleanField(default=False)


class Rating(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='ratings')
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='ratings')
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5),
    ], blank=True, null=True)

    def __str__(self):
        return f'{self.owner} --> {self.post.title}'
