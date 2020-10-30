import os
import re

from SAITA.IT16178700 import phrases
from SAITA.IT16178700.data.log import add_log, log_types
from SAITA.IT16178700.error.analysis.scheduler import drives_list
from SAITA.IT16178700.model import ESubDetail


# Identify application path from Application name
# Get Error model details for identify


def application_path_identify(self):
    # application_name = self.get_application_name()
    application_version = self.get_application_version()
    error_description = self.get_error_description()
    application_name = 'PyCharm'
    self.set_application_path(search_application_path(application_name))

    add_log(log_types[2], "Application Path Identify : ",
            application_version + ' ' + application_name + ' ' + error_description + ' ' + self.get_application_path())


# Search Application Path on OS
def search_application_path(get_application_name):
    path_list = []
    for head_dir in drives_list.get_os_drives_list():
        for root, dirs, files in os.walk(head_dir):
            for d in dirs:
                if d == get_application_name:
                    path_list.append(os.path.join(root, d))

    # If Application not installed in OS return as empty
    if len(path_list) == 0:
        return ''
    # If Application installed in OS return the application path
    else:
        return path_list[0]


# Check user who entered valid port
def check_port(error_description, self):
    port = 65538
    # regular expression patterns
    regular_expression1 = phrases.get_port_regular_expression1()
    expression1 = re.compile(regular_expression1)
    regular_expression2 = phrases.get_port_regular_expression2()
    expression2 = re.compile(regular_expression2)
    regular_expression3 = phrases.get_port_regular_expression3()
    expression3 = re.compile(regular_expression3)
    regular_expression4 = phrases.get_port_regular_expression4()
    expression4 = re.compile(regular_expression4)
    regular_expression5 = phrases.get_port_regular_expression5()
    expression5 = re.compile(regular_expression5)
    e5 = expression5.search(error_description)
    e4 = expression4.search(error_description)
    e3 = expression3.search(error_description)
    e2 = expression2.search(error_description)
    e1 = expression1.search(error_description)

    if e5:
        port = e5.group()
    elif e4:
        port = e4.group()
    elif e3:
        port = e3.group()
    elif e2:
        port = e2.group()
    elif e1:
        port = e1.group()

    for x in range(0, 65535):
        try:
            if str(x) == str(port):
                self.set_solution(port)
                return 'True'
        except IndexError:
            return 'False'


# Check user who entered valid port
def check_application_port(error_description, e):
    port = 65538
    # regular expression patterns
    regular_expression1 = phrases.get_port_regular_expression1()
    expression1 = re.compile(regular_expression1)
    regular_expression2 = phrases.get_port_regular_expression2()
    expression2 = re.compile(regular_expression2)
    regular_expression3 = phrases.get_port_regular_expression3()
    expression3 = re.compile(regular_expression3)
    regular_expression4 = phrases.get_port_regular_expression4()
    expression4 = re.compile(regular_expression4)
    regular_expression5 = phrases.get_port_regular_expression5()
    expression5 = re.compile(regular_expression5)
    e5 = expression5.search(error_description)
    e4 = expression4.search(error_description)
    e3 = expression3.search(error_description)
    e2 = expression2.search(error_description)
    e1 = expression1.search(error_description)

    if e5:
        port = e5.group()
    elif e4:
        port = e4.group()
    elif e3:
        port = e3.group()
    elif e2:
        port = e2.group()
    elif e1:
        port = e1.group()

    for x in range(0, 65535):
        try:
            if str(x) == str(port):
                e.set_application_path(port)
                return 'True'
        except IndexError:
            return 'False'
