import os
import sys


def load_weather_data():
    # Importing some required files and functions
    import os, time
    from tqdm import tqdm
    from django.conf import settings
    from Weather.MainApp.models import WeatherRecords
    from Weather.MainApp.utils import conver_string_to_date, remove_blank_return_clean
    try:
        # Initializing the counter to record how many records we have inserted
        record_counter = 0

        # Reading all files names from wx_data directory and making a list of all file names.
        all_station_ids = list(os.listdir(settings.WEATHER_DATA_DIRECTORY_NAME))

        # Start time of the processing 
        start_time = time.time()

        # Iterating over all the files 
        for station_id in tqdm(all_station_ids):

            # Opening the files in read mode
            file_data = open(settings.WEATHER_DATA_DIRECTORY_NAME + "/" + str(station_id), "r")

            # Reading all lines 
            all_data_lines = file_data.readlines()

            # iterating all the lines in that particular file
            for i in all_data_lines:

                # Will skip the blanks and None and strip the extra characters and get clean list with 4 records
                record = list(map(remove_blank_return_clean, i.split()))

                # Checking for only 4 records in the list
                if len(record) == 4:

                    # Unpacking the list 
                    date, maximum_temperature, minimum_temperature, amount_of_precipitation = record

                    # Convert date string to date object
                    date = conver_string_to_date(date)
                    if date != -1:
                        try:
                            # Creating the objects of weather records
                            WeatherRecords.objects.create(
                                station_id=str(station_id).split(".")[0],
                                date=date,
                                maximum_temperature=maximum_temperature,
                                minimum_temperature=minimum_temperature,
                                amount_of_precipitation=amount_of_precipitation
                            )
                            # Increasing the counter by 1 when we have inserted data
                            record_counter = record_counter + 1
                        except:
                            # Will be executed if any exception occurs while creating objects in database
                            pass

        # End time of the processing 
        end_time = time.time()

        # Log with number of records and time taken to complete the process of database creation from the files
        print("Congratulations! You have successfully uploaded Weather data into the database and total number of "
              "records ", record_counter, " inserted. And time taken to insert all these records is ", (end_time -
                                                                                                        start_time) / 60,
              "Minutes.")
    except Exception as e:
        # Will be executed when any exception occurs
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("[Exception] load_weather_data: ", str(e), " at line no. ", str(exc_tb.tb_lineno))


def load_yield_data():
    import os, time
    from django.conf import settings
    from tqdm import tqdm
    from Weather.MainApp.models import YieldRecords
    from Weather.MainApp.utils import remove_blank_return_clean
    try:
        # Reading all files names from wx_data directory and making a list of all file names.
        all_file_names = list(os.listdir(settings.YIELD_DATA_DIRECTORY_NAME))

        # Start time of the processing 
        start_time = time.time()

        # Initializing the counter to record how many records we have inserted
        record_counter = 0

        # Iterating over all the files 
        for file_name in all_file_names:

            # Opening the files in read mode
            file_data = open(settings.YIELD_DATA_DIRECTORY_NAME + "/" + str(file_name), "r")

            # Reading all lines 
            all_data_lines = file_data.readlines()

            # iterating all the lines in that particular file
            for i in all_data_lines:

                # Will skip the blanks and None and strip the extra characters and get clean list with 4 records
                record = list(map(remove_blank_return_clean, i.split()))

                # Checking for only 2 records in the list
                if len(record) == 2:

                    # Unpacking the list 
                    year, yield_value = record

                    # Checking if there is already exists this record
                    if YieldRecords.objects.filter(year=year, yield_value=yield_value).exists():
                        pass
                    else:
                        # Creating the objects of yield records
                        YieldRecords.objects.create(
                            year=year,
                            yield_value=yield_value
                        )
                        # Increasing the counter by 1 when we have inserted data
                        record_counter = record_counter + 1

        # End time of the processing 
        end_time = time.time()

        # Log with number of records and time taken to complete the process of database creation from the files
        print("Congratulations! You have successfully uploaded Yield data into the database and total number of "
              "records ", record_counter, " inserted. And time taken to insert all these records is ", (end_time -
                                                                                                        start_time),
              " Seconds.")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("[Exception] load_yield_data: ", str(e), " at line no. ", str(exc_tb.tb_lineno))


def create_weather_statistics():
    from tqdm import tqdm
    import json, time
    from Weather.MainApp.utils import calculate_average, calculate_sum
    from django.db.models import Avg
    from django.db.models import Sum
    from django.conf import settings
    from Weather.MainApp.models import WeatherRecords, StatRecords
    try:
        # Start time of the processing 
        start_time = time.time()

        # Initializing the counter to record how many records we have inserted
        record_counter = 0

        # Reading all files names from wx_data directory and making a list of all file names.
        all_station_ids = list(os.listdir(settings.WEATHER_DATA_DIRECTORY_NAME))

        # Iterating over all the station ids 
        for station_id in tqdm(all_station_ids):
            statistics_data = {}

            # As we know we have data from 1985 to 2014, so we are iterating on all years to filter data
            for year in range(1985, 2015):

                # Filtering data from database based on year and station id
                filtered_data = WeatherRecords.objects.filter(station_id=str(station_id).split(".")[0],
                                                              date__year=str(year))
                if filtered_data:
                    # Creating dictionary with average values
                    statistics_data[year] = {
                        "average_maximum_temperature": calculate_average(filtered_data.values("maximum_temperature"),
                                                                         'maximum_temperature'),
                        "average_minimum_temperature": calculate_average(filtered_data.values("minimum_temperature"),
                                                                         'minimum_temperature'),
                        "total_accumulated_precipitation": (calculate_sum(
                            filtered_data.values("amount_of_precipitation"))) / 10
                    }
            try:
                # Creating the objects of statistics records
                StatRecords.objects.create(
                    station_id=str(station_id).split(".")[0],
                    statistics=json.dumps(statistics_data)
                )
                # Increasing the counter by 1 when we have inserted data
                record_counter = record_counter + 1
            except:

                # Record will be updated
                StatRecords.objects.filter(station_id=str(station_id).split(".")[0]).update(
                    statistics=json.dumps(statistics_data))

        # End time of the processing 
        end_time = time.time()

        # Log with number of records and time taken to complete the process of database creation from the files
        print("Congratulations! You have successfully uploaded Yield data into the database and total number of "
              "records ", record_counter, " inserted. And time taken to insert all these records is ", (end_time -
                                                                                                        start_time),
              " Seconds.")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("[Exception] create_weather_statistics: ", str(e), " at line no. ", str(exc_tb.tb_lineno))


load_weather_data()
load_yield_data()
create_weather_statistics()
