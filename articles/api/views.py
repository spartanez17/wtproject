from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .services.weather_service import OpenWeatherMapService
from .serializers import WeatherSerializer
from articles.models import Weather

import requests
import json


open_weather_service = OpenWeatherMapService()


class WeatherView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        queries = request.query_params.dict()
        try:
            weather_object = open_weather_service.getWeather(**queries)
            # print(weather_object.__dict__)
            serializer = WeatherSerializer(data=weather_object.__dict__)
            if serializer.is_valid():
                print(serializer.errors)
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)

        except ValueError as e:
            response = Response(e.args, status=400)
