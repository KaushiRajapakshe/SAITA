from win32api import GetMonitorInfo, MonitorFromPoint

from Controllers.Chat_Controller import ChatController
from Data.Variables import *
from Data.Log import *
from tkinter import *
import time
from Util.SayText import SayText
from Models.Chat import TestChat
time_string = time.strftime('%H:%M:%S')
msg = "hii"

chatcon = ChatController()
userreply = []

time1 = ''
from PIL import ImageTk, Image
import tkinter as tk

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


def create_full_show_window(win_root):
    full_show_window = Frame(win_root, bg=full_window_color, highlightthickness=0)
    head_show_window = create_head_show_window(full_show_window,win_root)
    head_show_window.pack(expand=1, fill=BOTH)

    return full_show_window


large_font = ('Verdana', 17)


def create_head_show_window(full_window,win_root):
    global search_box, search_but
    head_window = Frame(full_window, bg=head_window_color, highlightthickness=0)

    clock = Label(head_window, font=("Square721 BT", 13, 'bold'), fg="gray29", bg="white")
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

    file_in = img_location
    pil_image = Image.open(file_in)
    image200x100 = pil_image.resize((500, 500), Image.ANTIALIAS)
    tk_image1 = ImageTk.PhotoImage(image200x100)
    global img_show
    img_show = tk_image1
    label2 = tk.Label(head_window, image=img_show, bg="white").pack(padx=80, pady=0, side=tk.LEFT)

    label4 = tk.Label(head_window, text="SAITA", font=("Square721 BT", 55, 'bold'), fg="gray29", bg="white").place(
        x=230, y=550)
    label5 = tk.Label(head_window, text="Smart Artificial Intelligent Troubleshooting Agent",
                      font=("Square721 BT", 14, 'bold'), fg="gray29", bg="white").place(x=90, y=640)
    label3 = tk.Label(head_window, width=1, height=58, bg="gray29").pack(padx=100, pady=0, side=tk.LEFT)

    def send():
        global chatcon, acc_ra, work_area
        msg = EntryBox.get("1.0", 'end-1c').strip()
        EntryBox.delete("0.0", END)

        if msg != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + msg + '\n\n')
            ChatLog.config(foreground="gray29", font=("Square721 BT", 11, 'bold'))

            chatcon.get_chat().set_usrerep(msg)
            chatcon.chat_question_sequence(acc_ra, work_area, win_root)

            print(msg)

            ChatLog.insert(END, "SAITA : " + chatcon.get_chat().get_lastsaitareply() + '\n\n')
            SayText.get_say_text().say(chatcon.get_chat().get_lastsaitareply())
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

    # Create Chat window
    ChatLog = Text(head_window, bd=0, bg="white", height="8", width="50", font=("Square721 BT", 11, 'bold'), )
    ChatLog.config(state=DISABLED)

    # Bind scrollbar to Chat window
    scrollbar = Scrollbar(head_window, command=ChatLog.yview, cursor="heart")
    ChatLog['yscrollcommand'] = scrollbar.set

    # Create Button to send message
    SendButton = Button(head_window, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                        bd=0, bg="gray29", activebackground="#3c9d9b", fg='#ffffff',
                        command=send)

    # Create the box to enter message
    EntryBox = Text(head_window, bd=0, bg="gray74", width="29", height="5", font=("Square721 BT", 11, 'bold'))
    label4 = tk.Label(head_window, text="SAITA : Hi!!! This is SAITA fundamental issue solving system. What type of issue do you have ? ",
                      font=("Square721 BT", 11, 'bold'), fg="gray29", bg="white").place(x=787, y=46)

    # Place all components on the screen
    scrollbar.place(x=1500, y=90, height=600)
    ChatLog.place(x=790, y=90, height=600, width=700)
    EntryBox.place(x=790, y=700, height=45, width=570)
    SendButton.place(x=1380, y=700, height=45)

    return head_window

    # bind search key to event
