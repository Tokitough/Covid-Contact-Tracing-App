# Import tkinter module
from tkinter import *
from contact_tracing_app import ContactTracing
import tkinter as tk

class ContactTracingGUI:
    def __init__(self, root):
        self.root = root
    
    # Create Labels
    root = tk.Tk()
    root.title("Covid Contact Tracing")
    root.geometry("700x500")
    name = Label(root, text = "Name: ")
    gender = Label(root, text = "Gender: ")
    bday = Label(root, text = "Birthday: ")
    phone_num = Label(root, text = "Phone Number: ")
    email_add = Label(root, text = "Email Address: ")
    address = Label(root, text = "Address: ")
    test = Label(root, text = "Have you tested for Covid? \n Select only one")

    # Button
    submit_btn = Button(root, text = "Submit Entry", command = self.add_entry())
    submit_btn.place(x = 160, y = 350, width = 90)
    
    search_btn = Button(root, text = "Search Entry", command = self.search_entry())
    search_btn.place(x = 160, y = 380, width = 90)
    
    # Create Entry Fields and Checkbuttons
    name_entry = Entry(root)
    gender_entry = Entry(root)
    bday_entry = Entry(root)
    phone_num_entry = Entry(root)
    email_add_entry = Entry(root)
    address_entry = Entry(root)
    
    test_var = IntVar()
    test_1 = Checkbutton(root, text = "No", variable = test_var, onvalue = 1, offvalue = 0)
    test_2 = Checkbutton(root, text = "Yes(Negative)", variable = test_var, onvalue = 1, offvalue = 0)
    test_3 = Checkbutton(root, text = "Yes(Positive)", variable = test_var, onvalue = 1, offvalue = 0)
    test_4 = Checkbutton(root,text = "Yes(Pending)", variable = test_var, onvalue = 1, offvalue = 0)
    
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
    
    test.grid(row = 6, column = 0, pady = 10, padx = 5)
    test_1.place(x = 160, y = 255)
    test_2.place(x = 160, y = 275)
    test_3.place(x = 160, y = 295)
    test_4.place(x = 160, y = 315)
    
    # Instance for contact tracing app
    contact_trace = ContactTracing()
    
    root.mainloop()
    # Function for getting entries
    def add_entry(self):
        name = self.name_entry.get()
        gender = self.gender_entry.get()
        bday = self.bday_entry.get()
        phone_num = self.phone_num_entry.get()
        email_add = self.email_add_entry.get()
        test = self.test_var.get()
        
        # Call add_entry method from ContactTracing class
        self.contact_trace.add_entry(name, gender, bday, phone_num, email_add, test)
        
        self.clear_entry()
        print("Entry Submitted.")
        
    #  Function for clearing entries
    def clear_entry(self):
        self.name_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.bday_entry.delete(0, END)
        self.phone_num_entry.delete(0, END)
        self.email_add_entry.delete(0, END)
        self.test.delete(0, END)

    # Search Entry
    def search_entry(self):
        
        search_window = Toplevel(root)
        name = self.name_entry.get()
        
        # Call search entry method from ContactTracing class
        entry = self.contact_trace.search_entry(name)
        
        if entry:
            print("Entry found:")
            for item in entry:
                print(item)
        else:
            print("We cannot find this entry")
        

