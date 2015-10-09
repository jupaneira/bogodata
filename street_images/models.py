from django.db import models


class Image(models.Model):
    lat = models.CharField(max_length=200)
    lon = models.CharField(max_length=200)
    hits = models.IntegerField()

    def __str__(self):
        return "(" + self.lat + "," + self.lon + ")"
    
