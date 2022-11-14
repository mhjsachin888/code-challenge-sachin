from django.urls import path
from . import views

# API End points as per requirement
urlpatterns = [
    path('weather', views.WeatherDataAPI.as_view(), name="weather"),
    path('yield', views.YieldDataAPI.as_view(), name="yield"),
    path('weather/stats', views.StatsDataAPI.as_view(), name="stats"),

]
