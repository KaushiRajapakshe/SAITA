from datetime import datetime
import calendar


# Define scheduler log error identify phrases
def get_phrases():
    keep_phrases = ["Address already in use", "Unable to open logs", "ReservedCodeCacheSize=240m",
                    "Application run failed", "objectMapperConfigurer", "The OSGi framework has been initialised"]
    return keep_phrases


# time regular expression pattern 01 for 2020 21:02:03
def get_regular_expression1():
    regular_expression = r"[0-9][0-9].[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]"
    return regular_expression


# time regular expression pattern 02 for 2020 9:02:03 PM
def get_regular_expression2():
    regular_expression = r"[0-9][0-9].[0-9]\:[0-9][0-9]\:[0-9][0-9]"
    return regular_expression


# GET current time and date version for match log errors
# It limited for current date errors and
# not showing previous errors on preventing scanner result
def get_current_date_versions():
    month = calendar.month_name[datetime.now().month]
    current_month = month[:3]
    current_year = datetime.now().year
    current_day = datetime.now().day

    # current date for '2020-10-25'
    current_date_with_time_v1 = str(datetime.now().date())
    # current date for 'Oct 25'
    current_date_with_time_v2 = str(current_month) + ' ' + str(current_day)
    # current date for 'Oct 25, 2020'
    current_date_with_time_v3 = str(current_date_with_time_v2) + ', ' + str(current_year)
    date_list = [current_date_with_time_v1, current_date_with_time_v2, current_date_with_time_v3]
    return date_list


# port regular expression pattern 01 for 8-5
def get_port_regular_expression1():
    regular_expression = r"[0-9]"
    return regular_expression


# port regular expression pattern 02 for 80
def get_port_regular_expression2():
    regular_expression = r"[0-9][0-9]"
    return regular_expression


# port regular expression pattern 03 for 808
def get_port_regular_expression3():
    regular_expression = r"[0-9][0-9][0-9]"
    return regular_expression


# port regular expression pattern 04 for 8080
def get_port_regular_expression4():
    regular_expression = r"[0-9][0-9][0-9][0-9]"
    return regular_expression


# port regular expression pattern 05 for 65535
def get_port_regular_expression5():
    regular_expression = r"[0-9][0-9][0-9][0-9][0-9]"
    return regular_expression
