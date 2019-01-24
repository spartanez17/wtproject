from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from django.http import HttpResponse
import requests
import json

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
unitMap = {'celsius': 'metric', 'kelvin': '', 'fahrenheit': 'imperial'}


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

    query = request.GET.get('query', default='loklololol')
    units = request.GET.get('units', default='lololollool3')
    mappedUnits = unitMap.get(units)
    appId = '9b672445b6ed15370b9b60aa56725e7d'
    payload = {'q': query, 'appid': appId, 'units': mappedUnits}
    response = requests.get(WEATHER_URL, params=payload)
    # print(response)
    print(response.json())
    result = filterResponse(openweathermapResponse=response.json())
    return HttpResponse(json.dumps(result), status=response.status_code)
