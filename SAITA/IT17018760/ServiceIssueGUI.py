from tkinter import*
import datetime
from random import choice

from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
root.state("zoomed")
root.grid_columnconfigure(0, weight=1)  # the line I've added

large_font = ('Verdana',18)


label3 = tk.Label(root, width=1, height=58, bg="gray29")
label3.grid(row=20, column=0)


label1=tk.Label(root, text="Chat Me ",font=("Helvetica", 16,'bold'),fg="gray29").place(x=980, y=60)
label4=tk.Label(root, text="SAITA",font=("Square721 BT", 55,'bold'),fg="gray29").place(x=230, y=550)
label5=tk.Label(root, text="Smart Artificial Intelligent Troubleshooting Agent",font=("Square721 BT", 14,'bold'),fg="gray29").place(x=90, y=640)



file_in = 'E:/SLIIT/4 year/CDAP/Presentation/SAITA.png'
pil_image = Image.open(file_in)
image200x100 = pil_image.resize((500, 500), Image.ANTIALIAS)
tk_image1 = ImageTk.PhotoImage(image200x100)
label2 = tk.Label(root,image=tk_image1).place(x=80,y=60)

now = datetime.datetime.now()
label6=tk.Label(root, text=now,font=("Square721 BT", 11,'bold'),fg="gray29").place(x=1255, y=5)


bot1  = StringVar()

start=["start","Start","STARTED","Begin","begin"]
stop=["stop","Stop","STOPPED","End","terminate"]
registry=["edit registry","Edit Registry","registry","Registry"]

def click():
    label7 = tk.Label(root, text=name.get(), font=("Helvetica", 11,'bold'), fg="white",bg='gray29',width='35').place(x=1000,y=550)
    issueType = name.get()
    if any(word in issueType for word in start):
        print(issueType)
        bot1.set("What is the issue")
    elif any(word in issueType for word in stop):
        exec(open("StopService.py").read())
    elif any(word in issueType for word in registry):
        print("Still Build in process")
    else:
        print("Enter the Correct Category")



name = tk.StringVar()
label8 = tk.Label(root, text=bot1.get(), font=("Helvetica", 11,'bold'), fg="gray29", bg='white', width='50').place(x=740,y=600)

nameEntered = tk.Entry(root,font=large_font, textvariable=name,width='35',bg='gray54',fg='black').place(x=710,y=660)
B = Button(root, text ="Send",font=("Helvetica", 11,'bold'),bg='gray29',fg='white',height='1',width='9',command=click).place(x=1255,y=660)

























root.mainloop()

