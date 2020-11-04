#main chat GUI
#importing libraries and classes
import difflib
from win32api import GetMonitorInfo, MonitorFromPoint
from SayText import SayText
from Controllers.Chat_Controller import ChatController
from Data.Variables import *
from Data.Log import *
from tkinter import *
import time
import mysql.connector

from Models.Chat import TestChat

#initialize the current time from the system
time_string = time.strftime('%H:%M:%S')
msg = "hii"    #set default message value because neet to pass the msg variable

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

# img display
img_show = None

# GUI display body
body_window = None
body_window_canves = None


def create_full_show_window(win_root):
    full_show_window = Frame(win_root, bg=full_window_color, highlightthickness=0)
    head_show_window = GUICna().create_head_show_window(full_show_window)
    head_show_window.pack(expand=1, fill=BOTH)

    return full_show_window

#Font style of the GUI
large_font = ('Verdana', 17)

#GUI connection class
class GUICna:
    ChatLog = None

    def create_head_show_window(self, full_window):
        global search_box, search_but
        head_window = Frame(full_window, bg=head_window_color, highlightthickness=0)
        #Place the time in the middle of the GUI
        clock = Label(head_window, font=("Square721 BT", 13, 'bold'), fg="gray29", bg="white")
        clock.pack(padx=130, pady=0, side=TOP)
        #calling say text class which saying the start speech
        SayText.get_say_text().say(start_text)

        #set the current time
        def tick():
            global time1
            # get the current local time from the PC
            time2 = time.strftime('%H:%M:%S')
            # if time string has changed, update it
            if time2 != time1:
                time1 = time2
                clock.config(text=time2)
            # calls itself every 200 milliseconds
            clock.after(200, tick)

        #pass the time text to the GUI
        clock.config(text="CLOCK:" + str(tick()))

        #Get the main image path from the variable file
        file_in = img_location
        pil_image = Image.open(file_in)
        image200x100 = pil_image.resize((500, 500), Image.ANTIALIAS) #resize the image
        tk_image1 = ImageTk.PhotoImage(image200x100)
        global img_show
        img_show = tk_image1
        label2 = tk.Label(head_window, image=img_show, bg="white").pack(padx=40, pady=0, side=tk.LEFT)

        #display SAITA word under the logo
        label4 = tk.Label(head_window, text="SAITA", font=("Square721 BT", 55, 'bold'), fg="gray29", bg="white").place(
            x=230, y=550)
        label5 = tk.Label(head_window, text="Smart Artificial Intelligent Troubleshooting Agent",
                          font=("Square721 BT", 14, 'bold'), fg="gray29", bg="white").place(x=90, y=640)
        label3 = tk.Label(head_window, width=1, height=58, bg="gray29").pack(padx=100, pady=0, side=tk.LEFT)

        #chat send function
        def send(event, cl):
            global chatcon
            msg = EntryBox.get("1.0", 'end-1c').strip()
            EntryBox.delete("0.0", END)

            #system checks chat is empty or not
            if msg != '':
                cl.ChatLog.config(state=NORMAL)
                cl.ChatLog.insert(END, "You: " + msg + '\n\n')  #display the last sent chat
                cl.ChatLog.config(foreground="gray29", font=("Square721 BT", 11, 'bold'))

                #conntection to the database
                mydb = mysql.connector.connect(
                    host=sql_server,
                    user=sql_uname,
                    password=sql_password,
                    database=sql_db
                )
                mycursor = mydb.cursor()

                #to get all service errors which are entered in the
                query = "SELECT * FROM service_error"

                mycursor.execute(query)

                myresult1 = mycursor.fetchall()
                result_t = []
                for y in myresult1:
                    CSVName = y[1]
                    result_t.append(CSVName)

                sim=difflib.get_close_matches(msg,result_t)
                listlen=len(sim)
                yesnolist=['yes','no']
                sim1=difflib.get_close_matches(msg,yesnolist)
                listlen2=len(sim1)


                if listlen2==1:
                    chatcon.get_chat().set_usrerep(''.join(sim1))
                    chatcon.chat_do(cl)
                elif msg in result_t:
                     chatcon.get_chat().set_usrerep(msg)
                     chatcon.chat_do(cl)

                elif listlen > 1:
                    cl.ChatLog.insert(END,
                                      "SAITA: Please choose the correct issue from the following list and retype it again" '\n\n'
                                      +' \n'.join(sim)+'\n\n')
                    SayText.get_say_text().say('SAITA have found '+str(listlen)+'similar errors which you entered Please select your error and retype or copy paste it')
                else:
                    cl.ChatLog.insert(END,
                                      "SAITA:Sorry cannot proceed that your entered value Please check it and try again "'\n\n')
                    SayText.get_say_text().say(not_found_error)


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


        scrollbar.place(x=1326, y=90, height=506)
        self.ChatLog.place(x=726, y=90, height=506, width=570)
        EntryBox.place(x=720, y=630, height=30, width=470)
        SendButton.place(x=1200, y=630, height=30)

        return head_window


