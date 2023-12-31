# Generated by Django 4.2.4 on 2023-08-10 13:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('a4d5bb4e-4799-4c34-ad4e-118abfece0cf'), editable=False, primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('done', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
