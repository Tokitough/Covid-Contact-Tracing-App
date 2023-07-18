# Import tkinter module
from tkinter import *

class ContactTracingGUI:
    def __init__(self, parent):
        self.parent = parent
    
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
    test_date = Label(parent, text = "Date of Test: ")
    test_result = Label(parent, text = "Test Result: ")

    # Button
    submit_btn = Button(parent, text = "Submit Entry", command= self.add_entry)
    submit_btn.grid(row = 8, column = 1)
    
    search_btn = Button(parent, text = "Search Entry", command=)
    search_btn.grid(row = 8, column = 0)
    
    # Create Entry Fields
    name_entry = Entry(parent)
    gender_entry = Entry(parent)
    bday_entry = Entry(parent)
    phone_num_entry = Entry(parent)
    email_add_entry = Entry(parent)
    address_entry = Entry(parent)
    test_date_entry = Entry(parent)
    test_result_entry = Entry(parent)

    # Place Labels and entry fields
    name.grid(row = 0, column = 0, pady = 10, padx = 5)
    name_entry.grid(row = 0, column = 1)

    gender.grid(row = 1, column = 0, pady = 10, padx = 5)
    gender_entry.grid(row = 1, column = 1)

    bday.grid(row = 2, column = 0, pady = 10, padx = 5)
    bday_entry.grid(row = 2, column = 1)

    phone_num.grid(row = 3, column = 0, pady = 10, padx = 5)
    phone_num_entry.grid(row = 3, column = 1)

    email_add.grid(row = 4, column = 0, pady = 10, padx = 5)
    email_add_entry.grid(row = 4, column = 1)

    address.grid(row = 5, column = 0, pady = 10, padx = 5)
    address_entry.grid(row = 5, column = 1)
    
    test_date.grid(row = 6, column = 0, pady = 10, padx = 5)
    test_date_entry.grid(row = 6, column = 1)
    
    test_result.grid(row = 7, column = 0, pady = 10, padx = 5)
    test_result_entry.grid(row = 7, column = 1)

    parent.mainloop()

    # Function for getting entries
    def add_entry(self):
        name = self.name_entry.get()
        gender = self.gender_entry.get()
        bday = self.bday_entry.get()
        phone_num = self.phone_num_entry.get()
        email_add = self.email_add_entry.get()
        test_date = self.test_date_entry.get()
        test_result = self.test_result_entry.get()
       
    #  Function for clearing entries
    def clear_entry(self):
        name = self.name_entry.delete(0, END)
        gender = self.gender_entry.delete(0, END)
        bday = self.bday_entry.delete(0, END)
        phone_num = self.phone_num_entry.delete(0, END)
        email_add = self.email_add_entry.delete(0, END)
        test_date = self.test_date_entry.delete(0, END)
        test_result = self.test_result_entry.delete(0, END)
        
    # Search Entry
    def search_entry(self):
        name = self.name_entry.get()
        
        