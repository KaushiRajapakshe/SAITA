from tkinter import *
from win32api import GetMonitorInfo, MonitorFromPoint, EnumDisplayMonitors
from PIL import ImageTk, Image
from Data.Veriables import *
from Data.Log import *
from Util.MainController import MainController
import math

# get monitor working aria size
monitor_fo = GetMonitorInfo(MonitorFromPoint((0, 0)))
add_log(log_types[2], "GuiCanvas.py", "Monitor info : " + str(monitor_fo))
work_area = monitor_fo.get("Work")
acc_ra = work_area[3] / work_area[2]
add_log(log_types[2], "GuiCanvas.py", "set acc_ra: " + str(acc_ra))

# search box
search_box = None
# search button
search_but = None

# body
body_window = None
body_window_canves = None


def create_full_show_window(win_root):
    full_show_window = Frame(win_root, bg=full_window_color, highlightthickness=0)
    head_show_window = create_head_show_window(full_show_window)
    body_show_window = create_body_show_window(full_show_window)
    head_show_window.pack(fill=X)
    body_show_window.pack(expand=1, fill=BOTH)
    return full_show_window


def create_head_show_window(full_window):
    global search_box, search_but
    head_window = Frame(full_window, bg=head_window_color, highlightthickness=0)
    search_box = Entry(head_window,
                       bg=main_search_color_bg,
                       fg=main_search_color_txt,
                       font="bold",
                       width=round(50 * acc_ra)
                       )
    search_box.pack(
        side=LEFT,
        padx=20 * acc_ra,
        pady=20 * acc_ra,
        ipadx=20 * acc_ra,
        ipady=20 * acc_ra

    )

    search_but = Button(head_window,
                        text=main_search_but_txt,
                        bg=main_search_but_bg,
                        activebackground=main_search_but_acc,
                        bd=2,
                        font="bold",
                        fg=main_search_but_txt_color,
                        activeforeground=main_search_but_txt_color,
                        highlightthickness=0
                        )

    search_but.pack(
        side=LEFT,
        padx=20 * acc_ra,
        pady=20 * acc_ra,
        ipadx=20 * acc_ra,
        ipady=20 * acc_ra

    )

    # bind search key to event
    search_but.bind("<Button-1>", search_soft)
    search_but.bind("<Enter>", search_button_hover_in)
    search_but.bind("<Leave>", search_button_hover_out)

    return head_window


def create_body_show_window(full_window):
    global body_window, body_window_canves
    main_body_window = Frame(full_window, bg=body_window_color, highlightthickness=0, padx=20 * acc_ra,
                             pady=20 * acc_ra)
    body_window_canves = Canvas(main_body_window, bg=body_window_color, highlightthickness=0)
    body_window = Frame(body_window_canves, bg=body_window_color)
    body_scrollbar = Scrollbar(main_body_window, orient="vertical", command=body_window_canves.yview)
    body_window_canves.configure(yscrollcommand=body_scrollbar.set)
    body_scrollbar.pack(side="right", fill="y")
    body_window_canves.pack(expand=1, fill=BOTH)
    body_window_canves.create_window((0, 0), window=body_window, anchor='nw')
    body_window.bind("<Configure>", scroll_all)
    main_con = MainController()
    soft_list = main_con.get_soft_list()
    create_body_data(soft_list)
    return main_body_window


def search_soft(event):
    global i, search_box
    add_log(log_types[2], "GuiCanvas.py", "search_soft : " + str(event) + "  Data : " + search_box.get())
    main_con = MainController()
    soft_list = main_con.get_soft_list()
    create_body_data(soft_list)


def search_button_hover_in(event):
    global search_but
    add_log(log_types[2], "GuiCanvas.py", "search_button_hover_in : " + str(event))
    search_but['bg'] = main_search_but_hover


def search_button_hover_out(event):
    global search_but
    add_log(log_types[2], "GuiCanvas.py", "search_button_hover_out : " + str(event))
    search_but['bg'] = main_search_but_bg


def scroll_all(event):
    global body_window_canves
    add_log(log_types[2], "GuiCanvas.py", "scroll_all : " + str(event))
    body_window_canves.configure(scrollregion=body_window_canves.bbox("all"))


def create_body_data(soft_list):
    global body_window,work_area
    wid = round((work_area[2]-(round(20 * acc_ra) *12))/coll_count)
    print(round(20 * acc_ra) *5)
    add_log(log_types[2], "GuiCanvas.py", "create_body_data : " + str(soft_list))
    ch = 0
    x_range =math.ceil(len(soft_list) / coll_count)
    # x_range = 50
    for x in range(x_range):
        # row_frame = Frame(body_window, bg=body_window_color, highlightthickness=0)
        for y in range(coll_count):
            if ch == len(soft_list):
                break
            else:
                singal_frame = Frame(body_window, bg=body_window_color, highlightthickness=0, padx=20 * acc_ra, pady=20 * acc_ra)
                singal_frame_in= Canvas(singal_frame, bg=cell_bg, highlightthickness=0, width=wid, height=wid)
                soft_topic = Label(singal_frame_in, text=soft_list[ch]['name'], bg=cell_bg, fg=cell_topic_txt_color, font="bold")
                singal_frame.grid(row=x, column=y)
                singal_frame_in.grid(row=0, column=0)
                # singal_frame.grid_propagate(False)
                singal_frame_in.grid_propagate(False)
                soft_topic.grid(row=0, column=0)
                soft_topic.grid_propagate(False)
                ch += 1
        # row_frame.pack(fill=X)
