from django.urls import path
from .views import  weather_foo

urlpatterns = [
    path('weather/', weather_foo),
]
