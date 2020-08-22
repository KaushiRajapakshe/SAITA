from tkinter import*
from Data.Variables import *
from GUI.GuiCanvas import *

root = Tk()
# turns off title bar
root.overrideredirect(True)

# set taskbar icon
root.iconbitmap(logo)

screen_size = "{}x{}".format(work_area[2], work_area[3])

# set new geometry
root.geometry(screen_size + '+0+0')


def mini_screen(event):
    root.overrideredirect(False)
    add_log(log_types[2], "GuiMain.py", "mini_screen : " + str(event))
    root.iconify()


def max_screen(event):
    add_log(log_types[2], "GuiMain.py", "max_screen : " + str(event))
    root.overrideredirect(True)


# make a frame for the title bar
title_bar = Frame(root,
                  bg=title_bar_bg,
                  relief='raised',
                  bd=0
                  )

# put a close button on the title bar
close_button = Button(title_bar,
                      text='x',
                      command=root.destroy,
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
# minimuice button
mini_button = Button(title_bar,
                     text='-',
                     bg=title_bar_bg,
                     padx=5,
                     pady=2,
                     activebackground=mini_but_acc_bg,
                     bd=0,
                     font="bold",
                     fg=title_bar_but_txt_color,
                     activeforeground=title_bar_but_txt_color,
                     highlightthickness=0
                     )

# window title
title_name = Label(title_bar, text=title_bar_txt, bg=title_bar_bg, fg=title_bar_txt_color, font="bold")

# title bar img
img = Image.open(logo)
new_img_w, new_img_h = img.size
new_img_w *= acc_ra * logo_div
new_img_h *= acc_ra * logo_div
img = img.resize((round(new_img_w), round(new_img_h)))
title_img = ImageTk.PhotoImage(img)
# title_img = ImageTk.PhotoImage(Image.open(logo))
title_img_set = Label(title_bar, image=title_img, bg=title_bar_bg, )

# a canvas for the main area of the window
window = create_full_show_window(root)

# pack the widgets
title_bar.pack(fill=X)
title_img_set.pack(side=LEFT)
title_name.pack(side=LEFT)
close_button.pack(side=RIGHT)
mini_button.pack(side=RIGHT)
window.pack(expand=1, fill=BOTH)
x_axis = None
y_axis = None


# bind title bar motion to the move window function


def move_window(event):
    add_log(log_types[2], "GuiMain.py", "Move Window : " + str(event))
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))


def close_btn_on_hovering(event):
    global close_button
    add_log(log_types[2], "GuiMain.py", "close_btn_on_hovering : " + str(event))
    close_button['bg'] = close_but_acc_bg


def mini_btn_on_hovering(event):
    global mini_button
    add_log(log_types[2], "GuiMain.py", "mini_btn_on_hovering : " + str(event))
    mini_button['bg'] = mini_but_acc_bg


def return_to_normal_state(event):
    global close_button
    global mini_button
    add_log(log_types[2], "GuiMain.py", "return_to_normal_state : " + str(event))
    close_button['bg'] = title_bar_bg
    mini_button['bg'] = title_bar_bg


# action bind
# title_bar.bind('<B1-Motion>', move_window)
close_button.bind('<Enter>', close_btn_on_hovering)
close_button.bind('<Leave>', return_to_normal_state)
mini_button.bind('<Enter>', mini_btn_on_hovering)
mini_button.bind('<Leave>', return_to_normal_state)
title_bar.bind('<Map>', max_screen)
mini_button.bind('<Button-1>', mini_screen)
root.mainloop()

