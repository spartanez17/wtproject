from rest_framework import serializers
from articles.models import Weather


# class WeatherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Weather
#         fields = '__all__'


class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=120)
    units = serializers.ChoiceField(choices=Weather.UNITS)
    date = serializers.DateTimeField()
    desc = serializers.CharField(max_length=120)
    temp = serializers.FloatField()
    humidity = serializers.IntegerField(min_value=0, max_value=100)
    wind_speed = serializers.FloatField(min_value=0)
    icon = serializers.CharField(max_length=120)
    country = serializers.CharField(max_length=120)
