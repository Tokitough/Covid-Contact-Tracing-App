import csv
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Class for search window
class Search:
    # Constructor
    def __init__(self, main):
        self.main = main
        
    def search(self):
        # Create window
        search_window = tk.Toplevel(self.main)
        search_window.title("Searching...")
        search_window.geometry("250x200")
        search_window.configure(bg = "#ffeebf")
        
        # Search Label, Entry field, and Button
        name = Label(search_window, text = "Search for?", bg = "#ffeebf")
        self.name_entry = Entry(search_window, text = "Search for?")
        name_search = tk.Button(search_window, text = "Search Entry", command = self.search_entry, bg = "#ffeebf")
    
        name.pack(anchor='center', padx=50, pady=15)
        self.name_entry.pack(anchor='center', padx=20, pady=2)
        name_search.pack(anchor='center', padx=20, pady=2)
        
    # Funtion to read the csv file
    def search_entry(self):
        # Input name to search
        entry = self.name_entry.get().lower()
        
        # If field is empty
        if not entry.strip():
           messagebox.showerror("!!!", "Please enter a name!")
           return
       
        data = []
        # Read csv
        with open("contact_tracing_entries.csv") as csvfile:
            locator = csv.reader(csvfile)
            for row in locator:
                data.append(row)
        
        # Create list of the names
        entries = [x[0].lower() for x in data if x]
        
        # If name is in the list
        if entry in entries:
            for x in range(0, len(data)):
                if data[x] and entry == data[x][0].lower():
                    # New window for the information of searched entry
                    display_entry = tk.Toplevel(self.main)
                    display_entry.title("Here's what we found: ")
                    display_entry.geometry("500x500")
                    display_entry.configure(bg = "#ffeebf")
                    
                    # Labels for Information
                    name = tk.Label(display_entry, text = "Name (FN,MN,LN): " + str(data[x][0]), bg = "#ffeebf")
                    age = tk.Label(display_entry, text = "Age: " + str(data[x][1]), bg = "#ffeebf")
                    gender = tk.Label(display_entry, text = "Gender: " + str(data[x][2]), bg = "#ffeebf")
                    phone_num = tk.Label(display_entry, text = "Phone Number: " + str(data[x][3]), bg = "#ffeebf")
                    email_add = tk.Label(display_entry, text = "Email Address: " + str(data[x][4]), bg = "#ffeebf")
                    address = tk.Label(display_entry, text = "Address: " + str(data[x][5]), bg = "#ffeebf")
                    test = tk.Label(display_entry, text = "Test Status: " + str(data[x][6]), bg = "#ffeebf")
                    test_equivalent = tk.Label(display_entry, text = "1 = Not Tested \n 2 = Negative \n 3 = Positive \n 4 = Pending", bg = "#ffeebf")
                    
                    name.pack(anchor='center', padx=20, pady=20)
                    gender.pack(anchor='center', padx=20, pady=2)
                    age.pack(anchor='center', padx=20, pady=2)
                    phone_num.pack(anchor='center', padx=20, pady=2)
                    email_add.pack(anchor='center', padx=20, pady=2)
                    address.pack(anchor='center', padx=20, pady=2)
                    test.pack(anchor='center', padx=20, pady=2)
                    test_equivalent.pack(anchor='center', padx=30, pady=2)                   
            
        # If the name is not found        
        else:
            messagebox.showerror("No data found", "We could not find this data")