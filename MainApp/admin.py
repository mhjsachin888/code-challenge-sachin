from django.contrib import admin
from .models import WeatherRecords, YieldRecords, StatRecords

admin.site.register(WeatherRecords)
admin.site.register(YieldRecords)
admin.site.register(StatRecords)
