from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()


    def __str__(self):
        return self.first_name


class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    titles = models.CharField(max_length=200)
    date_released = models.DateField()
    likes = models.PositiveIntegerField()
    artiste_id = models.PositiveIntegerField()


    def __str__(self):
        return self.titles

class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete = models.CASCADE)
    content = models.TextField()
    song_id = models.PositiveIntegerField()


    def __str__(self):
        return self.content


