from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox, Treeview
from urllib.error import *
from tkinter.messagebox import *
from win32api import GetMonitorInfo, MonitorFromPoint
from PIL import ImageTk, Image
from Data.Veriables import *
from Data.Log import *
from Gui.GuiPopupWindow import GuiPopupWindow
from Util.MainController import MainController
import math
from urllib.request import urlopen
from Util.Software import Software

# get monitor working aria size
monitor_fo = GetMonitorInfo(MonitorFromPoint((0, 0)))
add_log(log_types[2], "GuiCart.py", "Monitor info : " + str(monitor_fo))
work_area = monitor_fo.get("Work")
acc_ra = work_area[3] / work_area[2]
add_log(log_types[2], "GuiCart.py", "set acc_ra: " + str(acc_ra))

# install list = []
install_list = []
# install_list = [{'soft_id': 17, 'ver_id': 84, 'select_text_point': 0},
#                 {'soft_id': 27, 'ver_id': 115, 'select_text_point': 1},
#                 {'soft_id': 13, 'ver_id': 68, 'select_text_point': 1},
#                 {'soft_id': 19, 'ver_id': 94, 'select_text_point': 1}]
# install_list = [{'soft_id': 6, 'ver_id': 47, 'select_text_point': 0},
#                 {'soft_id': 16, 'ver_id': 82, 'select_text_point': 0},
#                 {'soft_id': 27, 'ver_id': 115, 'select_text_point': 1},]
# install_list = [{'soft_id': 6, 'ver_id': 47, 'select_text_point': 0},
#                 {'soft_id': 16, 'ver_id': 82, 'select_text_point': 0},]
# install_list = [{'soft_id': 2, 'ver_id': 12, 'select_text_point': 0},
#                 {'soft_id': 16, 'ver_id': 82, 'select_text_point': 0},]

# install button
install_but = None
style = None
root_main = None
cart_root = None
ch = True
cart_body_frame = None
soft_tree = None


def create_cart_window(cart_root_body, root, root_main_in):
    global cart_root, root_main
    cart_root = root
    root_main = root_main_in
    full_cart_frame = Frame(cart_root_body, bg=cart_full_window_color, highlightthickness=0)
    header_cart_frame = create_cart_header_window(full_cart_frame)
    body_cart_frame = create_cart_body_window(full_cart_frame)
    footer_cart_frame = create_cart_footer_window(full_cart_frame)
    header_cart_frame.pack(fill=X)
    body_cart_frame.pack(expand=1, fill=BOTH)
    footer_cart_frame.pack(fill=X)
    return full_cart_frame


def create_cart_header_window(cart_frame):
    return Frame(cart_frame, bg=cart_header_color)


def create_cart_body_window(cart_frame):
    global install_list, style, cart_body_frame
    cart_body_frame = Frame(cart_frame, bg=cart_body_color)
    body_table_col_name = ('Name', 'Version')
    cart_table = Treeview(cart_body_frame, columns=body_table_col_name, show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=(None, 20))
    style.configure("Treeview", font=(None, 15), rowheight=40)
    style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))
    for col in body_table_col_name:
        cart_table.heading(col, text=col)

    maincon = MainController()

    ch_int = 0
    for soft in install_list:
        if ch_int % 2 == 0:
            cart_table.insert("", "end", soft['soft_id'], text=str(soft['soft_id']),
                              values=(maincon.get_soft_name_by_id(soft['soft_id']),
                                      maincon.get_soft_version_by_id(soft['ver_id'])))
            cart_table.item(soft['soft_id'], tags='evenrow')
        else:
            cart_table.insert("", "end", soft['soft_id'], text=str(soft['soft_id']),
                              values=(maincon.get_soft_name_by_id(soft['soft_id']),
                                      maincon.get_soft_version_by_id(soft['ver_id'])))
            cart_table.item(soft['soft_id'], tags='oddrow')

        ch_int += 1

    cart_table.tag_configure("evenrow", background=cart_even_row_bg, foreground='black')
    cart_table.tag_configure("oddrow", background=cart_odd_row_bg, foreground='black')
    cart_table.pack(fill=BOTH, expand=1)
    return cart_body_frame


def fixed_map(option):
    global style
    # Fix for setting text colour for Tkinter 8.6.9
    # From: https://core.tcl.tk/tk/info/509cafafae
    #
    # Returns the style map for 'option' with any styles starting with
    # ('!disabled', '!selected', ...) filtered out.

    # style.map() returns an empty list for missing options, so this
    # should be future-safe.
    return [elm for elm in style.map('Treeview', query_opt=option) if
            elm[:2] != ('!disabled', '!selected')]


def install_but_button_hover_in(event):
    global install_but
    install_but['bg'] = main_search_but_hover


def install_but_button_hover_out(event):
    global install_but
    install_but['bg'] = main_search_but_bg


def create_cart_footer_window(cart_frame):
    global install_but
    cart_footer_form = Frame(cart_frame, bg=cart_footer_color)
    install_but = Button(cart_footer_form,
                         text=install_button_text,
                         bg=main_search_but_bg,
                         activebackground=main_search_but_acc,
                         bd=2,
                         font="bold",
                         fg=main_search_but_txt_color,
                         activeforeground=main_search_but_txt_color,
                         highlightthickness=0,
                         )

    install_but.pack(

        padx=pad_val * acc_ra,
        pady=pad_val * acc_ra,
        ipadx=main_search_but_ipadx * acc_ra,
        ipady=main_search_but_ipady * acc_ra,
    )
    # test_lable = Label(cart_footer_form,text="no input")
    # test_lable.pack(side=LEFT)
    install_but.bind('<Button-1>', setup_create)
    install_but.bind("<Enter>", install_but_button_hover_in)
    install_but.bind("<Leave>", install_but_button_hover_out)
    return cart_footer_form


def setup_create(event):
    global install_list, install_but, cart_root, ch, acc_ra, soft_tree, root_main
    if install_but['text'] == install_button_text:
        if ch:
            m_con = MainController()
            soft_tree = m_con.create_setup(install_list)
            for soft in soft_tree:
                if len(soft) > 1:
                    massage = GuiPopupWindow(cart_root,
                                             acc_ra,
                                             work_area,
                                             "Select Versions",
                                             soft,
                                             [0.4615, 0.5, 0.2702, 5],
                                             btn_txt="Continue"
                                             )
                    ch = False
                    cart_root.wait_window(massage.top)
                    ch = True
                    k = 0
                    for node in soft:
                        if massage.value[k].get() == 0 and node.get_do_install() == True:
                            node.set_do_install(False)
                            node.print_node()
                        k += 1

            create_prosesing_cart_body()
    else:
        cart_root.destroy()
        root_main.deiconify()
        MainController().run_install(root_main, soft_tree, acc_ra, work_area)


def create_prosesing_cart_body():
    global cart_body_frame, install_but, style, soft_tree
    for widget in cart_body_frame.winfo_children():
        widget.destroy()

    body_table_col_name = ('Name', 'Version')
    cart_table = Treeview(cart_body_frame, columns=body_table_col_name, show='headings')
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=(None, 20))
    style.configure("Treeview", font=(None, 15), rowheight=40)
    style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))
    for col in body_table_col_name:
        cart_table.heading(col, text=col)

    ch_int = 0
    for soft in soft_tree:
        for node in soft:
            if node.get_do_install():
                cart_table.insert("", "end", node.get_ver_id(), text=str(node.get_ver_id()),
                                  values=(node.get_soft_name(),
                                          node.get_ver()))
                if ch_int % 2 == 0:
                    cart_table.item(node.get_ver_id(), tags='evenrow')
                else:
                    cart_table.item(node.get_ver_id(), tags='oddrow')
                ch_int += 1

    cart_table.tag_configure("evenrow", background=cart_even_row_bg, foreground='black')
    cart_table.tag_configure("oddrow", background=cart_odd_row_bg, foreground='black')
    cart_table.pack(fill=BOTH, expand=1)

    install_but.config(text=install_button_text2)
