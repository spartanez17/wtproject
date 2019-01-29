from rest_framework import status
import requests
import json
import time
import datetime


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
        'windSpeed': wind['speed'],
        'date': dt,
        'country': sys['country'],
        'city': name
    }


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
            return {
                'message': 'Weather could not be provided with received params.',
                'status': status.HTTP_422_UNPROCESSABLE_ENTITY
            }

        mapped_units = unitOpenWeatherMap.get(units)
        payload = {'q': city, 'appid': APP_ID, 'units': mapped_units}
        response = requests.get(WEATHER_URL, params=payload)
        result = filterResponse(openweathermapResponse=response.json())
        return result
