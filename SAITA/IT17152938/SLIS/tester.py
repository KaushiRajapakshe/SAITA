# from Util.MainController import MainController
#
# install_list=[{'soft_id': 17, 'ver_id': 84, 'select_text_point': 0},{'soft_id': 27, 'ver_id': 115, 'select_text_point': 1},{'soft_id': 13, 'ver_id': 68, 'select_text_point': 1}, {'soft_id': 19, 'ver_id': 94, 'select_text_point': 1}]
# # install_list=[{'soft_id': 17, 'ver_id': 5, 'select_text_point': 0},{'soft_id': 27, 'ver_id': 115, 'select_text_point': 1},{'soft_id': 13, 'ver_id': 68, 'select_text_point': 1}, {'soft_id': 19, 'ver_id': 94, 'select_text_point': 1}]
# # install_list = [{'soft_id': 4, 'ver_id': 31, 'select_text_point': 4}, {'soft_id': 2, 'ver_id': 20, 'select_text_point': 3}, {'soft_id': 13, 'ver_id': 60, 'select_text_point': 1}, {'soft_id': 7, 'ver_id': 52, 'select_text_point': 1}, {'soft_id': 19, 'ver_id': 94, 'select_text_point': 1}, {'soft_id': 17, 'ver_id': 87, 'select_text_point': 3}, {'soft_id': 22, 'ver_id': 99, 'select_text_point': 1}, {'soft_id': 15, 'ver_id': 85, 'select_text_point': 2}]
# # install_list = [{'soft_id': 2, 'ver_id': 22, 'select_text_point': 1}, {'soft_id': 4, 'ver_id': 39, 'select_text_point': 3}, {'soft_id': 5, 'ver_id': 43, 'select_text_point': 0}, {'soft_id': 6, 'ver_id': 47, 'select_text_point': 2}, {'soft_id': 7, 'ver_id': 51, 'select_text_point': 2}, {'soft_id': 12, 'ver_id': 65, 'select_text_point': 1}, {'soft_id': 13, 'ver_id': 67, 'select_text_point': 2}, {'soft_id': 14, 'ver_id': 73, 'select_text_point': 2}, {'soft_id': 15, 'ver_id': 79, 'select_text_point': 2}, {'soft_id': 16, 'ver_id': 82, 'select_text_point': 0}, {'soft_id': 17, 'ver_id': 87, 'select_text_point': 3}, {'soft_id': 19, 'ver_id': 95, 'select_text_point': 0}, {'soft_id': 20, 'ver_id': 97, 'select_text_point': 5}, {'soft_id': 22, 'ver_id': 105, 'select_text_point': 1}, {'soft_id': 23, 'ver_id': 107, 'select_text_point': 0}, {'soft_id': 24, 'ver_id': 108, 'select_text_point': 0}, {'soft_id': 25, 'ver_id': 109, 'select_text_point': 0}, {'soft_id': 26, 'ver_id': 110, 'select_text_point': 2}, {'soft_id': 27, 'ver_id': 114, 'select_text_point': 1}, {'soft_id': 1, 'ver_id': 1, 'select_text_point': 7}]
# # m_con = MainController()
# # install_list = [{'soft_id': 5, 'ver_id': 43, 'select_text_point': 0}, {'soft_id': 6, 'ver_id': 47, 'select_text_point': 2}, {'soft_id': 7, 'ver_id': 52, 'select_text_point': 1}, {'soft_id': 10, 'ver_id': 60, 'select_text_point': 3}, {'soft_id': 23, 'ver_id': 107, 'select_text_point': 0}, {'soft_id': 22, 'ver_id': 105, 'select_text_point': 1}, {'soft_id': 24, 'ver_id': 108, 'select_text_point': 0}, {'soft_id': 26, 'ver_id': 112, 'select_text_point': 0}]
# m_con = MainController()
# m_con.create_setup(install_list)

# from Util.Osdata import Osdata
#
# osdata=Osdata()
#
# print(osdata.search_environment_variable("PATH", "JAVA"))

# from tkinter import *
# import time
# import os
# root = Tk()
#
# frames = frame2 = PhotoImage(file='Icon/loader.gif', format="gif -index 2")
#
# Label(image=frames).pack()
#
# root.mainloop()

# Author: Miguel Martinez Lopez


from tkinter import PhotoImage

# from win32api import GetMonitorInfo, MonitorFromPoint
#
# from Gui.GuiPopupWindow import GuiPopupWindow
#
# if __name__ == "__main__":
#     from tkinter import Tk, Label
#
#     root = Tk()
#     monitor_fo = GetMonitorInfo(MonitorFromPoint((0, 0)))
#     work_area = monitor_fo.get("Work")
#     acc_ra = work_area[3] / work_area[2]
#
#     massage = GuiPopupWindow(root,
#                              acc_ra,
#                              work_area,
#                              "Wait",
#                              ["Creating Windows Restore Point Please Wait"],
#                              [0.4615, 0.5, 0.2702, 5],
#                              type="wait",
#                              close=False,
#                              )
#
#     root.mainloop()

from tkinter import filedialog
from tkinter import *

def browse_button():
    filename = filedialog.askdirectory(master=None)
    print(filename)
    return filename


root = Tk()
v = StringVar()
button2 = Button(text="Browse", command=browse_button).grid(row=0, column=3)

mainloop()