import csv

# Initialize ContactTracing class
class ContactTracing:
    def __init__(self):
        pass
    
    def add_entry(self, name, gender, bday, phone_num, email_add, test):
        with open("contact_tracing_entries.csv", "a", newline="") as file:
            write_entry = csv.writer(file)
            write_entry.writerow([name, gender, bday, phone_num, email_add, test])
            
    def search_entry(self, name):
        # Input name to search
        entry = entry("Enter a name to find \n")
        
        # Read csv
        csv_file = csv.reader(open("contact_tracing_entries", "r"))
        
        # Loop through the csv list
        for row in csv_file:
            if entry == name[0]:
                print(row)