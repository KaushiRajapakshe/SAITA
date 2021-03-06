from Util.Software import Software
from Util.Osdata import Osdata


class SoftwareNode:
    ver_id = None
    osbit = None
    setup_link = None
    setup_type = None
    __dependency = []
    soft_id = None
    ver = None
    soft_name = None
    do_install = None
    installed_path = None
    file_path = None
    exe_param = None

    def __init__(self, ver_id, osbit):
        self.__dependency = []
        soft = Software()
        self.ver_id = ver_id
        self.osbit = osbit
        self.__set_setup_link(soft)
        self.__set_dependency(soft)
        self.do_install = None
        self.file_path = None
        self.installed_path = None

    def __set_setup_link(self, soft):
        for softver in soft.get_soft_ver_data_by_id(self.ver_id):
            if self.osbit == "64bit":
                self.setup_link = softver['x64_path']
            else:
                self.setup_link = softver['x86_path']

            self.setup_type = softver['execute']
            self.soft_id = softver['soft_id']
            self.ver = softver['v_no']
            self.soft_name = soft.get_soft_name_by_id(self.soft_id)[0]['name']
            self.exe_param = softver['exe_param']

    def __set_dependency(self, soft):
        for depan in soft.get_dependency(self.ver_id):
            self.__dependency.append(depan['depend_soft_id'])

    def print_node(self):
        print(self.ver_id, self.osbit, self.setup_link, self.setup_type, self.__dependency, self.soft_id, self.ver,
              self.soft_name, self.do_install)

    def get_dependency_len(self):
        return len(self.__dependency)

    def get_ver_id(self):
        return self.ver_id

    def get_osbit(self):
        return self.osbit

    def get_setup_link(self):
        return self.setup_link

    def get_setup_type(self):
        return self.setup_type

    def get_dependency(self):
        return self.__dependency

    def get_soft_id(self):
        return self.soft_id

    def get_ver(self):
        return self.ver

    def get_soft_name(self):
        return self.soft_name

    def set_do_install(self, status):
        self.do_install = status

    def get_do_install(self):
        return self.do_install

    def get_installed_path(self):
        return self.installed_path

    def set_installed_path(self, path):
        self.installed_path = path

    def get_file_path(self):
        return self.file_path

    def set_file_path(self, path):
        self.file_path = path

    def get_exe_param(self):
        return self.exe_param
