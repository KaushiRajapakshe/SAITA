from tkinter import *
from Data.Veriables import logo, error_str_size


class GuiError:
    error_root = None

    def __init__(self, err):
        self.error = err

    # show error dialog
    def show(self):
        self.error_root = Tk()
        self.error_root.iconbitmap(logo)
        self.error_root.title("Error")
        Label(self.error_root, text=self.create_error(), font="bold").pack(expand=True, fill='x')
        close_but = Button(self.error_root,
                           text='Close',
                           font="bold",
                           )
        close_but.pack(expand=True, fill='x')
        close_but.bind('<Button-1>', GuiError.close_event)
        self.error_root.mainloop()

    @staticmethod
    def close_event(event):
        exit()

    def create_error(self):
        str_err = ""
        for i in range(0, len(self.error), error_str_size):
            cut_str = i + error_str_size
            p = self.error[i:cut_str] + "\n"
            str_err += p
        return str_err
