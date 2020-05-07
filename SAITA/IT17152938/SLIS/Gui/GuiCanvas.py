from tkinter import *
from win32api import GetMonitorInfo, MonitorFromPoint
from PIL import ImageTk, Image
from Data.Veriables import *

# get monitor working aria size
monitor_fo = GetMonitorInfo(MonitorFromPoint((0, 0)))
work_area = monitor_fo.get("Work")
acc_ra = work_area[3] / work_area[2]
print(acc_ra)

# search box
search_box = None
# search button
search_but = None

# check variabale
i = 0


def create_full_show_window(win_root):
    full_show_window = Frame(win_root, bg=full_window_color, highlightthickness=0)
    head_show_window = create_head_show_window(full_show_window)
    body_show_window = create_body_show_window(full_show_window)
    head_show_window.pack(fill=X)
    body_show_window.pack(fill=BOTH)
    return full_show_window


def create_head_show_window(full_window):
    global search_box, search_but
    head_window = Frame(full_window, bg=head_window_color, highlightthickness=0)
    search_box = Entry(head_window,
                       bg=main_search_color_bg,
                       fg=main_search_color_txt,
                       width=round(100 * acc_ra)
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
    body_window = Frame(full_window, bg=body_window_color, highlightthickness=0)

    return body_window


def search_soft(event):
    global i, search_box
    print("search start", i, "   ", search_box.get())
    i = i + 1


def search_button_hover_in(event):
    global search_but
    search_but['bg'] = main_search_but_hover


def search_button_hover_out(event):
    global search_but
    search_but['bg'] = main_search_but_bg
