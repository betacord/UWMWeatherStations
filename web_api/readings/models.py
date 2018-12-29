from datetime import datetime
from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.lat}, {self.lon})'


class Reading(models.Model):
    added = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)
    station = models.OneToOneField(Station, on_delete=models.CASCADE, null=True, blank=True)
    temperature = models.FloatField()

    def __str__(self):
        return f'{self.modified} {self.station}: {self.temperature}ºC'
