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


class ModelWeatherSerializer(ser.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('__all__')

    def to_representation(self, instance):

        ret = super().to_representation(instance)
        if 'date' in ret.keys():
            date_timestamp = round(instance.date.timestamp())
            ret['date'] = date_timestamp
        return ret


class WeatherQuerySerializer(ser.Serializer):
    query = ser.CharField(max_length=40)
    units = ser.ChoiceField(choices=UNITS)
