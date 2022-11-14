import json
import sys
from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.views import APIView

from .models import WeatherRecords, YieldRecords, StatRecords
from .utils import conver_string_to_date


class WeatherDataAPI(APIView):
    """
    WeatherDataAPI: Api for Weather data
    Features: 
    1. We can get complete data with pagination
    2. We can filter data based on stationid and date by both of them or any one of them
    Return: Will return Json Data
    """

    def get(self, request, format=None):
        try:
            # Reading query parameters
            stationid = request.GET.get("stationid")
            date = request.GET.get("date")

            # Checking any query parameter presented or not
            if any([stationid, date]):
                if stationid is not None and date is not None:
                    # Execute if Both query params found

                    # Converting 19850101 -> date objects
                    date = conver_string_to_date(date)

                    # if date string validation fails then date will be -1
                    if date != -1:
                        # Filter WeatherRecords models with both stationid and date
                        weather_data = WeatherRecords.objects.filter(station_id=stationid, date=date).values(
                            'station_id', 'date', 'maximum_temperature', 'minimum_temperature',
                            'amount_of_precipitation')

                        # Return date 
                        # Pagination does not require because one record could be found
                        return JsonResponse({"status": 200, "data": list(weather_data)})
                elif stationid is None and date is not None:
                    # Execute if date query params found
                    date = conver_string_to_date(date)
                    if date != -1:
                        # Filter WeatherRecords models with date
                        weather_data = WeatherRecords.objects.filter(date=date).values('station_id', 'date',
                                                                                       'maximum_temperature',
                                                                                       'minimum_temperature',
                                                                                       'amount_of_precipitation')

                        # Get Paginator
                        paginator = Paginator(weather_data, settings.RECORDS_PER_PAGE)

                        # Read page number of present as a query
                        page_number = request.GET.get('page')

                        # Get Data based on page number
                        page_obj = paginator.get_page(page_number)

                        # Return date 
                        return JsonResponse({"status": 200, "data": list(page_obj)})
                elif stationid is not None and date is None:
                    # Execute if stationid query params found

                    # Filter WeatherRecords models with stationid
                    weather_data = WeatherRecords.objects.filter(station_id=stationid).values('station_id', 'date',
                                                                                              'maximum_temperature',
                                                                                              'minimum_temperature',
                                                                                              'amount_of_precipitation')
                    paginator = Paginator(weather_data, settings.RECORDS_PER_PAGE)
                    page_number = request.GET.get('page')
                    page_obj = paginator.get_page(page_number)

                    # Return date 
                    return JsonResponse({"status": 200, "data": list(page_obj)})

            # Will execute when there is not any query parameter found and will return complete data with pagination
            weather_data = WeatherRecords.objects.all().values('station_id', 'date', 'maximum_temperature',
                                                               'minimum_temperature', 'amount_of_precipitation')
            paginator = Paginator(weather_data, settings.RECORDS_PER_PAGE)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            # Return date 
            return JsonResponse({"status": 200, "data": list(page_obj)})
        except Exception as e:
            # Will be executed when any exception occurs
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("[Exception] WeatherDataAPI: ", str(e), " at line no. ", str(exc_tb.tb_lineno))
            return JsonResponse({"status": 500, "data": str(e)})


class YieldDataAPI(APIView):
    """
    YieldDataAPI: Api for Yield data
    Features: 
    1. We can get complete data with pagination
    Return: Will return Json Data
    """

    def get(self, request, format=None):
        try:
            # Getting complete data with 'year', 'yield_value' fields only
            yield_data = YieldRecords.objects.all().values('year', 'yield_value')
            paginator = Paginator(yield_data, settings.RECORDS_PER_PAGE)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return JsonResponse({"status": 200, "data": list(page_obj)})
        except Exception as e:
            # Will be executed when any exception occurs
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("[Exception] YieldDataAPI: ", str(e), " at line no. ", str(exc_tb.tb_lineno))
            return JsonResponse({"status": 500, "data": str(e)})


class StatsDataAPI(APIView):
    """
    StatsDataAPI: Api for Statistics data
    Features: 
    1. We can get complete statistics data with pagination
    Return: Will return Json Data
    """

    def get(self, request, format=None):
        try:
            # Getting complete data with 'station_id', 'statistics' fields only
            stat_data = StatRecords.objects.all().values('station_id', 'statistics')
            paginator = Paginator(stat_data, settings.RECORDS_PER_PAGE)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            final_data = []

            # Converting statistics string to json data object
            for data in list(page_obj):
                final_data.append({
                    "station_id": data['station_id'],
                    "statistics": json.loads(data['statistics'])
                })

            # Return data
            return JsonResponse({"status": 200, "data": final_data})
        except Exception as e:
            # Will be executed when any exception occurs
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("[Exception] YieldDataAPI: ", str(e), " at line no. ", str(exc_tb.tb_lineno))
            return JsonResponse({"status": 500, "data": str(e)})
