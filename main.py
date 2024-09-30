import tkinter as tk
from header_config import Header
from Views.ps_view import PrescriptionSearchView
from Views.reg_view import RegistrationView


class PharmacyApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Calle Pharmacy Management System")
        self.geometry("800x600")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Main container frame
        self.container = tk.LabelFrame(self)

        # Header frame
        self.header = Header(self.container)
        self.header.grid(row=0, column=0, padx=5, pady=5, sticky="NEW")

        # Configure the container frame
        self.container.columnconfigure(0, weight=1)
        self.container.grid(sticky="NESW", padx=5, pady=5)

        # prescription view frame
        self.ps_view = PrescriptionSearchView(self.container)
        self.ps_view.grid(row=2, column=0, padx=5, pady=5)

        # reg view frame
        self.reg_view = RegistrationView(self.container)
        self.reg_view.grid(row=2, column=0, padx=5, pady=5)

if __name__ == '__main__':
    app = PharmacyApp()
    app.mainloop()