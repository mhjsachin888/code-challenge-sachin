import sys
from datetime import datetime


def conver_string_to_date(date_string):
    """
    Function: conver_string_to_date: To convert string to an date object
    Params: date_string (Need to be a 8 character string otherwise return -1)
    Return: Date object
    """
    try:
        # Checking for 8 characters in string
        if len(date_string) == 8:

            # Making formatted string as '2022-09-01'
            final_date_string = date_string[:4] + "-" + date_string[4:6] + "-" + date_string[6:]

            # Converting '2022-09-01' to date object
            date_time_obj = datetime.strptime(final_date_string, '%Y-%m-%d')

            # returning only date from date and time 
            return date_time_obj.date()
        else:
            # Will print that date string is not in required format
            print("Error: Data is not contains 8 characters, Date string is: ", date_string)
            return -1
    except Exception as e:
        # Executes if any exception occurs
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("[Exception] conver_string_to_date: ", str(e), " at line no. ", str(exc_tb.tb_lineno))


def remove_blank_return_clean(value_string):
    """
    Function: remove_blank_return_clean: Will skip the blanks and None and strip the extra characters
    Params: value_string 
    Return: String
    """
    try:
        # Checking for empty, space and None
        if value_string == "" or value_string == " " or value_string is None:
            return
        else:
            # Returning stripped string
            return value_string.strip()
    except Exception as e:
        # Executes if any exception occurs
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("[Exception] remove_blank_return_clean: ", str(e), " at line no. ", str(exc_tb.tb_lineno))


def calculate_average(data, typ):
    """
    Function: calculate_average: Calculating the average values and will skip if None(-9999) found
    Params: data(data dict), typ(name type of the data to process)
    Return: Integer
    """
    try:
        sum_value = 0
        counter = 0
        for value in data:
            if value != -9999:
                sum_value = sum_value + int(value[typ])
                counter = counter + 1
        return round(sum_value / counter, 2)
    except Exception as e:
        # Executes if any exception occurs
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("[Exception] calculate_average: ", str(e), " at line no. ", str(exc_tb.tb_lineno))
        return None


def calculate_sum(data):
    """
    Function: calculate_sum: Calculating the sum of amount_of_precipitation and will skip if None(-9999) found
    Params: data(data dict)
    Return: Integer
    """
    try:
        sum_value = 0
        for value in data:
            if value != -9999:
                sum_value = sum_value + int(value['amount_of_precipitation'])
        return sum_value
    except Exception as e:
        # Executes if any exception occurs
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("[Exception] calculate_sum: ", str(e), " at line no. ", str(exc_tb.tb_lineno))
        return None
