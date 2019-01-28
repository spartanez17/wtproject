from django.db import models
from enum import Enum


class Weather(models.Model):
    country = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    weather_desc = models.CharField(max_length=120)
    temp = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    weather_icon = models.CharField(max_length=120)

    def __str__(self):
        return self.title


# class Units(models.Model):

#     class LocationType(Enum):
#         ROOFTOP = 1
#         RANGE_INTERPOLATED = 2
#         GEOMETRIC_CENTER = 3
#         APPROXIMATE = 4
#         UNRESOLVED = 5

#     units = EnumIntegerField(
#         enum=LocationType,
#         default=LocationType.UNRESOLVED
#     )