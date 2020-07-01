from Util.SoftwareNode import SoftwareNode
from Util.Osdata import Osdata


class SoftwareTreeCreator:
    tree = []
    tree_key = []

    def create_tree(self, soft_list):
        osdata = Osdata()
        osbit = osdata.get_os_architecture_type()
        for soft in soft_list:
            ver = [soft['ver_id']]
            self.__create_node(ver, osbit)
        return self.tree

    def __create_node(self, ver_list, osbit):
        for ver in ver_list:
            try:
                self.tree_key.index(ver)
            except:
                soft_node = SoftwareNode(ver, osbit)
                if not soft_node.get_dependency_len() == 0:
                    self.__create_node(soft_node.get_dependency(), osbit)
                self.tree_key.append(ver)
                self.tree.append(soft_node)

