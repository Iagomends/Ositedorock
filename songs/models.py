from django.db import models
from django.conf import settings
from datetime import datetime
from django.urls import reverse

class Song(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} ({self.release_year})'




class Post(models.Model):
    name = models.CharField(max_length=255)
    lyrics = models.CharField(max_length=2550)
    band = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.name} ({self.band})'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2550)
    posts = models.ManyToManyField(Post, blank = True)

    def __str__(self):
        return f'{self.name}'