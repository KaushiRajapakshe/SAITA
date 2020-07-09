from tkinter import *

from PIL import ImageTk, Image

from Data.Veriables import *

from Data.Log import *


class GuiPopupWindow:

    def __init__(self, master, acc_ra, work_area, massage_tital):
        self.img = Image.open(logo)
        new_img_w, new_img_h = self.img.size
        new_img_w *= acc_ra * logo_div
        new_img_h *= acc_ra * logo_div
        self.img = self.img.resize((round(new_img_w), round(new_img_h)))
        self.top = Toplevel(master)
        self.top.overrideredirect(True)
        self.top.iconbitmap(logo)
        # set new geometry
        top_size = "{}x{}+{}+{}".format(round(work_area[2] / 4), round(work_area[3] - new_img_w - 6-500),
                                        round(work_area[2]*3 / 8), (round(new_img_w) + 5)*6)
        # make a frame for the title bar
        self.top.geometry(top_size)
        self.top_title_bar = Frame(self.top,
                              bg=title_bar_bg,
                              relief='raised',
                              bd=0
                              )
        # put a close button on the title bar
        self.top_close_button = Button(self.top_title_bar,
                                   text='x',
                                   command=self.top.destroy,
                                   bg=title_bar_bg,
                                   padx=5,
                                   pady=2,
                                   activebackground=close_but_acc_bg,
                                   bd=0,
                                   font="bold",
                                   fg=title_bar_but_txt_color,
                                   activeforeground=title_bar_but_txt_color,
                                   highlightthickness=0
                                   )

        # window title
        self.massage_title_name = Label(self.top_title_bar, text=massage_tital, bg=title_bar_bg, fg=title_bar_txt_color,
                                   font="bold")
        # titalbar img
        self.top_title_img = ImageTk.PhotoImage(self.img)
        self.top_title_img_set = Label(self.top_title_bar, image=self.top_title_img, bg=title_bar_bg, )
        self.top_window = Frame(self.top, bg=title_bar_bg, )
        self.top_in_window = Frame(self.top_window, bg=cart_full_window_color, highlightthickness=0)
        self.l = Label(self.top_in_window, text="Hello World")
        self.l.pack()
        self.e = Entry(self.top_in_window)
        self.e.pack()
        self.b = Button(self.top_in_window, text='Ok', command=self.cleanup)
        self.b.pack()

        self.top_title_bar.pack(fill=X)
        self.top_title_img_set.pack(side=LEFT)
        self.massage_title_name.pack(side=LEFT)
        self.top_close_button.pack(side=RIGHT)
        self.top_window.pack(expand=1, fill=BOTH)
        self.top_in_window.pack(expand=1, fill=BOTH, padx=2, pady=2)
        self.value = None
        self.top_close_button.bind('<Enter>', self.cart_close_btn_on_hovering)
        self.top_close_button.bind('<Leave>', self.cart_close_btn_return_to_normal_state)

    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()

    def cart_close_btn_on_hovering(self, event):
        add_log(log_types[2], "GuiPopupWindow.py", "close_btn_on_hovering : " + str(event))
        self.top_close_button['bg'] = close_but_acc_bg

    def cart_close_btn_return_to_normal_state(self, event):
        add_log(log_types[2], "GuiPopupWindow.py", "return_to_normal_state : " + str(event))
        self.top_close_button['bg'] = title_bar_bg
