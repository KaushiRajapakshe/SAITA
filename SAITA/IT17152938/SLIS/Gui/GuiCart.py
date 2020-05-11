from tkinter import *
from tkinter.ttk import Combobox
from urllib.error import *
from tkinter.messagebox import *
from win32api import GetMonitorInfo, MonitorFromPoint
from PIL import ImageTk, Image
from Data.Veriables import *
from Data.Log import *
from Util.MainController import MainController
import math
from urllib.request import urlopen
from Util.Software import Software

# get monitor working aria size
monitor_fo = GetMonitorInfo(MonitorFromPoint((0, 0)))
add_log(log_types[2], "GuiCanvas.py", "Monitor info : " + str(monitor_fo))
work_area = monitor_fo.get("Work")
acc_ra = work_area[3] / work_area[2]
add_log(log_types[2], "GuiCanvas.py", "set acc_ra: " + str(acc_ra))

# install list = []
install_list = []


def open_cart(event):
    print(event)
    invoerscherm = Toplevel()
    invoerscherm.geometry("800x400+0+0")
    invoerscherm.title("Nieuwe Zending Invoeren")
