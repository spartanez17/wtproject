from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from django.http import HttpResponse
import requests


def weather_foo(request):
    # print(request.auth, request.user)
    query = request.GET.get('q', default='')
    appid = '9b672445b6ed15370b9b60aa56725e7d'
    r = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(query, appid))

    return HttpResponse(r.text, status=r.status_code)
