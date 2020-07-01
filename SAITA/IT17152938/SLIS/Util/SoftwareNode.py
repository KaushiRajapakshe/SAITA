from Util.Software import Software
from Util.Osdata import Osdata


class SoftwareNode:
    ver_id = None
    osbit = None
    setup_link = None
    setup_type = None
    __dependency = []

    def __init__(self, ver_id, osbit):
        self.__dependency = []
        soft = Software()
        self.ver_id = ver_id
        self.osbit = osbit
        self.__set_setup_link(soft)
        self.__set_dependency(soft)

    def __set_setup_link(self, soft):
        for softver in soft.get_soft_ver_data_by_id(self.ver_id):
            if self.osbit == "64bit":
                self.setup_link = softver['x64_path']
            else:
                self.setup_link = softver['x86_path']

            self.setup_type = softver['execute']

    def __set_dependency(self, soft):
        for depan in soft.get_dependency(self.ver_id):
            self.__dependency.append(depan['depend_soft_id'])

    def print_node(self):
        print(self.ver_id, self.osbit, self.setup_link, self.setup_type, self.__dependency)

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
