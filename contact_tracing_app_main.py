import tkinter as tk
from contact_tracing_gui import Add
from for_searching_entries import Search

# Create Main Window
main_window = tk.Tk()
main_window.title("Covid Contact Tracing")
main_window.geometry("750x500")
main_window.configure(bg = "#ffeebf")

# Instance of a class
add = Add(main_window)
search = Search(main_window)

# Buttons for adding and searching entry
add_button = tk.Button(main_window, text = "Add an entry", command = add.add_entry, width = 15, height = 2, font = ("Times New Roman", 12), bg = "#ffeebf")
add_button.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

search_button = tk.Button(main_window, text = "Add an entry", command = add.add_entry, width = 15, height = 2, font = ("Times New Roman", 12), bg = "#ffeebf")
search_button.place(relx=0.5, rely=0.60, anchor=tk.CENTER)

# Start the app
main_window.mainloop()