from django.db import models


# Weather data Model
class WeatherRecords(models.Model):
    station_id = models.CharField(max_length=30, default='', help_text="Used file name as weather station")
    date = models.DateField(default="", blank=False, help_text="Date of this weather record")
    maximum_temperature = models.CharField(max_length=20, default='',
                                           help_text="The maximum temperature for that day (in tenths of a degree Celsius)")
    minimum_temperature = models.CharField(max_length=20, default='',
                                           help_text="The minimum temperature for that day (in tenths of a degree Celsius)")
    amount_of_precipitation = models.CharField(max_length=20, default='',
                                               help_text="The amount of precipitation for that day (in tenths of a millimeter)")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Record creation date and time")
    last_updated = models.DateTimeField(auto_now=True, help_text="Record creation date and time")

    def __str__(self):
        return str(self.date)

    class Meta:
        unique_together = ('station_id', 'date',)
        verbose_name = 'WeatherRecords'
        verbose_name_plural = 'WeatherRecords'


# Yield data Model
class YieldRecords(models.Model):
    year = models.CharField(max_length=20, default='', help_text='Yield of this year in 1000s of megatons')
    yield_value = models.CharField(max_length=20, default='', help_text='Yield Value in 1000s of megatons')
    created_at = models.DateTimeField(auto_now_add=True, help_text="Record creation date and time")
    last_updated = models.DateTimeField(auto_now=True, help_text="Record creation date and time")

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'YieldRecords'
        verbose_name_plural = 'YieldRecords'


# Statistics data Model
class StatRecords(models.Model):
    station_id = models.CharField(max_length=30, default='', unique=True, help_text="Statistics of weather station")
    statistics = models.TextField(default='', help_text='statistics year wise')
    created_at = models.DateTimeField(auto_now_add=True, help_text="Record creation date and time")
    last_updated = models.DateTimeField(auto_now=True, help_text="Record creation date and time")

    def __str__(self):
        return self.station_id

    class Meta:
        verbose_name = 'StatRecords'
        verbose_name_plural = 'StatRecords'
