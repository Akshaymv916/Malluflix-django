# Generated by Django 5.0.6 on 2024-06-20 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_movie_list_m_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='youtube_link',
            field=models.TextField(default='null'),
        ),
    ]
