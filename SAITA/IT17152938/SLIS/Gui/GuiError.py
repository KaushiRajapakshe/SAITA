from tkinter import *
from Data.Veriables import logo


class GuiError:

    def __init__(self, error):
        root = Tk()
        root.iconbitmap(logo)
        root.title("Error")
        Label(root, text=error,font="bold").pack()
        root.mainloop()