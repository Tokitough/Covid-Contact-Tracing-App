# Import tkinter module
from tkinter import *

# Create Labels
parent = Tk()
parent.title("Covid Contact Tracing")
parent.geometry("700x500")
name = Label(parent, text = "Name: ")
gender = Label(parent, text = "Gender: ")
bday = Label(parent, text = "Birthday: ")
phone_num = Label(parent, text = "Phone Number: ")
email_add = Label(parent, text = "Email Address: ")
address = Label(parent, text = "Address: ")

# Button
submit_btn = Button(parent, text = "Submit")
submit_btn.grid(row = 7, column = 1)

# Create Entry Fields
name_entry = Entry(parent)
gender_entry = Entry(parent)
bday_entry = Entry(parent)
phone_num_entry = Entry(parent)
email_add_entry = Entry(parent)
address_entry = Entry(parent)

# Place Labels and entry fields
name.grid(row = 0, column = 0)
name_entry.grid(row = 0, column = 1)

gender.grid(row = 1, column = 1, pady = 10, padx = 5)
gender_entry.grid(row = 1, column = 1)

bday.grid(row = 2, column = 1, pady = 10, padx = 5)
bday_entry.grid(row = 2, column = 1)

phone_num.grid(row = 3, column = 1, pady = 10, padx = 5)
phone_num_entry.grid(row = 3, column = 1)

email_add.grid(row = 4, column = 1, pady = 10, padx = 5)
email_add_entry.grid(row = 4, column = 1)

address.grid(row = 5, column = 1, pady = 10, padx = 5)
address_entry.grid(row = 5, column = 1)

parent.mainloop()
