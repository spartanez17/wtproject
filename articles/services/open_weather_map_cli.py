import requests
from django.conf import settings

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
