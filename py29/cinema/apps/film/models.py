from django.db import models
from utils import generate_unique_slug

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Category(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Category, self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Film(models.Model):
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='videos')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='films')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Film, self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
