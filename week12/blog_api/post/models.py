import uuid

from slugify import slugify
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            if Category.objects.filter(slug=slug).exists():
                slug += '-' + uuid.uuid4().hex[:6]
            self.slug = slug
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            if Tag.objects.filter(slug=slug).exists():
                slug += '-' + uuid.uuid4().hex[:6]
            self.slug = slug
        super().save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag, related_name='tags', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            if Post.objects.filter(slug=slug).exists():
                slug += '-' + uuid.uuid4().hex[:6]
            self.slug = slug
        super().save(*args, **kwargs)
