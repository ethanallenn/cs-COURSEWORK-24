import tkinter as tk
from tkinter import ttk
from Controllers.controller import SQLController

'''
The 'View' contains all the UI for the software. It can call methods from the 'controller' class 
through widgets i.e. Buttons. 
** 'View' should never contain any actual code!!! It should only be able to use methods and code
from the controller. **
'''

class PrescriptionSearchView(ttk.Frame):

    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        # declaring the controller as 'self.control' and passing the 'view' into controller.py
        self.control = SQLController(PrescriptionSearchView)
        
        # create widgets here
        self.search_label = ttk.Label(self, text="Search Prescription:")
        self.search_label.grid(row=0, column=0, padx=10, pady=10)

        self.search_entry = ttk.Entry(self)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = ttk.Button(self, text="Search", command=self.search_prescription)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        self.result_label = ttk.Label(self, text="")
        self.result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def search_prescription(self):
        query = self.search_entry.get()
        result = self.control.search_prescription(query)
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prescription Search")
    prescription_search_view = PrescriptionSearchView(root)
    prescription_search_view.pack(expand=True, fill='both')
    root.mainloop()