from tkinter import *
from tkinter import ttk
from Software import Software

soft = Software()
root = Tk()
root.title("SAITA - Software List Installation System")
root.iconbitmap('logo.ico')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_width)
print(screen_height)
root.geometry(str(screen_width)+"x"+str(screen_height))
first_name_label = Label(root, text="First Name sdfvggggggffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff").grid(row=1, column=0, sticky=W, padx=10)
first_name_label = Label(root, text="First Name sdfvggggggffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff").grid(row=1, column=1, sticky=W, padx=10)
first_name_label = Label(root, text="First Name sdfvggggggffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff").grid(row=1, column=3, sticky=W, padx=10)
root.mainloop()
