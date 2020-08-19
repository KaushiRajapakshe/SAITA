# from tkinter import *
from Data.Veriables import logo, error_str_size
import tkinter as tk
from tkinter import messagebox


class GuiError:
    error_root = None

    def __init__(self, err):
        self.error = err

    # show error dialog
    def show(self):
        MsgBox = tk.messagebox.showerror('Error : Exit App', self.create_error())
        if MsgBox == 'ok':
            GuiError.close_event()

    def show2(self):
        MsgBox = tk.messagebox.showerror('Error : ', self.create_error())
        

    @staticmethod
    def close_event():
        exit()

    def create_error(self):
        str_err = ""
        for i in range(0, len(self.error), error_str_size):
            cut_str = i + error_str_size
            p = self.error[i:cut_str] + "\n"
            str_err += p
        return str_err
