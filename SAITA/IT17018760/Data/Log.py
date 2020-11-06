import datetime
from Data.Variables import log_file, log_enable_all, log_enable_error, log_enable_warning

#This is the python file to creating and writing the log file in each executions
log_types = ["Error", "Warning", "Info"]

#get the current data time
def get_curent_date_and_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def add_log(log_type, file_name, data):
    f = open(log_file, "a") #creating a log file
    if log_enable_all:
        f.write(get_curent_date_and_time() + " : " + file_name + "\n")
        f.write("\t" + log_type + " : " + data + "\n")
    elif log_enable_warning and (log_type == log_types[0] or log_type == log_types[1]):
        f.write(get_curent_date_and_time() + " : " + file_name + "\n")
        f.write("\t" + log_type + " : " + data + "\n")
    elif log_enable_error and log_type == log_types[0]:
        f.write(get_curent_date_and_time() + " : " + file_name + "\n")
        f.write("\t" + log_type + " : " + data + "\n")
    f.close()

