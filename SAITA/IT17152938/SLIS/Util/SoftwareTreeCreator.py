from Util.SoftwareNode import SoftwareNode
from Util.Osdata import Osdata


class SoftwareTree:
    tree = []

    def create_tree(self, soft_list):
        osdata = Osdata()
        osbit = osdata.get_os_architecture_type()
        for soft in soft_list:
            ver = [soft['ver_id']]
            self.__create_node(ver, osbit)

        self.__clean_duplicate()
        return self.tree

    def __create_node(self, ver_list, osbit):
        for ver in ver_list:
            soft_node = SoftwareNode(ver, osbit)
            if not soft_node.get_dependency_len() == 0:
                self.__create_node(soft_node.get_dependency(), osbit)
            self.tree.append(soft_node)

    def __clean_duplicate(self):
        temp_tree = {}
        temp_id = []
        for node in self.tree:
            try:
                temp_id.index(node.get_ver_id())
            except:
                temp_id.append(node.get_ver_id())
                temp_tree[node.get_ver_id()] = node

        self.tree = temp_tree
