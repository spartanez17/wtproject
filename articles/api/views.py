import json

from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from articles.models import Weather
from articles.services.weather_service import WeatherService
from .serializers import WeatherQuerySerializer


class WeatherView(APIView):
    permission_classes = (IsAuthenticated,)
    model = Weather
    q_serializer = WeatherQuerySerializer
    weather_service = WeatherService()

    def get(self, request):
        queries = self.q_serializer(data=request.query_params.dict())
        if not queries.is_valid():
            return HttpResponse(queries.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        weather_response = self.weather_service.get_weather(**queries.data, exp_period_min=20)

        return HttpResponse(json.dumps(weather_response), status=status.HTTP_200_OK)
