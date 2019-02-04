from articles.api.serializers import ModelWeatherSerializer, UNITS
from articles.models import Weather
from .open_weather_map_cli import OpenWeatherMapClient
from django.utils import timezone
from datetime import datetime, timedelta


def converter(o):
    if isinstance(o, datetime):
        return o.timestamp()


class WeatherService:
    weather_cli = OpenWeatherMapClient()

    def get_weather(self, query, units='kelvin', exp_period_min=10):
        now = timezone.now()
        expiration_time = now - timedelta(minutes=exp_period_min)
        queryset = Weather.objects.all()
        q = queryset.filter(city__iexact=query).filter(
            date__range=(expiration_time, now))
        weather_obj = q.first()
        is_fetched = False
        if weather_obj is None:
            response = self.weather_cli.make_weather_request(
                q=query)
            weather_serializer = ModelWeatherSerializer(data=response)
            if weather_serializer.is_valid():
                is_fetched = True
                weather_obj = Weather(**response)
                weather_obj.save()
            else:
                message = 'Weather response not valid'
                raise ResourceWarning(message + weather_serializer.errors)

        serialized_weather = ModelWeatherSerializer(instance=weather_obj)
        response = format_weather(units, serialized_weather.data)
        # check
        response['is_fetched'] = str(is_fetched).lower()
        return response


def format_weather(units, weather_dict):
    if units not in dict(UNITS).values():
        return weather_dict
    temp = weather_dict['temp']
    wind_speed = weather_dict['wind_speed']
    formatted_temp = temp
    formatted_ws = wind_speed
    if units == 'celsius':
        formatted_temp = round((temp - 273.15), 1)

    elif units == 'fahrenheit':
        formatted_temp = round((temp - 273.15) * (9 / 5) + 32, 1)
        formatted_ws = round(wind_speed * 2.23694, 2)

    new_weather_dict = dict(weather_dict)
    new_weather_dict['temp'] = str(formatted_temp)
    new_weather_dict['wind_speed'] = str(formatted_ws)
    return new_weather_dict
