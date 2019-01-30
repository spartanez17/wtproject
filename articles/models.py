from django.db import models
from django.utils.timezone import now


class Weather(models.Model):
    KELVIN = 'kelvin'
    CELSIUS = 'celsius'
    FAHRENHEIT = 'fahrenheit'
    UNITS = (
        (KELVIN, 'kelvin'),
        (CELSIUS, 'celsius'),
        (FAHRENHEIT, 'fahrenheit'),
    )

    units = models.CharField(
        max_length=2,
        choices=UNITS,
        default=KELVIN,
    )

    date = models.DateTimeField(default=now)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    desc = models.CharField(max_length=120)
    temp = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    icon = models.CharField(max_length=120)

    def __str__(self):
        return self.city
