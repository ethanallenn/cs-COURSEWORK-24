import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Here you can add your authentication logic
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# Create the main window
root = tk.Tk()
root.title("Login Window")

# Create a frame for the login form
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

# Username label and entry
label_username = tk.Label(frame, text="Username")
label_username.grid(row=0, column=0, pady=5)
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, pady=5)

# Password label and entry
label_password = tk.Label(frame, text="Password")
label_password.grid(row=1, column=0, pady=5)
entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, pady=5)

# Login button
button_login = tk.Button(frame, text="Login", command=login)
button_login.grid(row=2, columnspan=2, pady=10)

# Run the application
root.mainloop()