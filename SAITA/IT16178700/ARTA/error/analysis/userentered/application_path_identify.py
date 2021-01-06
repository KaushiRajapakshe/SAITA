import os
import re
import winapps

from ARTA.typesoferrors import phrases
from ARTA.controllers.ontology import query_controller
from ARTA.data import validate

# Identify application path from Application name
# Get Error model details for identify
from ARTA.ontology import query


def check_application_path(self):
    # Get Error Application name
    application_name = self.get_application_name()

    # Define application path string variable as null
    application_path = ''

    # Find installed application path from OS
    for app in winapps.search_installed(application_name):
        application_path = app.install_location

    return application_path


def application_path_identify(application_name):

    # Define application list array
    application_list = []

    # GET application name list
    query_type = query.get_application_type()
    application_name_list = query_controller.execute_query(query_type)

    for application_n in application_name_list:
        if application_n == application_name:
            # Find installed application path from OS
            for app in winapps.search_installed(application_name):

                # Search Application Path on OS
                if app.install_location != '':
                    for root, dirs, files in os.walk(app.install_location):
                        for d in dirs:
                            for ap in validate.application_validate:
                                if re.search(application_name + '\\b', str(ap[0]), re.IGNORECASE) and re.search(
                                        str(ap[1]+"$"), str(d), re.IGNORECASE):
                                    application_list.append([application_name, str(os.path.join(root, d)), ap[1]])

                        for f in files:
                            for ap in validate.application_validate:
                                if re.search(r'\b' + application_name + '\\b', str(ap[0]), re.IGNORECASE) and re.search(
                                        str(ap[1])+"$", str(f)):
                                    application_list.append([application_name, str(os.path.join(root, f)), ap[1]])

    if len(application_list) == 0:
        for ap in validate.application_validate:
            if re.search(application_name + '\\b', str(ap[0]), re.IGNORECASE):
                application_list.append([application_name, '', ap[1]])
    # [Application name, application installed path, process name]
    return application_list


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
