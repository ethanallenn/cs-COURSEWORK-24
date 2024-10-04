import tkinter as tk
from tkinter import messagebox

# Dummy user data for demonstration purposes
users = {'admin': 'password'}
staff_members = []  # List to store staff members

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login System")
        self.geometry("300x200")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.create_login_widgets()

    def create_login_widgets(self):
        tk.Label(self, text="Username").pack(pady=5)
        tk.Entry(self, textvariable=self.username).pack(pady=5)
        tk.Label(self, text="Password").pack(pady=5)
        tk.Entry(self, textvariable=self.password, show='*').pack(pady=5)
        tk.Button(self, text="Login", command=self.login).pack(pady=20)

    def login(self):
        username = self.username.get()
        password = self.password.get()
        if username in users and users[username] == password:
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def show_dashboard(self):
        for widget in self.winfo_children():
            widget.destroy()
        tk.Label(self, text="Dashboard").pack(pady=20)
        tk.Button(self, text="Add New Staff", command=self.add_staff).pack(pady=5)
        tk.Button(self, text="Delete Staff Member", command=self.delete_staff).pack(pady=5)
        tk.Button(self, text="Stock Check", command=self.stock_check).pack(pady=5)
        tk.Button(self, text="Logout", command=self.logout).pack(pady=20)

    def add_staff(self):
        self.withdraw()  # Hide the main window
        AddStaffWindow(self)

    def delete_staff(self):
        self.withdraw()  # Hide the main window
        DeleteStaffWindow(self)

    def stock_check(self):
        messagebox.showinfo("Info", "Stock Check functionality")

    def logout(self):
        self.username.set("")
        self.password.set("")
        self.create_login_widgets()

class AddStaffWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add New Staff")
        self.geometry("300x200")
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Add New Staff").pack(pady=20)
        tk.Label(self, text="Staff Name").pack(pady=5)
        self.staff_name = tk.Entry(self)
        self.staff_name.pack(pady=5)
        tk.Button(self, text="Save", command=self.save_staff).pack(pady=20)
        tk.Button(self, text="Back to Dashboard", command=self.back_to_dashboard).pack(pady=5)

    def save_staff(self):
        staff_name = self.staff_name.get()
        if staff_name:
            staff_members.append(staff_name)
            messagebox.showinfo("Info", f"Staff '{staff_name}' added successfully")
        else:
            messagebox.showerror("Error", "Staff name cannot be empty")

    def back_to_dashboard(self):
        self.destroy()
        self.parent.deiconify()  # Show the main window again

class DeleteStaffWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Delete Staff Member")
        self.geometry("300x200")
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Delete Staff Member").pack(pady=20)
        self.staff_list_frame = tk.Frame(self)
        self.staff_list_frame.pack(pady=5)
        self.update_staff_list()
        tk.Button(self, text="Back to Dashboard", command=self.back_to_dashboard).pack(pady=20)

    def update_staff_list(self):
        for widget in self.staff_list_frame.winfo_children():
            widget.destroy()
        for staff in staff_members:
            frame = tk.Frame(self.staff_list_frame)
            frame.pack(fill='x', pady=2)
            tk.Label(frame, text=staff).pack(side='left', padx=5)
            tk.Button(frame, text="Delete", command=lambda s=staff: self.delete_staff(s)).pack(side='right', padx=5)

    def delete_staff(self, staff_name):
        if staff_name in staff_members:
            staff_members.remove(staff_name)
            messagebox.showinfo("Info", f"Staff '{staff_name}' deleted successfully")
            self.update_staff_list()
        else:
            messagebox.showerror("Error", "Staff name not found")

    def back_to_dashboard(self):
        self.destroy()
        self.parent.deiconify()  # Show the main window again

if __name__ == "__main__":
    app = Application()
    app.mainloop()