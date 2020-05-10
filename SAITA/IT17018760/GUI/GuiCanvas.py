import urllib
from tkinter import *
from win32api import GetMonitorInfo, MonitorFromPoint, EnumDisplayMonitors
from SAITA.IT17018760.Data.Veriables import *
from SAITA.IT17018760.Data.Log import *
from tkinter import*
import datetime
from random import choice
import time
time_string = time.strftime('%H:%M:%S')
msg="hii"
time1 = ''
from PIL import ImageTk, Image
import tkinter as tk

import math
from urllib.request import urlopen

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
    head_show_window = create_head_show_window(full_show_window)
    head_show_window.pack(expand=1, fill=BOTH)


    return full_show_window

large_font = ('Verdana',17)

def create_head_show_window(full_window):
    global search_box, search_but
    head_window = Frame(full_window, bg=head_window_color, highlightthickness=0)

    clock = Label(head_window, font=("Square721 BT", 11, 'bold'), fg="gray29",bg="white")
    clock.place(x=720,y=5)

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




#Text field input getter
    def retrieve_input():
        global msg
        msg = EntryBox.get("1.0", 'end-1c').strip()
        EntryBox.delete("0.0", END)
        if msg != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, "You: " + msg + '\n\n\n\n')
            ChatLog.config(selectforeground="Blue", font=("Square721 BT", 11, 'bold'), fg="gray29",bg="white")
            print(msg)
            ChatLog.configure(state='disabled')

            hello = ["hi", "hello", "hai"]

            if any(word in msg for word in hello):
                label7 = tk.Label(head_window, text="Please Enter your Issue: SAITA  ", font=("Square721 BT", 11, 'bold'), fg="white", bg='gray29',width='35').place(x=1000, y=150)











    EntryBox = Text(head_window, height=2, width=60)
    EntryBox.place(x=740, y=635)



    search_but = Button(head_window,
                        text="Send",
                        bg=main_search_but_bg,
                        activebackground=main_search_but_acc,
                        bd=2,
                        font="bold",
                        fg=main_search_but_txt_color,
                        activeforeground=main_search_but_txt_color,
                        highlightthickness=0,
                        height='1',width='9',command=lambda: retrieve_input()).place(x=1250, y=635)

    file_in = 'E:/SLIIT/4 year/CDAP/Presentation/SAITA.png'
    pil_image = Image.open(file_in)
    image200x100 = pil_image.resize((500, 500), Image.ANTIALIAS)
    tk_image1 = ImageTk.PhotoImage(image200x100)
    global img_show
    img_show = tk_image1
    label2 = tk.Label(head_window, image=img_show,bg="white").place(x=80, y=60)

    now = datetime.datetime.now()
    label6 = tk.Label(head_window, text=now, font=("Square721 BT", 11, 'bold'), fg="gray29",bg="white").place(x=1255, y=5)

    label1 = tk.Label(head_window, text="Chat Me ", font=("Helvetica", 16, 'bold'), fg="gray29",bg="white").place(x=980, y=60)
    label4 = tk.Label(head_window, text="SAITA", font=("Square721 BT", 55, 'bold'), fg="gray29",bg="white").place(x=230, y=550)
    label5 = tk.Label(head_window, text="Smart Artificial Intelligent Troubleshooting Agent",
                      font=("Square721 BT", 14, 'bold'), fg="gray29",bg="white").place(x=90, y=640)
    label3 = tk.Label(head_window, width=1, height=58, bg="gray29").place(x=700,y=0)




    ChatLog = Text(head_window, bd=0, bg="White", width="55", font="Arial", fg="Blue",state='disabled')
    ChatLog.grid(row=2, column=0)
    ChatLog.pack(side=RIGHT)
    ChatLog.configure(state='normal')

    # Bind scrollbar to Chat window
    scrollbar = Scrollbar(head_window, orient="vertical", command=ChatLog.yview)
    scroll_x = Scrollbar(head_window, orient="horizontal", command=ChatLog.xview)
    ChatLog.configure(yscrollcommand=scrollbar.set, xscrollcommand=scroll_x.set,state='disabled')










    return head_window




    # bind search key to event












