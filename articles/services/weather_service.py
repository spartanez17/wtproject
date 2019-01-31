from datetime import datetime, timedelta, time
from django.utils import timezone
from articles.api.serializers import ModelWeatherSerializer
from django.conf import settings
from articles.models import Weather
import requests


class OpenWeatherMapClient():

    def make_weather_request(self, q):
        payload = {'q': q, 'appid': settings.APP_ID}
        response = requests.get(settings.WEATHER_URL, params=payload)

        if response.status_code is not 200:
            raise Warning('REQUEST FAIL')
        result = self.filterResponse(open_weather_map_response=response.json())
        return result

    def filter_response(self, open_weather_map_response):
        weather = open_weather_map_response['weather'][0]
        main = open_weather_map_response['main']
        wind = open_weather_map_response['wind']
        sys = open_weather_map_response['sys']
        dt = open_weather_map_response['dt']
        name = open_weather_map_response['name']
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

    def get_weather(self, query, units):

        now = timezone.now()
        expiration_time = now - timedelta(minutes=10)
        queryset = Weather.objects.all()
        q = queryset.filter(city__iexact=query).filter(
            date__range=(expiration_time, now))
        weather_obj = q.first()
        if weather_obj is None:
            response = self.weather_cli.make_weather_request(
                q=query)
            weather_serializer = ModelWeatherSerializer(data=response)
            if weather_serializer.is_valid():
                weather_obj = Weather(**weather_serializer.data)
                weather_obj.save()

        serialized_weather = ModelWeatherSerializer(instance=weather_obj)
        response = serialized_weather.data

        return response


def format_weather(units, temp, wind_speed):
    formatted_temp = temp
    formatted_ws = wind_speed
    if units == 'celsius':
        formatted_temp = temp - 273.15

    elif units == 'fahrenheit':
        formatted_temp = (temp - 273.15) * (9 / 5) + 32,
        formatted_ws = wind_speed * 2.23694

    return {
        'temp': str(formatted_temp),
        'wind_speed': str(formatted_ws)
    }
