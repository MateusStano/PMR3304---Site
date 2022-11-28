from django.db import models
from django.conf import settings


class Album(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    poster_url = models.URLField(max_length=200, null=True)
    post_date = models.DateTimeField(auto_now=True)
    info = models.CharField(max_length=255000)

    def __str__(self):
        return f'{self.name} ({self.release_year})'


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    post_date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'


class List(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    albuns = models.ManyToManyField(Album)

    def __str__(self):
        return f'{self.name}'
