from tkinter import *

from PIL import ImageTk, Image

from Data.Variables import *

from Data.Log import *
from GUI.GuiGifShow import AnimatedGIF
from tkinter import ttk


class GuiPopupWindow:
    massage = None
    massage2 = None
    checkbox_array = []
    checkbox_array_val = []
    data = None
    acc = None
    progress_num = None
    progress = None

    def __init__(self, master, acc_ra, work_area, massage_tital, data_in, poin_val, close=True, type="soft",
                 btn_txt=""):
        self.checkbox_array = []
        self.checkbox_array_val = []
        self.data = data_in
        self.img = Image.open(logo)
        self.acc = acc_ra
        new_img_w, new_img_h = self.img.size
        new_img_w *= acc_ra * logo_div
        new_img_h *= acc_ra * logo_div
        self.img = self.img.resize((round(new_img_w), round(new_img_h)))
        self.top = Toplevel(master)
        self.top.overrideredirect(True)
        self.top.iconbitmap(logo)
        # set new geometry
        top_size = "{}x{}+{}+{}".format(round(work_area[2] * poin_val[0]),
                                        round((work_area[3] - new_img_w - 6) * poin_val[1]),
                                        round(work_area[2] * poin_val[2]), (round(new_img_w) + 5) * poin_val[3])
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
        self.top_in_window = Frame(self.top_window, bg=message_body_color)
        self.top_in_window_body = None
        self.top_in_window_footer = Frame(self.top_in_window, bg=message_body_color)

        if type == "soft":
            self.dependencies_select_body()
        elif type == "wait":
            self.creat_wait_body()
        elif type == "download":
            self.creat_download_body()
        elif type == "show":
            self.creat_show_body()
        if close:
            self.but = Button(self.top_in_window_footer,
                              text=btn_txt,
                              bg=main_search_but_bg,
                              command=self.cleanup,
                              activebackground=main_search_but_acc,
                              bd=2,
                              font="bold",
                              fg=main_search_but_txt_color,
                              activeforeground=main_search_but_txt_color,
                              highlightthickness=0,
                              )

            self.but.pack(

                padx=pad_val * acc_ra / 2,
                pady=pad_val * acc_ra / 2,
                ipadx=main_search_but_ipadx * acc_ra / 2,
                ipady=main_search_but_ipady * acc_ra / 2,
            )

            self.but.bind("<Enter>", self.but_hover_in)
            self.but.bind("<Leave>", self.but_hover_out)

        self.top_in_window_body.pack(expand=1, fill=BOTH)
        self.top_in_window_footer.pack(fill=X)

        self.top_title_bar.pack(fill=X)
        self.top_title_img_set.pack(side=LEFT)
        self.massage_title_name.pack(side=LEFT)
        if close:
            self.top_close_button.pack(side=RIGHT)
        self.top_window.pack(expand=1, fill=BOTH)
        self.top_in_window.pack(expand=1, fill=BOTH, padx=2, pady=2)
        self.value = None
        self.top_close_button.bind('<Enter>', self.cart_close_btn_on_hovering)
        self.top_close_button.bind('<Leave>', self.cart_close_btn_return_to_normal_state)

    def cleanup(self):
        self.value = self.checkbox_array_val
        self.top.destroy()

    def cart_close_btn_on_hovering(self, event):
        add_log(log_types[2], "GuiPopupWindow.py", "close_btn_on_hovering : " + str(event))
        self.top_close_button['bg'] = close_but_acc_bg

    def cart_close_btn_return_to_normal_state(self, event):
        add_log(log_types[2], "GuiPopupWindow.py", "return_to_normal_state : " + str(event))
        self.top_close_button['bg'] = title_bar_bg

    def dependencies_select_body(self):
        self.top_in_window_body = Frame(self.top_in_window, bg=message_body_color, highlightthickness=0)
        # body start
        fontsize = round(self.acc / 1.5)
        masage_txt = "System identified different version of " + self.data[0].get_soft_name() + " in dependencies"
        self.massage = Label(self.top_in_window_body, text=masage_txt, bg=message_body_color, font="bold")
        self.massage.pack(fill=X)
        masage_txt2 = "Please select one or more to continue"
        self.massage2 = Label(self.top_in_window_body, text=masage_txt2, bg=message_body_color)
        self.massage2.pack(fill=X)
        self.massage.config(font=("arial", fontsize))
        self.massage2.config(font=("arial", fontsize))
        self.checkbox_array = []
        k = 0
        # main_in = Frame(self.top_in_window, bg=message_body_color, highlightthickness=0)
        for node in self.data:
            chshow = Frame(self.top_in_window_body, bg=message_body_color)
            chshow.pack(fill=X, padx=10, pady=10)
            self.checkbox_array_val.append(IntVar())
            txt = node.get_soft_name() + " version: " + node.get_ver()
            if not node.get_do_install():
                txt += " (installed)"
            self.checkbox_array_val[k].set(1)
            self.checkbox_array.append(Checkbutton(chshow,
                                                   text=txt,
                                                   variable=self.checkbox_array_val[k],
                                                   bg=message_body_color
                                                   )
                                       )
            self.checkbox_array[k].config(font=("arial", fontsize))
            self.checkbox_array[k].pack(fill=X, side=LEFT)
            if not node.get_do_install():
                self.checkbox_array[k].config(state='disable')
            k += 1

        # body end

    def but_hover_in(self, event):
        self.but['bg'] = main_search_but_hover

    def but_hover_out(self, event):
        self.but['bg'] = main_search_but_bg

    def creat_wait_body(self):
        self.top_in_window_body = Frame(self.top_in_window, bg=message_body_color, highlightthickness=0)
        fontsize = round(self.acc / 1.5)
        self.massage = Label(self.top_in_window_body, text=self.data[0], bg=message_body_color, font="bold")
        self.massage.config(font=("arial", fontsize))
        self.massage.pack(fill=X)
        animate = AnimatedGIF(self.top_in_window_body, loader_icon)
        animate.pack(fill=BOTH, pady=10)

    def creat_download_body(self):
        self.top_in_window_body = Frame(self.top_in_window, bg=message_body_color, highlightthickness=0)
        fontsize = round(self.acc / 1.5)
        self.massage = Label(self.top_in_window_body, text=self.data[0], bg=message_body_color, font="bold")
        self.massage.config(font=("arial", fontsize))
        self.massage.pack(fill=X, pady=10)
        self.progress = ttk.Progressbar(self.top_in_window_body, orient="horizontal", mode="determinate")
        self.progress.pack(fill=X,padx=10,pady=10)
        self.progress_num = Label(self.top_in_window_body, text=self.data[0], bg=message_body_color, font="bold")
        self.progress_num.config(font=("arial", fontsize))
        self.progress_num.pack(fill=X, pady=10)

    def creat_show_body(self):
        self.top_in_window_body = Frame(self.top_in_window, bg=message_body_color, highlightthickness=0)
        fontsize = round(self.acc / 1.5)
        self.massage = Label(self.top_in_window_body, text=self.data[0], bg=message_body_color, font="bold")
        self.massage.config(font=("arial", fontsize))
        self.massage.pack(fill=X, pady=10)