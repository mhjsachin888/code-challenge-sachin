from rest_framework import serializers
from .models import WeatherRecords


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherRecords
        fields = ['station_id', 'date', 'maximum_temperature', 'minimum_temperature', 'amount_of_precipitation']
