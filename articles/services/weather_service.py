from datetime import datetime, timedelta

import requests
from django.conf import settings
from django.utils import timezone

from articles.api.serializers import ModelWeatherSerializer  # WeatherSerializer,
from articles.models import Weather


class OpenWeatherMapClient:

    def make_weather_request(self, q):
        payload = {'q': q, 'appid': settings.APP_ID}
        response = requests.get(settings.WEATHER_URL, params=payload)

        if response.status_code is not 200:
            message = 'Weather request failed with {}'.format(response.status_code)
            raise ResourceWarning(message)
        result = self.filter_response(open_weather_map_response=response.json())
        return result

    @staticmethod
    def filter_response(open_weather_map_response):
        weather = open_weather_map_response['weather'][0]
        main = open_weather_map_response['main']
        wind = open_weather_map_response['wind']
        sys = open_weather_map_response['sys']

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


class WeatherService:
    weather_cli = OpenWeatherMapClient()

    def get_weather(self, query, units, exp_period_min):
        now = timezone.now()
        expiration_time = now - timedelta(minutes=exp_period_min)
        queryset = Weather.objects.all()
        q = queryset.filter(city__iexact=query).filter(
            date__range=(expiration_time, now))
        weather_obj = q.first()

        if weather_obj is None:
            response = self.weather_cli.make_weather_request(
                q=query)
            weather_serializer = ModelWeatherSerializer(data=response)
            if weather_serializer.is_valid():
                weather_obj = Weather(**response)
                weather_obj.save()
            else:
                message = 'Weather response not valid'
                raise ResourceWarning(message + weather_serializer.errors)

        serialized_weather = ModelWeatherSerializer(instance=weather_obj)
        response = format_weather(units, serialized_weather.data)

        return response


def format_weather(units, weather_dict):
    temp = weather_dict['temp']
    wind_speed = weather_dict['wind_speed']
    formatted_temp = temp
    formatted_ws = wind_speed
    if units == 'celsius':
        formatted_temp = round((temp - 273.15), 1)

    elif units == 'fahrenheit':
        formatted_temp = round((temp - 273.15) * (9 / 5) + 32, 1)
        formatted_ws = round(wind_speed * 2.23694, 2)

    elif units == 'kelvin':
        return weather_dict

    new_weather_dict = dict(weather_dict)
    new_weather_dict['temp'] = str(formatted_temp)
    new_weather_dict['wind_speed'] = str(formatted_ws)
    return new_weather_dict
