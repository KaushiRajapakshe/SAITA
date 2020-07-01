# from Util.MainController import MainController
#
# install_list=[{'soft_id': 17, 'ver_id': 86, 'select_text_point': 0},{'soft_id': 27, 'ver_id': 115, 'select_text_point': 1},{'soft_id': 13, 'ver_id': 68, 'select_text_point': 1}, {'soft_id': 19, 'ver_id': 94, 'select_text_point': 1}]
# m_con = MainController()
# m_con.create_setup(install_list)

from Util.Osdata import Osdata

osdata=Osdata()
print(osdata.get_restorepoint("sachin tes"))