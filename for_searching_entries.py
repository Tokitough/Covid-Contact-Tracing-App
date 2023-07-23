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
                    display_entry.title("Result")
                    display_entry.geometry("500x500")
                    
                    # Labels for Information
                    
                    