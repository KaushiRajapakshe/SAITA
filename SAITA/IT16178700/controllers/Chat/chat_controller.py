from SAITA.IT16178700.constant import constants
from SAITA.IT16178700.data import variables
from SAITA.IT16178700.error.analysis.scheduler import scanner
from SAITA.IT16178700.error.analysis.userentered import application_path_identify
from SAITA.IT16178700.model.Error import Error
from SAITA.IT16178700.model.Chat import TestChat
from SAITA.IT16178700.ontology import query
from SAITA.IT16178700.controllers.ontology import query_controller
from SAITA.IT16178700.controllers.shell_script import schell_script_controller as schell
import re


def clean_version_data(ap_version):
    v1 = ap_version.replace('___', ' ')
    v2 = v1.replace('__', '-')
    v3 = v2.replace('_', '.')
    return v3


class ChatController:
    next_q = []
    chat = None
    application_q = ['Sorry.. We are out of service for entered query you. Try out for other.',
                     'Please enter your application name.?',
                     'Please enter version of your application.?',
                     'Please enter your error discretion.?',
                     'Please wait until error analyzing.',
                     'Insight-dashboard.jar service run on 8080 port.',
                     'Do you need to continue.?',
                     'Your problem is solved.',
                     'System has no issue to find.']

    global error_list, error_dist
    error_list = []
    error_dict = {}
    scanner_v = ''

    def __init__(self):
        self.loop = 0
        self.chat = TestChat()
        self.error = Error()

    def chat_question_sequence(self):

        # User Entered
        if re.search(r'\bno\b', self.chat.get_lastuserreply()) or re.search(r'\bNo\b', self.chat.get_lastuserreply()):
            self.chat.set_sitarep(self.application_q[1])
            self.loop = 1
        # Scheduler
        elif self.loop == 10:
            error_dict = scanner.scanner_details()
            error_list.append(error_dict)
            self.loop = 11
            if self.loop == 11:
                chat_list = ''
                if len(error_list) == 0:
                    self.chat.set_sitarep("No issues to find.")
                else:
                    for e in range(len(error_list)):
                        for er in error_list[e]:
                            if not chat_list == '':
                                chat_list += '\n\t' + str(error_list[e][er])
                            else:
                                chat_list = '\t' + str(error_list[e][er])
                                self.loop = 12

                self.chat.set_sitarep(chat_list)

        elif self.loop == 12:
            if type(int(self.chat.get_lastuserreply())) == int:
                schell.shell_script_write(variables.script1)
                self.chat.set_sitarep(self.application_q[7])
        elif re.search(r'\byes\b', self.chat.get_lastuserreply()) or \
                re.search(r'\bYes\b', self.chat.get_lastuserreply()) and self.loop == 0:
            self.chat.set_sitarep("Scheduler running...")
            self.loop = 10
            scanner_v = 'started'
            print(scanner_v)

        # Application name check
        elif self.loop == 1:
            query_type = query.get_application_type()
            application_name = query_controller.execute_query(query_type)
            for ap_name in application_name:
                if re.search(r'\b' + ap_name + '\\b', self.chat.get_lastuserreply(), re.IGNORECASE):
                    self.loop = 2
                    # Set Error application name
                    self.error.set_application_name(ap_name)
            if self.loop == 2:
                self.chat.set_sitarep(self.application_q[2])
            else:
                self.chat.set_sitarep(self.application_q[0])

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
                    self.error.set_application_version(clean_version_data(ap_version))
            if self.loop == 3:
                self.chat.set_sitarep(self.application_q[3])
            else:
                self.chat.set_sitarep(self.application_q[0])

        # Application description check
        elif self.loop == 3:
            query_type = query.check_error_description(constants.APPLICATION_VERSION, self.chat.get_check_userreply(),
                                                       constants.ERROR_DESCRIPTION)
            error_description = query_controller.execute_query(query_type)
            for error in error_description:
                if re.search(r'\b' + error + '\\b', self.chat.get_lastuserreply(),
                             re.IGNORECASE):
                    self.loop = 4
                    # Set Error error description
                    self.error.set_error_description(error)
                if self.loop == 4:
                    self.chat.set_sitarep(self.application_q[4])
                    application_path_identify.application_path_identify(self.error)
                    if application_path_identify.check_port(self.error) == 'False':
                        self.loop = 5
                        # if self.loop == 5:
                        #     self.chat.set_sitarep(self.application_q[8])

            query.get_error_action(constants.APPLICATION_NAME, constants.ERROR_DESCRIPTION,
                                   constants.APPLICATION_VERSION, self.error.get_application_name(),
                                   self.error.set_error_description(), self.error.get_application_version())

        # # Application error analysing
        # elif self.loop == 4:
        #     application_path_identify.application_path_identify(self.error)
        # Wait for scan done
        # elif self.loop == 10:
        #     self.chat.set_sitarep("Please wait until preventing scanner done.")

        # No such type or error
        else:
            self.chat.set_sitarep(self.application_q[0])

    def get_chat(self):
        return self.chat
