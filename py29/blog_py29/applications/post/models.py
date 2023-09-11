from django.db import models
from django.contrib.auth import get_user_model

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
