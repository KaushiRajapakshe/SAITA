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
        self.__do_category()
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

    def __do_category(self):
        temp_tree_category = []
        temp_tree = []
        for main_node in self.tree:
            try:
                temp_tree.index(main_node)
                continue
            except:
                temp_tree.append(main_node)
            temp = [main_node]
            for node in self.tree:
                try:
                    temp_tree.index(node)
                    continue
                except:
                    if main_node.get_soft_id() == node.get_soft_id():
                        temp_tree.append(node)
                        temp.append(node)
            temp_tree_category.append(temp)
        self.tree = temp_tree_category
