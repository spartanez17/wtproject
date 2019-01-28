from django.urls import path
from .views import weather_foo, Weather


urlpatterns = [
    path('weather/', weather_foo),
    path('weather2/', Weather.as_view())
]
