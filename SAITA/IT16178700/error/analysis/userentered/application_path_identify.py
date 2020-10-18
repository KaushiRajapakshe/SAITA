import os

from SAITA.IT16178700.error.analysis.scheduler import drives_list
from SAITA.IT16178700.model import Error


def application_path_identify(self):
    application_name = self.get_application_name()
    application_version = self.get_application_version()
    error_description = self.get_error_description()
    self.set_application_path(search_application_path(application_name))

    print(application_version, application_name, error_description, self.get_application_path())


def search_application_path(get_application_name):
    path_list = []
    for head_dir in drives_list.get_os_drives_list():
        for root, dirs, files in os.walk(head_dir):
            for d in dirs:
                if d == get_application_name:
                    path_list.append(os.path.join(root, d))

    return path_list[0]


def check_port(self):
    error_description = self.get_error_description()
    for x in range(0, 65535):
        if str(x) in error_description:
            return 'True'
