from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from articles.services.weather_service import WeatherService
from .serializers import WeatherQuerySerializer, WeatherSerializer, ModelWeatherSerializer

from articles.models import Weather
from datetime import datetime
import requests
import json


class WeatherView(APIView):
    permission_classes = (IsAuthenticated,)
    model = Weather
    q_serializer = WeatherQuerySerializer
    w_serializer = WeatherSerializer
    m_serializer = ModelWeatherSerializer
    weather_service = WeatherService()

    def get(self, request, format=None):
        queries = self.q_serializer(data=request.query_params.dict())
        if not queries.is_valid():
            return HttpResponse(queries.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        weather_responce = self.weather_service.getWeather(**queries.data)

        return HttpResponse(weather_responce, status=status.HTTP_200_OK)
