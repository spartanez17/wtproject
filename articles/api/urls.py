from django.urls import path
from .views import  weather_foo

urlpatterns = [
    path('', weather_foo),
    # path('<pk>', ArticleDetailView.as_view())
]
