# Generated by Django 4.2.5 on 2023-09-12 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_like_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
