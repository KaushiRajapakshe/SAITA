from win32api import GetMonitorInfo, MonitorFromPoint

from ARTA.config import config_controller
from ARTA.controllers.chat.chat_controller import ChatController
from tkinter import Frame, Label, BOTH, TOP, END, NORMAL, DISABLED, Text, Scrollbar, Button
from PIL import ImageTk, Image
import tkinter as tk

import time

from ARTA.data import variables
from ARTA.data.log import add_log, log_types
from ARTA.data.variables import head_window_color, full_window_color

# Define Time format
from ARTA.model.SayText import SayText

time_string = time.strftime('%H:%M:%S')
msg = "hii"

# Define Chat Controller Variable as chatcon
chatcon = ChatController()
# Define user reply list variable
userreply = []
# Define time1 string variable as null
time1 = ''

# get monitor working aria size
monitor_fo = GetMonitorInfo(MonitorFromPoint((0, 0)))
add_log(log_types[2], "GuiCanvas.py", "Monitor info : " + str(monitor_fo))
work_area = monitor_fo.get("Work")
acc_ra = work_area[3] / work_area[2]
add_log(log_types[2], "GuiCanvas.py", "set acc_ra: " + str(acc_ra))

# img
img_show = None

# body
body_window = None
body_window_canves = None


# CREATE full show window for Installed Application GUI
def create_full_show_window(win_root):
    full_show_window = Frame(win_root, bg=full_window_color, highlightthickness=0)
    head_show_window = create_head_show_window(full_show_window, win_root)
    head_show_window.pack(expand=1, fill=BOTH)

    return full_show_window


large_font = ('Verdana', 17)


# CREATE head show window for Installed Application GUI
def create_head_show_window(full_window, win_root):
    global search_box, search_but
    head_window = Frame(full_window, bg=head_window_color, highlightthickness=0)

    clock = Label(head_window, font=("Square721 BT", 11, 'bold'), fg="gray29", bg="white")
    clock.pack(padx=130, pady=0, side=TOP)

    def tick():
        global time1
        # get the current local time from the PC
        time2 = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, tick)

    clock.config(text="CLOCK:" + str(tick()))

    pil_image = Image.open(variables.file_in)
    image200x100 = pil_image.resize((400, 400), Image.ANTIALIAS)
    tk_image1 = ImageTk.PhotoImage(image200x100)
    global img_show
    img_show = tk_image1
    label2 = tk.Label(head_window, image=img_show, bg="white").pack(padx=variables.label2_x, pady=0, side=tk.LEFT)

    label4 = tk.Label(head_window, text="SAITA", font=("Square721 BT", 45, 'bold'), fg="gray29", bg="white").place(
        x=variables.label4_x, y=variables.label4_y)
    label5 = tk.Label(head_window, text="Smart Artificial Intelligent Troubleshooting Agent",
                      font=("Square721 BT", 14, 'bold'), fg="gray29", bg="white").place(x=variables.label5_x,
                                                                                        y=variables.label5_y)
    label3 = tk.Label(head_window, width=variables.label3_w, height=variables.label3_h,
                      bg="gray29").pack(padx=variables.label3_padx, pady=variables.label3_pady, side=tk.LEFT)

    # initialise config object using the config_controller
    app_config = config_controller.init_config(variables.app_config_path)
    # set scheduler_log_scan string value
    app_config.set("log", "scheduler_log_scan", 'enable')
    config_controller.save(variables.app_config_path, app_config)

    def send(event, full_root):
        global chatcon, acc_ra, work_area
        msg = entry_box.get("1.0", 'end-1c').strip()
        entry_box.delete("0.0", END)

        if msg != '':
            chat_log.config(state=NORMAL)
            chat_log.insert(END, "You: " + msg + '\n\n')
            chat_log.config(foreground="gray29", font=("Square721 BT", 11, 'bold'))

            chatcon.get_chat().set_usrerep(msg)
            chatcon.chat_question_sequence(work_area, acc_ra, full_root)

            chat_log.insert(END, "SAITA : " + chatcon.get_chat().get_lastsaitareply() + '\n\n')

            chat_log.config(state=DISABLED)
            chat_log.yview(END)

    # Create Chat window
    chat_log = Text(head_window, bd=0, bg="white", height="8", width="50", font=("Square721 BT", 11, 'bold'), )
    chat_log.config(state=DISABLED)

    # Bind scrollbar to Chat window
    scrollbar = Scrollbar(head_window, command=chat_log.yview, cursor="heart")
    chat_log['yscrollcommand'] = scrollbar.set

    # Create Button to send message
    send_button = Button(head_window, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                        bd=0, bg="gray29", activebackground="#3c9d9b", fg='#ffffff')
    send_button.bind("<Button-1>", lambda eff, full_root=win_root:
    send(eff, full_root=full_root))

    # Create the box to enter message
    entry_box = Text(head_window, bd=0, bg="gray74", width="29", height="5", font=("Square721 BT", 11, 'bold'))
    label4 = tk.Label(head_window,
                      text="SAITA : Hi!!! This is SAITA pre selected application problem solving system.\nDo you like "
                           "to run error preventing scan for your operating system.? (Yes / No)",
                      font=("Square721 BT", 11, 'bold'), fg="gray29", bg="white").place(x=variables.label4_xx,
                                                                                        y=variables.label4_yy)
    SayText.get_say_text().say(variables.q11)

    # Place all components on the screen
    scrollbar.place(x=variables.scrollbar_x, y=variables.scrollbar_y, height= variables.scrollbar_h)
    chat_log.place(x=variables.chat_log_x, y=variables.chat_log_y, height=variables.chat_log_h,
                   width=variables.chat_log_w)
    entry_box.place(x=variables.entry_box_x, y=variables.entry_box_y, height= variables.entry_box_h, width=variables.entry_box_w)
    send_button.place(x=variables.send_button_x, y=variables.send_button_y, height=variables.send_button_h)

    return head_window
