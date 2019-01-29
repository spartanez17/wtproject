from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .services.weather_service import OpenWeatherMapService
import requests
import json

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
unitOpenWeatherMap = {'celsius': 'metric',
                      'kelvin': '', 'fahrenheit': 'imperial'}
open_weather_service = OpenWeatherMapService()


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


def weather_foo(request):
    query = request.GET.get('query', default='')
    units = request.GET.get('units', default='')
    mapped_units = unitOpenWeatherMap.get(units)
    app_id = '9b672445b6ed15370b9b60aa56725e7d'
    payload = {'q': query, 'appid': app_id, 'units': mapped_units}
    response = requests.get(WEATHER_URL, params=payload)
    print(response.json())
    result = filterResponse(openweathermapResponse=response.json())
    return HttpResponse(json.dumps(result), status=response.status_code)


class WeatherView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        queries = request.query_params.dict()
        response = open_weather_service.getWeather(**queries)
        return Response(response)




        # print('---')
        # print(queries)
        # print('---')
