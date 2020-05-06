import winapps_change
import tkinter as tkr
from MainController import MainController


maincon = MainController()
print(maincon.get_soft_list())

root = tkr.Tk()
root.geometry("400x200")

# remove title bar from window
root.overrideredirect(True)

# create custom title bar
tit_bar = tkr.Frame(root, bg="medium blue")
root.mainloop()
