# Import tkinter module
from tkinter import *

# Create Labels
parent = Tk()
parent.title("Covid Contact Tracing")
parent.geometry("300x200")
name = Label(parent, text = "Name: ")
gender = Label(parent, text = "Gender: ")
bday = Label(parent, text = "Birthday: ")
phone_num = Label(parent, text = "Phone Number: ")
email_add = Label(parent, text = "Email Address: ")
address = Label(parent, text = "Address: ")

# Button
enter_btn = Button(parent, text = "Submit")


# Create Entry Fields
name_entry = Entry(parent)
gender_entry = Entry(parent)
bday_entry = Entry(parent)
phine_num_entry = Entry(parent)
email_add_entry = Entry(parent)
address_entry = Entry(parent)

# Place Labels and entry fields
name.grid(row = 0, column = 1)


parent.mainloop()
