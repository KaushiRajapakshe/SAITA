import datetime
from Data.Veriables import log_file

log_types = ["Error", "Warning", "Info"]


def get_curent_date_and_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def add_log(log_type, file_name, data):
    f = open(log_file, "a")
    f.write(get_curent_date_and_time()+" : "+file_name+"\n")
    f.write("\t"+log_type + " : " + data+"\n")
    f.close()
