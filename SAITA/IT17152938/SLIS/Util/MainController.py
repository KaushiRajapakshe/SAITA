from Data.Log import *
from Util.SoftwareTreeCreator import SoftwareTreeCreator
from Util.Software import Software
from Util.Osdata import Osdata


class MainController:
    soft = None
    osdata = None
    install_soft_list = []

    def __init__(self):
        self.install_soft_list = []
        self.soft = Software()
        self.osdata = Osdata()

    # get complete software data set
    def get_soft_list_full(self):
        return self.get_soft_list(self.soft.get_all_software())

    # get serch software data set
    def get_soft_list_search(self, soft):
        return self.get_soft_list(self.soft.get_search_software(soft))

    def get_soft_list(self, db_soft_list):
        self.install_soft_list = []
        installed_list = self.osdata.get_installed_soft_list()
        for app in installed_list:
            for db_app in db_soft_list:
                sp_len = len(app.name.lower().split(str(db_app['name']).lower()))
                if sp_len != 1:
                    db_app['installed'] = 1
                    if not 'installed_ver' in db_app:
                        db_app['installed_ver'] = []
                    db_app['installed_ver'].append(app.version)
        self.create_installed_list(db_soft_list)
        return db_soft_list

    def get_soft_name_by_id(self, soft_id):
        soft_name = self.soft.get_soft_name_by_id(soft_id)
        for soft in soft_name:
            return soft['name']

        add_log(log_types[1], "MainController", "get_soft_name_by_id : " + str(soft_id) + " id not found")
        return ""

    def get_soft_version_by_id(self, soft_ver):
        soft_ver = self.soft.get_soft_ver_by_id(soft_ver)
        for soft in soft_ver:
            return soft['v_no']

        add_log(log_types[1], "MainController", "get_soft_version_by_id : " + str(soft_ver) + " id not found")
        return ""

    def create_installed_list(self, softlist):
        # install_soft_list = []
        for soft in softlist:
            for ver in self.soft.get_all_version(soft['id']):
                if 'installed_ver' in soft:
                    for inst in soft['installed_ver']:
                        if inst is None:
                            continue
                        inst_split = inst.split('.')
                        inst_ok = None
                        v_no_split = str(ver['v_no']).split('.')
                        v_no_ok = None
                        if len(inst_split) > 1:
                            inst_ok = inst_split[0] + "." + inst_split[1]
                        else:
                            inst_ok = inst_split[0] + ".0"

                        if len(v_no_split) > 1:
                            v_no_ok = v_no_split[0] + "." + v_no_split[1]
                        else:
                            v_no_ok = v_no_split[0] + ".0"
                        if inst_ok == v_no_ok:
                            self.install_soft_list.append(ver['id'])

    def get_insalled_list(self):
        return self.install_soft_list

    def create_setup(self, install_list):
        self.get_soft_list_full()
        per_install_softwares = list(dict.fromkeys(self.get_insalled_list()))
        soft_tree = SoftwareTreeCreator()
        tree = soft_tree.create_tree(install_list)
        temp_tree = tree
        for node_array in tree:
            for node in node_array:
                try:
                    per_install_softwares.index(node.get_ver_id())
                    node.set_do_install(False)
                except:
                    node.set_do_install(True)
        return tree
