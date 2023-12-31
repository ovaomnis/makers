# Generated by Django 4.2.5 on 2023-09-14 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('video', models.FileField(upload_to='videos')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='films', to='film.category')),
            ],
        ),
    ]
