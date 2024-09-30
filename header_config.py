import tkinter as tk
from tkinter import ttk

# This class will be able to change the header shown depending on what functionality is being used,
# e.g., if in the inventory section, it will display "Pharmacy Manager - Inventory".
class Header(tk.LabelFrame):
    
    # 'header' class will constantly update the location in which the user is accessing.
    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.head_label = tk.Label(self, text="Pharmacy Manager")
        self.head_label.grid(row=0, column=0)

    def update_header(self, section):
        self.head_label.config(text=f"Pharmacy Manager - {section}")

if __name__ == "__main__":
    root = tk.Tk()
    head = Header(root)
    head.pack(fill="both", expand=True)
    
    # Example of updating the header
    head.update_header("Inventory")
    
    root.mainloop()

# This class will be able to change the header shown depending on what functionality is being used,
# e.g., if in the inventory section, it will display "Pharmacy Manager - Inventory".
class Header(tk.LabelFrame):
    
    # 'header' class will constantly update the location in which the user is accessing.
    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.head_label = tk.Label(self, text="Pharmacy Manager")
        self.head_label.grid(row=0, column=0)

    def update_header(self, section):
        self.head_label.config(text=f"Pharmacy Manager - {section}")