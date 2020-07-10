from Gui.GuiCartBody import *

# title bar img
img = Image.open(logo)
new_img_w, new_img_h = img.size
new_img_w *= acc_ra * logo_div
new_img_h *= acc_ra * logo_div
img = img.resize((round(new_img_w), round(new_img_h)))
cart_title_img = None

cart_root = None
cart_close_button = None
root = None


def cart_close_btn_on_hovering(event):
    global cart_close_button
    add_log(log_types[2], "GuiCart.py.py", "close_btn_on_hovering : " + str(event))
    cart_close_button['bg'] = close_but_acc_bg


def cart_close_btn_return_to_normal_state(event):
    global cart_close_button
    add_log(log_types[2], "GuiCart.py", "return_to_normal_state : " + str(event))
    cart_close_button['bg'] = title_bar_bg


def open_cart_window(root_win):
    global cart_root, img, new_img_w, cart_title_img, cart_close_button, root
    if len(install_list) < 1:
        showinfo("Info", "No Software for Installation")
    else:
        root = root_win
        cart_root = Toplevel(root_win)
        cart_root.overrideredirect(True)
        cart_root.iconbitmap(logo)
        cart_root_screen_size = "{}x{}+{}+{}".format(round(work_area[2] / 2), round(work_area[3] - new_img_w - 6),
                                                     round(work_area[2] / 4), round(new_img_w) + 5)

        # set new geometry
        cart_root.geometry(cart_root_screen_size)

        # make a frame for the title bar
        cart_title_bar = Frame(cart_root,
                               bg=title_bar_bg,
                               relief='raised',
                               bd=0
                               )

        # put a close button on the title bar
        cart_close_button = Button(cart_title_bar,
                                   text='x',
                                   command=cart_root_close,
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
        cart_title_name = Label(cart_title_bar, text=cart_title, bg=title_bar_bg, fg=title_bar_txt_color, font="bold")

        # titalbar img
        cart_title_img = ImageTk.PhotoImage(img)
        cart_title_img_set = Label(cart_title_bar, image=cart_title_img, bg=title_bar_bg, )

        cart_window = Frame(cart_root, bg=title_bar_bg, )
        cart_in_window = create_cart_window(cart_window, cart_root,root)

        cart_title_bar.pack(fill=X)
        cart_title_img_set.pack(side=LEFT)
        cart_title_name.pack(side=LEFT)
        cart_close_button.pack(side=RIGHT)
        cart_window.pack(expand=1, fill=BOTH)
        cart_in_window.pack(expand=1, fill=BOTH, padx=2, pady=2)

        cart_close_button.bind('<Enter>', cart_close_btn_on_hovering)
        cart_close_button.bind('<Leave>', cart_close_btn_return_to_normal_state)


def cart_root_close():
    global cart_root, root
    cart_root.destroy()
    root.deiconify()