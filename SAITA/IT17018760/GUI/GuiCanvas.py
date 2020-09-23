from win32api import GetMonitorInfo, MonitorFromPoint

from Controllers.Chat_Controller import ChatController
from Data.Variables import *
from Data.Log import *
from tkinter import *
import time

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
    head_show_window = GUICna().create_head_show_window(full_show_window)
    head_show_window.pack(expand=1, fill=BOTH)

    return full_show_window


large_font = ('Verdana', 17)

class GUICna:
    ChatLog =None
    def create_head_show_window(self,full_window):
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
        label2 = tk.Label(head_window, image=img_show, bg="white").pack(padx=40, pady=0, side=tk.LEFT)

        label4 = tk.Label(head_window, text="SAITA", font=("Square721 BT", 55, 'bold'), fg="gray29", bg="white").place(
            x=230, y=550)
        label5 = tk.Label(head_window, text="Smart Artificial Intelligent Troubleshooting Agent",
                          font=("Square721 BT", 14, 'bold'), fg="gray29", bg="white").place(x=90, y=640)
        label3 = tk.Label(head_window, width=1, height=58, bg="gray29").pack(padx=100, pady=0, side=tk.LEFT)

        def send(event,cl):
            global chatcon
            msg = EntryBox.get("1.0", 'end-1c').strip()
            EntryBox.delete("0.0", END)

            if msg != '':
                cl.ChatLog.config(state=NORMAL)
                cl.ChatLog.insert(END, "You: " + msg + '\n\n')
                cl.ChatLog.config(foreground="gray29", font=("Square721 BT", 11, 'bold'))

                listOfStrings = ['The code execution cannot proceed because MSVCR100.dll was not found', 'yes', 'no']

                if msg in listOfStrings:
                    chatcon.get_chat().set_usrerep(msg)
                    chatcon.chat_do(cl)
                else:
                    cl.ChatLog.insert(END, "SAITA: Your entered message cannot proceed.Enter the correct message " '\n\n')



                # chatcon.chat_question_sequence()

                #print(msg)

                # ChatLog.insert(END, "SAITA : " + chatcon.get_chat().get_lastsaitareply() + '\n\n')

                    cl.ChatLog.config(state=DISABLED)
                    cl.ChatLog.yview(END)



        # Create Chat window
        self.ChatLog = Text(head_window, bd=0, bg="white", height="8", width="50", font=("Square721 BT", 11, 'bold'), )
        self.ChatLog.config(state=DISABLED)

        # Bind scrollbar to Chat window
        scrollbar = Scrollbar(head_window, command=self.ChatLog.yview, cursor="heart")
        self.ChatLog['yscrollcommand'] = scrollbar.set

        # Create Button to send message
        SendButton = Button(head_window, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                            bd=0, bg="gray29", activebackground="#3c9d9b", fg='#ffffff')
        SendButton.bind("<Button-1>", lambda eff, cl=self:
        send(eff, cl=cl))

        # Create the box to enter message
        EntryBox = Text(head_window, bd=0, bg="gray74", width="29", height="5", font=("Square721 BT", 11, 'bold'))
        label4 = tk.Label(head_window, text="SAITA : Hi!!! Please note your issue.",
                          font=("Square721 BT", 11, 'bold'), fg="gray29", bg="white").place(x=726, y=46)

        # Place all components on the screen
        scrollbar.place(x=1326, y=90, height=506)
        self.ChatLog.place(x=726, y=90, height=506, width=570)
        EntryBox.place(x=720, y=630, height=30, width=470)
        SendButton.place(x=1200, y=630, height=30)


        return head_window

        # bind search key to event
