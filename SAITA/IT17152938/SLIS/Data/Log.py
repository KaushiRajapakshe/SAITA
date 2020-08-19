import datetime
from Data.Veriables import log_file, log_enable_all, log_enable_error, log_enable_warning
from Gui.GuiError import GuiError

log_types = ["Error", "Warning", "Info", "NormalError"]


def get_curent_date_and_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def add_log(log_type, file_name, data):
    f = open(log_file, "a")
    ch = False
    if log_type == log_types[3]:
        log_type = log_types[0]
        ch = True
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

    if log_type == log_types[0] and ch:
        er = GuiError(data)
        er.show2()
    elif log_type == log_types[0]:
        er = GuiError(data)
        er.show()
