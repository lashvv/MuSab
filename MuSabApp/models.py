from django.db import models

# Create your models here.
class Album(models.Model):
    year = models.IntegerField()
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.artist} - {self.album}"