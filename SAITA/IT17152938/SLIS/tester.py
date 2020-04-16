import winapps_change
from MainController import MainController


maincon = MainController()
maincon.get_soft_list()

# for app in winapps_change.list_installed():
#     print(app.name+"\t"+app.install_date.__str__())
#
# print('\n')
#
# # for app in winapps_change.search_installed('Asus Sonic Radar 3'):
# #     print(app)
#
# [ap] = winapps_change.search_installed('jetAudio Basic')
# print(ap)

