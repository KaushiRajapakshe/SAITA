import datetime
from ARTA.data.variables import log_file, log_enable_all, log_enable_error, log_enable_warning

# Log status types
log_types = ["Error", "Warning", "Info"]


# GET Current date and time for log writer
def get_current_date_and_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


# Write System logs in foi.log file
def add_log(log_type, file_name, data):
    f = open(log_file, "a")
    if log_enable_all or (log_enable_warning and (log_type == log_types[0] or log_type == log_types[1])) or (
            log_enable_error and log_type == log_types[0]):
        f.write(get_current_date_and_time() + " : " + file_name + "\n")
        f.write("\t" + log_type + " : " + data + "\n")
    f.close()
