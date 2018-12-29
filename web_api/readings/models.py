from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model


class Station(models.Model):
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='station')

    def __str__(self):
        return f'{self.id}: {self.name} ({self.lat}, {self.lon})'


class Reading(models.Model):
    added = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)
    temperature = models.FloatField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='readings')

    def __str__(self):
        return f'{self.id} | {self.modified} {self.station}: {self.temperature}ºC'
