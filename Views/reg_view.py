import tkinter as tk
from tkinter import ttk
# import sqlite3  # Removed as it is not accessed
from Controllers.sql_controller import SQLController


class RegistrationView(ttk.Frame):

    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self.control = SQLController()  # Create an instance of the controller

        # make a SQL query here which gets the number of medications and generates a button for each
        self.cursor = self.control.cursor  # Access the cursor attribute directly
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Medications (
            medication_ID INTEGER PRIMARY KEY,
            medication_name TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''SELECT medication_ID, medication_name FROM Medications''')
        # Create the Medications table if it doesn't exist
        
        self.control.connection.commit()

        # Fetch the medications from the database
        medications = self.cursor.fetchall()
            
        r, c = 1, 0
        for medication in medications:
            _, medication_name = medication  # Removed unused variable medication_id
            self.reg_button = tk.Button(self, text=f"Register {medication_name}").grid(row=r, column=c)
            r += 1  # Increment row for each button

            # create labels for each medication to store the registers.
            # Additional logic for labels can be added here
