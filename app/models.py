from django.conf import settings
from django.db import models
import uuid

# Create your models here.

class Movie(models.Model):
    GENERE=[
        ('action','Action'),
        ('comedy','Comedy'),
        ('thriller','Thriller'),
        ('romance','Romance'),
        ('horror','Horror'),
        ('drama','Drama')
    ]

    u_id=models.UUIDField(default=uuid.uuid4)
    title=models.CharField(max_length=200)
    description=models.TextField()
    tags=models.TextField(default='null')
    youtube_link=models.TextField(default='null')
    releasedate=models.DateField()
    genre=models.CharField(max_length=100,choices=GENERE)
    length=models.FloatField(default=0)
    coming_soon=models.TextField(default=1)
    image_banner=models.ImageField(upload_to='movi_images/')
    image_cover=models.ImageField(upload_to='movi_images/')
    views=models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

class Movie_list(models.Model):
    owner_user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    m_id=models.TextField(default=0)


    def __str__(self):
        return self.movie.title