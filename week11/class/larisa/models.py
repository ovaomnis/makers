from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class TestModel(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    integer = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.pk)



