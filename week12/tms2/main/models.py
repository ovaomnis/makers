from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='my_comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
