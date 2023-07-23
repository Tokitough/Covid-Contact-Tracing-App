import csv
import tkinter 
import tkinter as tk
from tkinter import *

# Class for search window
class Search:
    # Constructor
    def __init__(self, main):
        self.main = main
        
    def search(self):
        
        search_window = tk.Toplevel(self.main)
        
        # Search Label, Entry field, and Button
        name = Label(tk.Toplevel, text = "Search for?")
        name.grid(row = 0, column = 0, pady = 10, padx = 5)
        
        name = Entry(tk.Toplevel, text = "Search for?")
        self.name_entry.grid(row = 1, column = 0)
        
        self.name_search = tk.Button(tk.Toplevel, text = "Search Entry", command = self.search_entry)
        self.name_search.place(row = 2, column = 0)