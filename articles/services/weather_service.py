from rest_framework import status
from articles.models import Weather
from django.db.models.functions import Lower
from datetime import datetime, timedelta, time
from django.utils import timezone
from articles.api.serializers import ModelWeatherSerializer
from django.conf import settings
from django.forms.models import model_to_dict
import requests
import json
import pytz


class OpenWeatherMapClient():

    def makeWeatherRequest(self, q):
        payload = {'q': q, 'appid': settings.APP_ID}
        response = requests.get(settings.WEATHER_URL, params=payload)

        if response.status_code is not 200:
            raise Warning('REQUEST FAIL')
        result = self.filterResponse(openweathermapResponse=response.json())
        return result

    def filterResponse(self, openweathermapResponse):
        weather = openweathermapResponse['weather'][0]
        main = openweathermapResponse['main']
        wind = openweathermapResponse['wind']
        sys = openweathermapResponse['sys']
        dt = openweathermapResponse['dt']
        name = openweathermapResponse['name']
        return {
            'desc': weather['description'],
            'icon': weather['icon'],
            'temp': main['temp'],
            'humidity': main['humidity'],
            'wind_speed': wind['speed'],
            'country': sys['country'],
            'city': name
        }


def converter(o):
    if isinstance(o, datetime):
        return o.timestamp()


class WeatherService():
    weather_cli = OpenWeatherMapClient()

    def getWeather(self, query, units):
        city = query
        temp_units = units
        now = timezone.now()
        experation_time = now - timedelta(minutes=10)
        queryset = Weather.objects.all()
        q = queryset.filter(city__iexact=city).filter(
            date__range=(experation_time, now))
        weather_obj = q.first()
        if weather_obj is None:
            response = self.weather_cli.makeWeatherRequest(
                q=city)
            weather_serializer = ModelWeatherSerializer(data=response)
            if weather_serializer.is_valid():
                weather_obj = Weather(weather_serializer.data)
                weather_obj.save()

        serialized_weather = ModelWeatherSerializer(instance=weather_obj)
        print(serialized_weather.data)
        # dict_obj = model_to_dict(weather_obj)
        # serialized = json.dumps(dict_obj, default=converter)
        return serialized_weather.data


def format_weather(units, temp, wind_speed):
    formatted_temp = temp
    formatted_ws = wind_speed
    if units == 'celsius':
        formatted_temp = temp - 273.15
        formatted_ws
    elif units == 'fahrenheit':
        formatted_temp = (temp - 273.15) * (9 / 5) + 32,
        formatted_ws = wind_speed * 2.23694
    return {
        'temp': str(formatted_temp),
        'wind_speed': str(formatted_ws)
    }
