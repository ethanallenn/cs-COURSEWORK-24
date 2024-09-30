import tkinter as tk
from tkinter import ttk
# import sqlite3  # Removed as it is not accessed
from controllers.controller import SQLController


class RegistrationView(ttk.Frame):

    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self.control = SQLController(RegistrationView)

        # make a SQL query here which gets the number of medications and generates a button for each
        self.cursor = self.control.connection.cursor()  # Assuming 'connection' is the correct attribute
        self.cursor.execute('''SELECT medication_ID, medication_name FROM Medications''')
        medications = self.cursor.fetchall()
        
        r, c = 1, 0
        for medication in medications:
            _, medication_name = medication  # Removed unused variable medication_id
            self.reg_button = tk.Button(self, text=f"Register {medication_name}").grid(row=r, column=c)
            r += 1  # Increment row for each button

        # create labels for each medication to store the registers.
        # Additional logic for labels can be added here
