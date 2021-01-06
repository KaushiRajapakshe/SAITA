from tkinter import Entry, END, Toplevel, Label, Button
from tkinter import messagebox

import requests

from ARTA.config import config_controller
from ARTA.data import variables
from ARTA.data.variables import logo


def click_feedback_ui():
    # Function to set focus (cursor)
    def focus1(event):
        # set focus on the email_field box
        email_field.focus_set()

    # Function to set focus
    def focus2(event):
        # set focus on the contact_number_field box
        contact_number_field.focus_set()

    # Function to set focus
    def focus3(event):
        # set focus on the error_type_field box
        error_type_field.focus_set()

    # Function to set focus
    def focus4(event):
        # set focus on the error_description_field box
        error_description_field.focus_set()

    # Function to set focus
    def focus5(event):
        # set focus on the application_name_field box
        application_name_field.focus_set()

    # Function to set focus
    def focus6(event):
        # set focus on the application_version_field box
        application_version_field.focus_set()

    # Function for clearing the
    # contents of text entry boxes
    def clear():
        # clear the content of text entry box
        name_field.delete(0, END)
        email_field.delete(0, END)
        contact_number_field.delete(0, END)
        error_type_field.delete(0, END)
        error_description_field.delete(0, END)
        application_name_field.delete(0, END)
        application_version_field.delete(0, END)

    # Function to take data from GUI
    # window and write to an excel file
    def insert():
        # if user not fill any entry
        # then print "empty input"
        if (name_field.get() == "" or
                email_field.get() == "" or
                contact_number_field.get() == "" or
                error_type_field.get() == "" or
                error_description_field.get() == "" or
                application_name_field.get() == "" or
                application_version_field.get() == ""):

            messagebox.showwarning("SAITA", "Please enter all details.")
            print("empty input")
            name_field.focus_set()

        else:
            # initialise config object using the config_controller
            app_config = config_controller.init_config(variables.app_config_path)
            # set scheduler_log_scan string value
            admin_context_path = app_config.get("admin", "admin_context_path")
            try:
                r = requests.post(admin_context_path, json={'applicationName': application_name_field.get(),
                                                            'applicationVersion': application_version_field.get(),
                                                            'errorType': error_type_field.get(),
                                                            'errorDescription': error_description_field.get(),
                                                            'userName': name_field.get(),
                                                            'contactNumber': contact_number_field.get(),
                                                            'userEmail': email_field.get()
                                                            })
                if r.status_code == 200:
                    print('Success')
                    messagebox.showinfo("SAITA", "Your feedback successfully submitted.")
                else:
                    print('Fail')
                    messagebox.showerror("SAITA", "Unknown error occurred, \nPlease check the connection.")
            except:
                messagebox.showwarning("SAITA", "Please check the admin server connection.")
                pass

            # set focus on the name_field box
            name_field.focus_set()
            # call the clear() function
            clear()
            # close the feedback gui
            toplevel.destroy()

        # Driver code

    toplevel = Toplevel()

    # set taskbar icon
    toplevel.iconbitmap(logo)

    # set the background colour of GUI window
    toplevel.configure(background='white')

    # toplevel.overrideredirect(True)  # turns off title bar, geometry

    w = 550  # width for the Tk root
    h = 650  # height for the Tk root

    # get screen width and height
    ws = toplevel.winfo_screenwidth()  # width of the screen
    hs = toplevel.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    toplevel.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # will disable max/min tab of window
    toplevel.resizable(0, 0)

    # create a Form label
    heading = Label(toplevel, text="Feedback Form", bg="white", font=("Square721 BT", 13, 'bold'))

    # create a Name label
    name = Label(toplevel, text="Name", bg="white", font=("Square721 BT", 11, 'bold'))

    # create a Email label
    email = Label(toplevel, text="Email", bg="white", font=("Square721 BT", 11, 'bold'))

    # create a Contact Number label
    contact_number = Label(toplevel, text="Contact Number", bg="white", font=("Square721 BT", 11, 'bold'))

    # create a Error Type label
    error_type = Label(toplevel, text="Error Type", bg="white", font=("Square721 BT", 11, 'bold'))

    # create a Error Description label
    error_description = Label(toplevel, text="Error Description", bg="white", font=("Square721 BT", 11, 'bold'))

    # create a Application Name label
    application_name = Label(toplevel, text="Application Name", bg="white", font=("Square721 BT", 11, 'bold'))

    # create a Application Version label
    application_version = Label(toplevel, text="Application Version", bg="white", font=("Square721 BT", 11, 'bold'))

    heading.grid(row=0, column=1, sticky="NW", pady=35)
    name.grid(sticky="W", row=2, column=0, padx=30, pady=12)
    email.grid(sticky="W", row=4, column=0, padx=30, pady=12)
    contact_number.grid(sticky="W", row=6, column=0, padx=30, pady=12)
    error_type.grid(sticky="W", row=8, column=0, padx=30, pady=12)
    error_description.grid(sticky="W", row=10, column=0, padx=30, pady=12)
    application_name.grid(sticky="W", row=12, column=0, padx=30, pady=12)
    application_version.grid(sticky="W", row=14, column=0, padx=30, pady=12)

    # create a text entry box
    # for typing the information
    name_field = Entry(toplevel, bd=0, bg="gray74", width="15", font=("Square721 BT", 11, 'bold'))
    email_field = Entry(toplevel, bd=0, bg="gray74", width="15", font=("Square721 BT", 11, 'bold'))
    contact_number_field = Entry(toplevel, bd=0, bg="gray74", width="15", font=("Square721 BT", 11, 'bold'))
    error_type_field = Entry(toplevel, bd=0, bg="gray74", width="15", font=("Square721 BT", 11, 'bold'))
    error_description_field = Entry(toplevel, bd=0, bg="gray74", width="15", font=("Square721 BT", 11, 'bold'))
    application_name_field = Entry(toplevel, bd=0, bg="gray74", width="15", font=("Square721 BT", 11, 'bold'))
    application_version_field = Entry(toplevel, bd=0, bg="gray74", width="15", font=("Square721 BT", 11, 'bold'))

    # bind method of widget is used for
    # the binding the function with the events

    # whenever the enter key is pressed
    # then call the focus1 function
    name_field.bind("<Return>", focus1)

    # whenever the enter key is pressed
    # then call the focus2 function
    email_field.bind("<Return>", focus2)

    # whenever the enter key is pressed
    # then call the focus3 function
    contact_number_field.bind("<Return>", focus3)

    # whenever the enter key is pressed
    # then call the focus4 function
    error_type_field.bind("<Return>", focus4)

    # whenever the enter key is pressed
    # then call the focus5 function
    error_description_field.bind("<Return>", focus5)

    # whenever the enter key is pressed
    # then call the focus6 function
    application_name_field.bind("<Return>", focus6)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    name_field.grid(row=2, column=1, ipadx="90", ipady="4")
    email_field.grid(row=4, column=1, ipadx="90", ipady="4")
    contact_number_field.grid(row=6, column=1, ipadx="90", ipady="4")
    error_type_field.grid(row=8, column=1, ipadx="90", ipady="4")
    error_description_field.grid(row=10, column=1, ipadx="90", ipady="4")
    application_name_field.grid(row=12, column=1, ipadx="90", ipady="4")
    application_version_field.grid(row=14, column=1, ipadx="90", ipady="4")

    # create a Submit Button and place into the toplevel window
    submit = Button(toplevel, text="Submit", font=("Verdana", 12, 'bold'), width="12", bd=0,
                    bg="gray29", activebackground="#3c9d9b", fg='#ffffff', command=insert)
    submit.grid(row=16, column=1, sticky="NW", pady=50)
