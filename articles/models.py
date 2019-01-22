from django.db import models

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
