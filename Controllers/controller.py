import sqlite3


class SQLController:
    def __init__(self, view=None):
        self.view = view
        # Establish a connection to the 'CallePharmacy.db' database.
        self.conn = sqlite3.connect("/Users/ethanallen/Documents/A2_CourseworkProject/Programming//Controllers/CallePharmacy.db")
        self.cursor = self.conn.cursor()
    
    def change_day_reg(self, day):
        day = day.strip()
        print(f"Control \"{day}\"")
        # Assuming 'Appointments' table exists with 'day' and 'patient_name' fields.
        self.cursor.execute('SELECT patient_name FROM Appointments WHERE day=?', (day,))
        current_reg = self.cursor.fetchall()
        return current_reg  # Return value to view to be put into the UI
    
    def reg_factory(self, day):
        # Placeholder for future implementation
        pass
    
    def mainloop(self):
        # Placeholder for the main loop logic
        print("Main loop started")
        # Add your main loop logic here


if __name__ == "__main__":
    control = SQLController()
    control.mainloop()