from email.mime import image
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


AGE_LIMIT= (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

MOVIE_CHOICES = (
    ('Drama', 'Drama'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Action', 'Action'),
    ('Animation', 'Animation'),
    ('Family', 'Family'),
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age_limit = models.CharField(choices=AGE_LIMIT, max_length=5)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null = True)
    date = models.DateField()
    uuid = models.UUIDField(default=uuid.uuid4)
    genre = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField('Video')
    image = models.ImageField(upload_to='bgcovers')
    age_limit = models.CharField(choices=AGE_LIMIT, max_length=5)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=300)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title
    