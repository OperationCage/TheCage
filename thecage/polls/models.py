import datetime
from django.db import models
from django.utils import timezone



class Cryptid(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    discovered_date = models.DateTimeField("date discovered")
    photo = models.ImageField(upload_to="upload/", default="None")

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    cryptids = models.ManyToManyField(Cryptid, related_name="locations")

    def __str__(self):
        return self.name
