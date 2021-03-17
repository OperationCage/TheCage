import datetime
from django.db import models
from django.utils import timezone

class Name(models.Model):
    name_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name_text

class Location(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    location_text = models.CharField(max_length=200)

    def __str__(self):
        return self.location_text

class Description(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    description_text = models.CharField(max_length=400)

    def __str__(self):
        return self.description_text

class DiscoveryDate(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    discoveryDate_text = models.DateTimeField("date discovered")

    def __str__(self):
        return self.discoveryDate_text