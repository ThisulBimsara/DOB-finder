import tkinter as tk
from tkinter import messagebox
import datetime

# Function to get and validate the NIC number
def get_nic():
    nic = nic_entry.get().strip()
    if validate_nic(nic):
        birth_date, gender, voting_eligibility = extract_info(nic)
        display_results(birth_date, gender, voting_eligibility)
    else:
        messagebox.showerror("Invalid NIC", "Please enter a valid NIC number.")

# Function to validate the NIC number
def validate_nic(nic):
    if len(nic) == 10:
        # Old NIC format: 9 digits followed by 'V' or 'X'
        return nic[:-1].isdigit() and nic[-1].upper() in ['V', 'X']
    elif len(nic) == 12:
        # New NIC format: 12 digits
        return nic.isdigit()
    else:
        return False

# Function to extract information from the NIC
def extract_info(nic):
    if len(nic) == 10:
        # Old NIC format
        year = int(nic[:2]) + 1900
        day_count = int(nic[2:5])
        gender = 'Female' if day_count > 500 else 'Male'
        if gender == 'Female':
            day_count -= 500
        birth_date = calculate_birth_date(day_count, year)
        voting_eligibility = 'Eligible' if nic[-1].upper() == 'V' else 'Not Eligible'
    elif len(nic) == 12:
        # New NIC format
        year = int(nic[:4])
        day_count = int(nic[4:7])
        gender = 'Female' if day_count > 500 else 'Male'
        if gender == 'Female':
            day_count -= 500
        birth_date = calculate_birth_date(day_count, year)
        voting_eligibility = 'Information not available in new NIC format'
    return birth_date, gender, voting_eligibility

# Function to calculate birth date from day count
def calculate_birth_date(day_count, year):
    date = datetime.datetime(year, 1, 1) + datetime.timedelta(days=day_count - 2)
    return date.strftime("%B %d, %Y")

# Function to display the results
def display_results(birth_date, gender, voting_eligibility):
    result_label.config(text=f"Date of Birth: {birth_date}\nGender: {gender}\nVoting Eligibility: {voting_eligibility}")

# Main GUI setup
root = tk.Tk()
root.title("NIC Analyzer")

# Labels and Entries
tk.Label(root, text="What is your name?").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Type your NIC?").pack(pady=5)
nic_entry = tk.Entry(root)
nic_entry.pack(pady=5)

# Button to submit NIC
submit_button = tk.Button(root, text="Analyze NIC", command=get_nic)
submit_button.pack(pady=10)

# Label to display results
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
