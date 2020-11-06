import copy

from SAITA.IT16178700.constant import constants
from SAITA.IT16178700.data import variables
from SAITA.IT16178700.error.analysis.scheduler import scanner
from SAITA.IT16178700.error.analysis.userentered.application_path_identify import application_path_identify, check_port, \
    check_application_path
from SAITA.IT16178700.model.Error import Error
from SAITA.IT16178700.model.ESubDetail import ESubDetail
from SAITA.IT16178700.model.Chat import TestChat
from SAITA.IT16178700.model.SayText import SayText
from SAITA.IT16178700.ontology import query
from SAITA.IT16178700.controllers.ontology import query_controller
from SAITA.IT16178700.controllers.shell_script import shell_script_controller as schell
from SAITA.IT16178700.data.log import add_log, log_types
import re


# Identify user entered application version
# for that clean application version data
# to match with ontology data
def clean_version_data(ap_version):
    v1 = ap_version.replace('___', ' ')
    v2 = v1.replace('__', '-')
    v3 = v2.replace('_', '.')
    return v3


# Pre selected application problem solving system
# Chat Agent Controller
class ChatController:
    next_q = []
    chat = None

    # Pre selected questionnaires list
    application_q = ['Sorry.. We missed it. Please try out for other.',
                     'Please enter your application name.?',
                     'Please enter your application version.?',
                     'Please enter your error description.?',
                     'Please wait until error analyzing.',
                     'Do you need to continue.? (Yes/No)',
                     'Your problem is solved. Do you have any other problem? (Yes/No)',
                     'System has no issue to find. Do you have any other problem? (Yes/No)',
                     'Do you have any other problem? (Yes/No)',
                     'Preventing scanner will take few minutes. Do you want to continue... (Yes/No)',
                     'Hi!!! This is SAITA pre selected application problem solving system.Do you like to run error '
                     'preventing scan for your operating system.? (Yes / No)',
                     'Please enter valid port for analyze the error.',
                     'Please enter the scanner issue number to solve.']

    global error_list, error_dist
    error_dict = {}
    error_scan_list = []

    def __init__(self):
        self.loop = 0
        self.chat = TestChat()
        self.error = Error()
        self.eSubDetail = ESubDetail()

    def chat_question_sequence(self, work_area, acc_ra, roott):

        # User Entered
        if (re.search(r'\bno\b', self.chat.get_lastuserreply()) or re.search(r'\bNo\b',
                                                                             self.chat.get_lastuserreply())) and self.loop == 0:
            self.chat.set_sitarep(self.application_q[1])
            SayText.get_say_text().say(variables.q2)
            self.loop = 1
        # Scheduler
        elif self.loop == 10:
            # Check User want to run scheduler
            if re.search(r'\bno\b', self.chat.get_lastuserreply()) or re.search(r'\bNo\b',
                                                                                self.chat.get_lastuserreply()):
                self.chat.set_sitarep(self.application_q[10])
                SayText.get_say_text().say(variables.q11)
                self.loop = 0
            elif re.search(r'\byes\b', self.chat.get_lastuserreply()) or re.search(r'\bYes\b',
                                                                                   self.chat.get_lastuserreply()):
                self.error_scan_list = scanner.scanner_details(work_area, acc_ra, roott)
                self.loop = 11
                if self.loop == 11:
                    chat_list = ''
                    # Check scanner error list empty
                    if len(self.error_scan_list) == 0:
                        self.chat.set_sitarep("No issues to find." + self.application_q[5])
                        SayText.get_say_text().say(variables.q14+variables.q6)
                        self.loop = 0
                    else:
                        # Show Scanner error list
                        for e in self.error_scan_list:
                            if not chat_list == '':
                                chat_list += '\n\t' + str(e.get_error_description())
                            else:
                                chat_list = '\t' + str(e.get_error_description())
                                self.loop = 12

                    self.chat.set_sitarep(chat_list+'\n'+self.application_q[12])
                    SayText.get_say_text().say(variables.q13)
            else:
                self.chat.set_sitarep(self.application_q[0])
                SayText.get_say_text().say(variables.q1)
                self.loop = 0

        # Execute Scheduler error solution scripts
        elif self.loop == 12:
            if type(int(self.chat.get_lastuserreply())) == int:
                schell.shell_script_write(variables.script1)
                self.error_scan_list[int(self.chat.get_lastuserreply())-1]

                # Todo: Check error with KB data and execute solution by powershell script
                self.chat.set_sitarep(self.application_q[6])
                SayText.get_say_text().say(variables.q7)
                self.loop = 8
            else:
                self.chat.set_sitarep(self.application_q[0])
                SayText.get_say_text().say(variables.q1)
                self.loop = 12
        #         Todo : Iterate for other errors
        # Check scheduler want to continue
        elif self.loop == 8:
            if re.search(r'\bno\b', self.chat.get_lastuserreply()) or re.search(r'\bNo\b',
                                                                                self.chat.get_lastuserreply()):
                exit()
            elif re.search(r'\byes\b', self.chat.get_lastuserreply()) or re.search(r'\bYes\b',
                                                                                   self.chat.get_lastuserreply()):
                self.chat.set_sitarep(self.application_q[12])
                SayText.get_say_text().say(variables.q13)
                self.loop = 12
            else:
                self.chat.set_sitarep(self.application_q[0])
                SayText.get_say_text().say(variables.q1)
                self.loop = 0

        elif (re.search(r'\byes\b', self.chat.get_lastuserreply()) or re.search(r'\bYes\b',
                                                                                self.chat.get_lastuserreply())) and \
                self.loop == 0:
            self.chat.set_sitarep(self.application_q[9])
            SayText.get_say_text().say(variables.q10)
            self.loop = 10

        # Application name check
        elif self.loop == 1:
            query_type = query.get_application_type()
            application_name = query_controller.execute_query(query_type)
            for ap_name in application_name:
                if re.search(r'\b' + ap_name + '\\b', self.chat.get_lastuserreply(), re.IGNORECASE):
                    self.loop = 2
                    # Set Error application name
                    self.error.set_application_name(ap_name)
            # Check Application installed in OS
            if check_application_path(self.error) != '' and self.loop == 2:
                self.chat.set_sitarep(self.application_q[2])
                SayText.get_say_text().say(variables.q3)
            elif self.error.get_application_name() != '' and check_application_path(self.error) == '':
                self.chat.set_sitarep(self.error.get_application_name() + ' is not installed in your operating system. '
                                                                          'Please try out for other application.')
                SayText.get_say_text().say(self.error.get_application_name()+variables.q15)
                self.loop = 1
                self.error.set_application_name('')
            else:
                self.chat.set_sitarep(self.application_q[0])
                SayText.get_say_text().say(variables.q1)

        # Application version check
        elif self.loop == 2:
            query_type = query.check_app_version(constants.APPLICATION_NAME, self.chat.get_check_userreply(),
                                                 constants.APPLICATION_VERSION)
            application_version = query_controller.execute_query(query_type)
            for ap_version in application_version:
                if re.search(r'\b' + clean_version_data(ap_version) + '\\b', self.chat.get_lastuserreply(),
                             re.IGNORECASE):
                    self.loop = 3
                    # Set Error application version
                    self.error.set_application_version(ap_version)
            if self.loop == 3:
                self.chat.set_sitarep(self.application_q[3])
                SayText.get_say_text().say(variables.q4)
            else:
                self.chat.set_sitarep(self.application_q[0])
                SayText.get_say_text().say(variables.q1)

        # Application description check
        elif self.loop == 3:
            query_type = query.check_error_description(constants.APPLICATION_VERSION, self.chat.get_check_userreply(),
                                                       constants.ERROR_DESCRIPTION)
            error_description = query_controller.execute_query(query_type)
            for er in error_description:
                if re.search(r'\b' + er + '\\b', self.chat.get_lastuserreply(), re.IGNORECASE):
                    # Set Error error description
                    self.error.set_error_description(er)
                    self.chat.set_sitarep(self.application_q[4])
                    SayText.get_say_text().say(variables.q5)
                    self.loop = 5

        # Application error status check
        elif self.loop == 5:
            # Application error target check
            query_type = query.get_error_target(constants.APPLICATION_NAME, constants.ERROR_DESCRIPTION,
                                                constants.APPLICATION_VERSION, self.error.get_application_name(),
                                                self.error.get_error_description(),
                                                self.error.get_application_version())
            error_target = query_controller.execute_query(query_type)
            self.eSubDetail.set_solution('none')
            result_value = ''
            # Check valid port range
            if check_port(self.chat.get_check_userreply(), self.eSubDetail) == 'True':
                port = self.eSubDetail.get_solution()
                if port != '' and re.search(r'\bport_number\b', error_target[0]):
                    script = str(error_target[0]).replace('port_number', port)
                    result = schell.shell_script_write(script)
                    try:
                        result_value = int(re.search(r'\d+', result).group())
                        if result_value != '':
                            if self.error.get_error_description() == constants.PORT_BLOCK:
                                self.eSubDetail.set_solution('none')
                                # Check valid port range
                                if check_port(self.chat.get_check_userreply(), self.eSubDetail) == 'True':
                                    query_type = query.get_error_status(constants.APPLICATION_NAME,
                                                                        constants.ERROR_DESCRIPTION,
                                                                        constants.APPLICATION_VERSION,
                                                                        self.error.get_application_name(),
                                                                        self.error.get_error_description(),
                                                                        self.error.get_application_version())
                                    error_status = query_controller.execute_query(query_type)
                                    self.chat.set_sitarep(error_status[0] + self.application_q[5])
                                    SayText.get_say_text().say(variables.q6)
                                    self.loop = 6
                                else:
                                    self.chat.set_sitarep(self.application_q[11])
                                    SayText.get_say_text().say(variables.q12)
                                    self.loop = 3
                    except TypeError:
                        self.chat.set_sitarep("No issues to find." + self.application_q[8])
                        SayText.get_say_text().say(variables.q9)
                        self.loop = 7
            else:
                if re.search(r'\bprocess_name\b', error_target[0]):
                    # [Application name, application installed path, process name]
                    for app in application_path_identify():
                        process_name = str(app[2])
                        script = str(error_target[0]).replace('process_name', process_name[:-4])
                        result = schell.shell_script_write(script)
                        if len(str(result)) < 10:
                            self.chat.set_sitarep("No issues to find." + self.application_q[8])
                            SayText.get_say_text().say(variables.q14+variables.q9)
                            self.loop = 7
                        else:
                            query_type = query.get_error_status(constants.APPLICATION_NAME,
                                                                constants.ERROR_DESCRIPTION,
                                                                constants.APPLICATION_VERSION,
                                                                self.error.get_application_name(),
                                                                self.error.get_error_description(),
                                                                self.error.get_application_version())
                            error_status = query_controller.execute_query(query_type)
                            self.chat.set_sitarep(error_status[0] + self.application_q[5])
                            SayText.get_say_text().say(variables.q6)
                            self.loop = 6

        # Application error action check
        elif self.loop == 6:
            if re.search(r'\bno\b', self.chat.get_lastuserreply()) or re.search(r'\bNo\b',
                                                                                self.chat.get_lastuserreply()):
                self.chat.set_sitarep(self.application_q[8])
                SayText.get_say_text().say(variables.q9)
                self.loop = 7
            elif re.search(r'\byes\b', self.chat.get_lastuserreply()) or re.search(r'\bYes\b',
                                                                                   self.chat.get_lastuserreply()):
                query_type = query.get_error_action(constants.APPLICATION_NAME, constants.ERROR_DESCRIPTION,
                                                    constants.APPLICATION_VERSION, self.error.get_application_name(),
                                                    self.error.get_error_description(),
                                                    self.error.get_application_version())
                error_action = query_controller.execute_query(query_type)
                port = self.eSubDetail.get_solution()
                if port != '' and re.search(r'\bport_number\b', error_action[0]):
                    script = str(error_action[0]).replace('port_number', port)
                else:
                    script = copy.deepcopy(error_action[0])
                    # [Application name, application installed path, process name]
                    for app in application_path_identify():
                        if app[0] == self.error.get_application_name():
                            if re.search(r'\bapplication_name\b', script):
                                str(script).replace('application_name', app[0])
                            if re.search(r'\bapplication_path\b', script):
                                str(script).replace('application_path', app[1])
                            if re.search(r'\bprocess_name\b', script):
                                str(script).replace('process_name', app[2])

                schell.shell_script_write(script)
                self.chat.set_sitarep(self.application_q[6])
                SayText.get_say_text().say(variables.q7)
                self.loop = 7
            else:
                self.chat.set_sitarep(self.application_q[0])
                SayText.get_say_text().say(variables.q1)
                self.loop = 0

        # Check User want to continue
        elif self.loop == 7:
            if re.search(r'\bno\b', self.chat.get_lastuserreply()) or re.search(r'\bNo\b',
                                                                                self.chat.get_lastuserreply()):
                exit()
            elif re.search(r'\byes\b', self.chat.get_lastuserreply()) or re.search(r'\bYes\b',
                                                                                   self.chat.get_lastuserreply()):
                self.chat.set_sitarep(self.application_q[1])
                SayText.get_say_text().say(variables.q2)
                self.loop = 1
            else:
                self.chat.set_sitarep(self.application_q[0])
                SayText.get_say_text().say(variables.q1)
                self.loop = 0

        # No such type or error
        else:
            self.chat.set_sitarep(self.application_q[0])
            SayText.get_say_text().say(variables.q1)
        add_log(log_types[2], "Chat Controller : ", self.chat.get_lastsaitareply() + self.chat.get_lastuserreply())

    def get_chat(self):
        return self.chat
