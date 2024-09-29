import tkinter as tk
from tkinter import ttk
import sqlite3
from Controllers.controller import SQLController


class RegistrationView(ttk.Frame):

    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self.control = SQLController(RegistrationView)

        # make a SQL query here which gets the number of medications and generates a button for each
        self.cursor = self.control.get_cursor()
        self.cursor.execute('''SELECT medication_ID, medication_name FROM Medications''')
        medications = self.cursor.fetchall()
        
        r, c = 1, 0
        for medication in medications:
            medication_id, medication_name = medication
            self.reg_button = tk.Button(self, text=f"Register {medication_name}").grid(row=r, column=c)
            r += 1  # Increment row for each button

        # create labels for each medication to store the registers.
        # Additional logic for labels can be added here
