from rest_framework import status
from articles.models import Weather
from django.db.models.functions import Lower
import requests
import json
from datetime import datetime, timedelta, time
from django.utils import timezone
import pytz


def filterResponse(openweathermapResponse):
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
    # 'last_update': datetime.fromtimestamp(dt, tzinfo=pytz.UTC),


WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
unitOpenWeatherMap = {'celsius': 'metric',
                      'kelvin': '', 'fahrenheit': 'imperial'}
APP_ID = '9b672445b6ed15370b9b60aa56725e7d'


class OpenWeatherMapService():
    def getWeather(self, query, units):
        city = query
        temp_units = units
        if (len(city) < 3 or len(city) > 20 or
                temp_units not in unitOpenWeatherMap.keys()):
            raise ValueError('Queries is not valid.')
        time_end = timezone.now()
        experation_time = time_end - timedelta(minutes=10)
        result = {}
        try:
            queryset = Weather.objects.order_by(
                '-date').filter(date__gte=experation_time).get(city__iexact=city)
            result = queryset[:1].get()
        except Weather.DoesNotExist:
            print('--------------\n--------------\n--------------\n--------------\n')
            response = self.makeWeatherRequest(q=city, units=temp_units)
            response['units'] = units
            result = Weather(**response)
            result.save()
        finally:
            return result

    def makeWeatherRequest(self, q, units):
        mapped_units = unitOpenWeatherMap.get(units)
        payload = {'q': q, 'appid': APP_ID, 'units': mapped_units}
        response = requests.get(WEATHER_URL, params=payload)
        result = filterResponse(openweathermapResponse=response.json())
        return result
