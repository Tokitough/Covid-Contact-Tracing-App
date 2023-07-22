# Import tkinter module
from tkinter import *
from contact_tracing_app import ContactTracing
import tkinter as tk

class ContactTracingGUI:
    def __init__(self, root):
        self.root = root
        
        # Create Labels
        root.title("Covid Contact Tracing")
        root.geometry("700x500")
        name = Label(root, text = "Name: ")
        gender = Label(root, text = "Gender: ")
        bday = Label(root, text = "Birthday: ")
        phone_num = Label(root, text = "Phone Number: ")
        email_add = Label(root, text = "Email Address: ")
        address = Label(root, text = "Address: ")
        test = Label(root, text = "Have you tested for Covid?")
        
        # Create Entry Fields and Radiobuttons
        self.name_entry = Entry(root)
        self.gender_entry = Entry(root)
        self.bday_entry = Entry(root)
        self.phone_num_entry = Entry(root)
        self.email_add_entry = Entry(root)
        self.address_entry = Entry(root)
        
        self.test_var = IntVar()
        test_1 = Radiobutton(root, text = "No", variable = self.test_var, value = 1)
        test_2 = Radiobutton(root, text = "Yes(Negative)", variable = self.test_var, value = 2)
        test_3 = Radiobutton(root, text = "Yes(Positive)", variable = self.test_var, value = 3)
        test_4 = Radiobutton(root, text = "Yes(Pending)", variable = self.test_var, value = 4)
        
        # Place Labels and entry fields
        name.grid(row = 0, column = 0, pady = 10, padx = 5)
        self.name_entry.grid(row = 0, column = 1)

        gender.grid(row = 1, column = 0, pady = 10, padx = 5)
        self.gender_entry.grid(row = 1, column = 1)

        bday.grid(row = 2, column = 0, pady = 10, padx = 5)
        self.bday_entry.grid(row = 2, column = 1)

        phone_num.grid(row = 3, column = 0, pady = 10, padx = 5)
        self.phone_num_entry.grid(row = 3, column = 1)

        email_add.grid(row = 4, column = 0, pady = 10, padx = 5)
        self.email_add_entry.grid(row = 4, column = 1)

        address.grid(row = 5, column = 0, pady = 10, padx = 5)
        self.address_entry.grid(row = 5, column = 1)
        
        test.grid(row = 6, column = 0, pady = 10, padx = 5)
        test_1.place(x = 160, y = 255)
        test_2.place(x = 160, y = 275)
        test_3.place(x = 160, y = 295)
        test_4.place(x = 160, y = 315)
        
        # Button
        self.submit_btn = tk.Button(root, text = "Submit Entry", command = self.add_entry)
        self.submit_btn.place(x = 160, y = 350, width = 90)
    
        self.search_btn = tk.Button(root, text = "Search Entry", command = self.search_entry)
        self.search_btn.place(x = 160, y = 380, width = 90)
        
        # Instance for contact tracing app
        self.contact_trace = ContactTracing()
        
        
    # Function for getting entries
    def add_entry(self):
        name = self.name_entry.get()
        gender = self.gender_entry.get()
        bday = self.bday_entry.get()
        phone_num = self.phone_num_entry.get()
        email_add = self.email_add_entry.get()
        address = self.address_entry.get()
        test = self.test_var.get()
        
        # Call add_entry method from ContactTracing class
        self.contact_trace.add_entry(name, gender, bday, phone_num, email_add, address, test)
        
        self.clear_entry()
        print("Entry Submitted.")
        
    #  Function for clearing entries
    def clear_entry(self):
        self.name_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.bday_entry.delete(0, END)
        self.phone_num_entry.delete(0, END)
        self.email_add_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.test_var.set("")

    # Search Entry
    def search_entry(self):
        
        self.search_window = tk.Toplevel(self.main)
        
        # Search Label, Entry field, and Button
        name = Label(tk.Toplevel, text = "Search for?")
        name.grid(row = 0, column = 0, pady = 10, padx = 5)
        
        name = Entry(tk.Toplevel, text = "Search for?")
        self.name_entry.grid(row = 1, column = 0)
        
        self.name_search = tk.Button(tk.Toplevel, text = "Search Entry", command = self.search_entry)
        self.name_search.place(row = 2, column = 0)
        
        name = self.name_entry.get()
        
        # Call search entry method from ContactTracing class
        entry = self.contact_trace.search_entry(name)
        
        if entry:
            print("Entry found:")
            for item in entry:
                print(item)
        else:
            print("We cannot find this entry")
        
