import csv

# Initialize ContactTracing class
class ContactTracing:
    def __init__(self):
        pass
    
    def add_entry(self, name, gender, bday, phone_num, email_add, address, test):
        with open("contact_tracing_entries.csv", "a", newline="") as file:
            write_entry = csv.writer(file)
            write_entry.writerow([name, gender, bday, phone_num, email_add, address, test])
            
