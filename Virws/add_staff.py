import tkinter as tk
from tkinter import messagebox

# add_staff.py

staff_members = []

def add_staff(firstname, lastname, dob, username, password):
    staff = {
        'firstname': firstname,
        'lastname': lastname,
        'dob': dob,
        'username': username,
        'password': password
    }
    staff_members.append(staff)
    messagebox.showinfo("Success", "Staff member added successfully!")

def submit():
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    dob = entry_dob.get()
    username = entry_username.get()
    password = entry_password.get()
    
    add_staff(firstname, lastname, dob, username, password)
    print(staff_members)

def login(username, password):
    for staff in staff_members:
        if staff['username'] == username and staff['password'] == password:
            messagebox.showinfo("Login Success", "Welcome, " + staff['firstname'] + "!")
            return True
    messagebox.showerror("Login Failed", "Invalid username or password")
    return False

def login_submit():
    username = entry_login_username.get()
    password = entry_login_password.get()
    login(username, password)

def back_to_dashboard():
    messagebox.showinfo("Dashboard", "Returning to the dashboard...")

# Create the main window
root = tk.Tk()
root.title("Add Staff Member")

# Create and place the labels and entry widgets for adding staff
tk.Label(root, text="First Name").grid(row=0, column=0)
entry_firstname = tk.Entry(root)
entry_firstname.grid(row=0, column=1)

tk.Label(root, text="Last Name").grid(row=1, column=0)
entry_lastname = tk.Entry(root)
entry_lastname.grid(row=1, column=1)

tk.Label(root, text="Date of Birth (YYYY-MM-DD)").grid(row=2, column=0)
entry_dob = tk.Entry(root)
entry_dob.grid(row=2, column=1)

tk.Label(root, text="Username").grid(row=3, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=3, column=1)

tk.Label(root, text="Password").grid(row=4, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=4, column=1)

# Create and place the submit button for adding staff
submit_button = tk.Button(root, text="Add Staff Member", command=submit)
submit_button.grid(row=5, columnspan=2)

# Create and place the labels and entry widgets for login
tk.Label(root, text="Login Username").grid(row=6, column=0)
entry_login_username = tk.Entry(root)
entry_login_username.grid(row=6, column=1)

tk.Label(root, text="Login Password").grid(row=7, column=0)
entry_login_password = tk.Entry(root, show="*")
entry_login_password.grid(row=7, column=1)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=login_submit)
login_button.grid(row=8, columnspan=2)

# Create and place the "Back to Dashboard" button
back_button = tk.Button(root, text="Back to Dashboard", command=back_to_dashboard)
back_button.grid(row=9, columnspan=2)

# Run the application
root.mainloop()
