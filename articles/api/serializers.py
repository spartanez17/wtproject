from rest_framework import serializers as ser
from articles.models import Weather


KELVIN = 'kelvin'
CELSIUS = 'celsius'
FAHRENHEIT = 'fahrenheit'
UNITS = (
    (KELVIN, 'kelvin'),
    (CELSIUS, 'celsius'),
    (FAHRENHEIT, 'fahrenheit'),
)


class WeatherSerializer(ser.Serializer):
    city = ser.CharField(max_length=40)
    units = ser.ChoiceField(choices=UNITS)
    date = ser.DateTimeField()
    desc = ser.CharField(max_length=120)
    temp = ser.FloatField()
    humidity = ser.IntegerField(min_value=0, max_value=100)
    wind_speed = ser.FloatField(min_value=0)
    icon = ser.CharField(max_length=120)
    country = ser.CharField(max_length=120)


class WeatherQuerySerializer(ser.Serializer):

    query = ser.CharField(max_length=40)
    units = ser.ChoiceField(choices=UNITS)


class ModelWeatherSerializer(ser.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('__all__')
