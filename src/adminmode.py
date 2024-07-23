import tkinter as tk
from tkinter import messagebox
import src.med_reco as med

class AdminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Mode")
        self.root.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Admin Mode", font=("Arial", 20)).pack()

        self.buttons = [
            ("Add new user", self.add_user),
            ("Delete user", self.delete_user),
            ("Update user", self.update_user),
            ("Add new hospital", self.add_hospital),
            ("Delete hospital", self.delete_hospital),
            ("Update hospital", self.update_hospital),
            ("Add new doctor", self.add_doctor),
            ("Delete doctor", self.delete_doctor),
            ("Update doctor working hospital", self.update_doctor),
            ("Display mode", self.display_mode),
            ("Logout", self.logout),
            ("Exit", self.exit_app)
        ]

        for text, command in self.buttons:
            tk.Button(self.frame, text=text, command=command).pack(fill="x", pady=5)

    def add_user(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add New User")
        self.new_window.geometry("400x400")

        fields = ['Aadhaar Card No', 'First Name', 'Last Name', 'Date of Birth (yyyy-mm-dd)', 'Gender', 'Contact No', 'Address']
        self.entries = {}

        for field in fields:
            frame = tk.Frame(self.new_window)
            frame.pack(pady=5)
            label = tk.Label(frame, text=field)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.RIGHT)
            self.entries[field] = entry

        submit_button = tk.Button(self.new_window, text="Submit", command=self.submit_user)
        submit_button.pack(pady=20)

    def submit_user(self):
        try:
            aadhaar = self.entries['Aadhaar Card No'].get()
            firstname = self.entries['First Name'].get()
            lastname = self.entries['Last Name'].get()
            dob = self.entries['Date of Birth (yyyy-mm-dd)'].get()
            gender = self.entries['Gender'].get()
            contact = self.entries['Contact No'].get()
            address = self.entries['Address'].get()

            query = f"INSERT INTO Aadhaar (aadhar, first_name, last_name, dob, gender, contact_info, address) VALUES({aadhaar}, '{firstname}', '{lastname}', '{dob}', '{gender}', '{contact}', '{address}');"
            med.insertvalue(query)
            messagebox.showinfo("Success", "User added successfully.")
            self.new_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add user: {e}")

    def delete_user(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Delete User")
        self.new_window.geometry("300x200")

        frame = tk.Frame(self.new_window)
        frame.pack(pady=20)
        label = tk.Label(frame, text="Enter Aadhaar Card No to delete:")
        label.pack(side=tk.LEFT)
        self.aadhaar_entry = tk.Entry(frame)
        self.aadhaar_entry.pack(side=tk.RIGHT)

        delete_button = tk.Button(self.new_window, text="Delete", command=self.submit_delete_user)
        delete_button.pack(pady=20)

    def submit_delete_user(self):
        try:
            aadhaar = self.aadhaar_entry.get()
            query = f"DELETE FROM Aadhaar WHERE aadhar={aadhaar};"
            med.deletevalue(query)
            messagebox.showinfo("Success", "User deleted successfully.")
            self.new_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete user: {e}")

    def update_user(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Update User")
        self.new_window.geometry("400x400")

        fields = ['Aadhaar Card No', 'Field to Update (1. Name, 2. Last Name, 3. Date of Birth, 4. Gender, 5. Contact No, 6. Address)', 'New Value']
        self.entries = {}

        for field in fields:
            frame = tk.Frame(self.new_window)
            frame.pack(pady=5)
            label = tk.Label(frame, text=field)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.RIGHT)
            self.entries[field] = entry

        update_button = tk.Button(self.new_window, text="Update", command=self.submit_update_user)
        update_button.pack(pady=20)

    def submit_update_user(self):
        try:
            aadhaar = self.entries['Aadhaar Card No'].get()
            field_choice = int(self.entries['Field to Update (1. Name, 2. Last Name, 3. Date of Birth, 4. Gender, 5. Contact No, 6. Address)'].get())
            new_value = self.entries['New Value'].get()

            fields = ['first_name', 'last_name', 'dob', 'gender', 'contact_info', 'address']
            query = f"UPDATE Aadhaar SET {fields[field_choice - 1]} = '{new_value}' WHERE aadhar = {aadhaar};"
            med.updatevalue(query)
            messagebox.showinfo("Success", "User updated successfully.")
            self.new_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update user: {e}")

    def add_hospital(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add New Hospital")
        self.new_window.geometry("400x400")

        fields = ['Hospital Name', 'Hospital Address', 'Hospital Contact No']
        self.entries = {}

        for field in fields:
            frame = tk.Frame(self.new_window)
            frame.pack(pady=5)
            label = tk.Label(frame, text=field)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.RIGHT)
            self.entries[field] = entry

        submit_button = tk.Button(self.new_window, text="Submit", command=self.submit_hospital)
        submit_button.pack(pady=20)

    def submit_hospital(self):
        try:
            hospital_name = self.entries['Hospital Name'].get()
            hospital_address = self.entries['Hospital Address'].get()
            hospital_contact = self.entries['Hospital Contact No'].get()

            query = f"INSERT INTO Hospital_Details (hospital_name, location, contact_info) VALUES ('{hospital_name}', '{hospital_address}', '{hospital_contact}');"
            med.insertvalue(query)
            messagebox.showinfo("Success", "Hospital added successfully.")
            self.new_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add hospital: {e}")

    def delete_hospital(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Delete Hospital")
        self.new_window.geometry("300x200")

        frame = tk.Frame(self.new_window)
        frame.pack(pady=20)
        label = tk.Label(frame, text="Enter Hospital ID to delete:")
        label.pack(side=tk.LEFT)
        self.hospital_id_entry = tk.Entry(frame)
        self.hospital_id_entry.pack(side=tk.RIGHT)

        delete_button = tk.Button(self.new_window, text="Delete", command=self.submit_delete_hospital)
        delete_button.pack(pady=20)

    def submit_delete_hospital(self):
        try:
            hospital_id = self.hospital_id_entry.get()
            query = f"DELETE FROM Hospital_Details WHERE user_id={hospital_id};"
            med.deletevalue(query)
            messagebox.showinfo("Success", "Hospital deleted successfully.")
            self.new_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete hospital: {e}")

    def update_hospital(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Update Hospital")
        self.new_window.geometry("400x400")

        fields = ['Hospital ID', 'Field to Update (1. Name, 2. Address, 3. Contact No)', 'New Value']
        self.entries = {}

        for field in fields:
            frame = tk.Frame(self.new_window)
            frame.pack(pady=5)
            label = tk.Label(frame, text=field)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.RIGHT)
            self.entries[field] = entry

        update_button = tk.Button(self.new_window, text="Update", command=self.submit_update_hospital)
        update_button.pack(pady=20)

    def submit_update_hospital(self):
        try:
            hospital_id = self.entries['Hospital ID'].get()
            field_choice = int(self.entries['Field to Update (1. Name, 2. Address, 3. Contact No)'].get())
            new_value = self.entries['New Value'].get()

            fields = ['hospital_name', 'location', 'contact_info']
            query = f"UPDATE Hospital_Details SET {fields[field_choice - 1]} = '{new_value}' WHERE
