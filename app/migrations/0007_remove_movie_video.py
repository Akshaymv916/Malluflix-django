# Generated by Django 5.0.6 on 2024-06-20 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_movie_youtube_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='video',
        ),
    ]
