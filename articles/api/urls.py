from django.urls import path
from .views import weather_foo, WeatherView


urlpatterns = [
    # path('weather_old/', weather_foo),
    path('weather/', WeatherView.as_view())
]
