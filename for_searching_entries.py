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
        search_window.title("Looking for Someone: ")
        search_window.geometry("500x500")
        
        
        # Search Label, Entry field, and Button
        name = Label(tk.Toplevel, text = "Search for?")
        name.grid(row = 0, column = 0, pady = 10, padx = 5)
        
        self.name_entry = Entry(tk.Toplevel, text = "Search for?")
        self.name_entry.grid(row = 1, column = 0)
        
        self.name_search = tk.Button(tk.Toplevel, text = "Search Entry", command = self.search_entry)
        self.name_search.place(row = 2, column = 0)
        
        # Funtion to read the csv file
    def search_entry(self):
        # Input name to search
        entry = self.name_entry.get().lower()
        
        # If field is empty
        if not entry.strip():
           messagebox.showerror("Please enter a name!")
            
        # Read csv
        csv_file = csv.reader(open("contact_tracing_entries", "r"))
            
        # Loop through the csv list
        for row in csv_file:
            if entry == name[0]:
                print(row)
        # Search Entry
        name = self.name_entry.get()
        
        # Call search entry method from ContactTracing class
        entry = self.contact_trace.search_entry(name)
        
        if entry:
            print("Entry found:")
            for item in entry:
            print(item)
        else:
            print("We cannot find this entry")