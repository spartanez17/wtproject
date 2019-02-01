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


# class WeatherSerializer(ser.Serializer):
#     id = ser.IntegerField(read_only=True)
#     date = ser.DateTimeField(required=False)
#     country = ser.CharField(max_length=120)
#     city = ser.CharField(max_length=40)
#     desc = ser.CharField(max_length=120)
#     temp = ser.FloatField()
#     humidity = ser.IntegerField(min_value=0, max_value=100)
#     wind_speed = ser.FloatField(min_value=0)
#     icon = ser.CharField(max_length=120)
#
#     def to_representation(self, instance):
#         """Convert `username` to lowercase."""
#         ret = super().to_representation(instance)
#         if 'date' in ret.keys():
#             ret['date'] = str(ret['date'].timestamp())
#         return ret


class ModelWeatherSerializer(ser.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('__all__')

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        if 'date' in ret.keys():
            date_timestamp = round(instance.date.timestamp())
            ret['date'] = date_timestamp
        return ret


class WeatherQuerySerializer(ser.Serializer):
    query = ser.CharField(max_length=40)
    units = ser.ChoiceField(choices=UNITS)
