import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk  
import entry as pl
import src.med_reco as sqlcon

class MedicalRecordsApp:
    def __init__(self, root,prev_root):
        self.root = root
        self.prev_root = prev_root
        self.root.title("Medical Records Tracker")
        self.setup_admin_page()
    def setup_main_page(self):
        self.setup_admin_page()
    def setup_admin_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Admin Mode").pack()

        tk.Button(self.root, text="Add New User", command=self.add_new_user).pack()
        tk.Button(self.root, text="Delete User", command=self.delete_user).pack()
        tk.Button(self.root, text="Update User", command=self.update_user).pack()
        tk.Button(self.root, text="Add New Hospital", command=self.add_new_hospital).pack()
        tk.Button(self.root, text="Delete Hospital", command=self.delete_hospital).pack()
        tk.Button(self.root, text="Update Hospital", command=self.update_hospital).pack()
        tk.Button(self.root, text="Add New Doctor", command=self.add_new_doctor).pack()
        tk.Button(self.root, text="Delete Doctor", command=self.delete_doctor).pack()
        tk.Button(self.root, text="Update Doctor Working Hospital", command=self.update_doctor_hospital).pack()
        tk.Button(self.root, text="Display Mode", command=self.display_mode).pack()
        tk.Button(self.root, text="Logout", command=self.logout).pack()
    def logout(self):
        
        
        pl.MedicalRecordsApp(self.root)
    def add_new_user(self):
        aad = simpledialog.askinteger("Input", "Enter the aadhar card no.:")
        firstname = simpledialog.askstring("Input", "Enter the first name:")
        lastname = simpledialog.askstring("Input", "Enter the last name:")
        dob = simpledialog.askstring("Input", "Enter the date of Birth (yyyy-mm-dd):")
        gender = simpledialog.askstring("Input", "Enter the gender:")
        contact = simpledialog.askstring("Input", "Enter the contact no.:")
        address = simpledialog.askstring("Input", "Enter the residence address:")

        try:
            query = f"INSERT INTO Aadhaar (aadhar, first_name, last_name, dob, gender, contact_info, address) VALUES({aad}, '{firstname}', '{lastname}', '{dob}', '{gender}', '{contact}', '{address}');"
            sqlcon.insertvalue(query)
            messagebox.showinfo("Success", "User added successfully.")
        except:
            messagebox.showerror("Error", "Unable to add user.")

    def delete_user(self):
        aad = simpledialog.askinteger("Input", "Enter the aadhar card no. to delete:")
        try:
            query = f"DELETE FROM Aadhaar WHERE aadhar={aad};"
            sqlcon.deletevalue(query)
            messagebox.showinfo("Success", "User deleted successfully.")
        except:
            messagebox.showerror("Error", "Unable to delete user.")

    def update_user(self):
        aad = simpledialog.askinteger("Input", "Enter the aadhar card no. to update:")
        update_choice = simpledialog.askinteger("Input", "Enter the number of the detail to update:\n1. First Name\n2. Last Name\n3. Date of Birth\n4. Gender\n5. Contact Number\n6. Address")

        if update_choice == 1:
            new_value = simpledialog.askstring("Input", "Enter the new first name:")
            column = "first_name"
        elif update_choice == 2:
            new_value = simpledialog.askstring("Input", "Enter the new last name:")
            column = "last_name"
        elif update_choice == 3:
            new_value = simpledialog.askstring("Input", "Enter the new date of birth (yyyy-mm-dd):")
            column = "dob"
        elif update_choice == 4:
            new_value = simpledialog.askstring("Input", "Enter the new gender:")
            column = "gender"
        elif update_choice == 5:
            new_value = simpledialog.askstring("Input", "Enter the new contact number:")
            column = "contact_info"
        elif update_choice == 6:
            new_value = simpledialog.askstring("Input", "Enter the new address:")
            column = "address"
        else:
            messagebox.showerror("Error", "Invalid choice.")
            return

        try:
            query = f"UPDATE Aadhaar SET {column} = '{new_value}' WHERE aadhar = {aad};"
            sqlcon.updatevalue(query)
            messagebox.showinfo("Success", "User updated successfully.")
        except:
            messagebox.showerror("Error", "Unable to update user.")

    def add_new_hospital(self):
        hospital_name = simpledialog.askstring("Input", "Enter the hospital name:")
        hospital_address = simpledialog.askstring("Input", "Enter the hospital address:")
        hospital_contact = simpledialog.askstring("Input", "Enter the hospital contact number:")
        
        try:
            query = f"INSERT INTO Hospital_Details (hospital_name, location, contact_info) VALUES('{hospital_name}', '{hospital_address}', '{hospital_contact}');"
            sqlcon.insertvalue(query)
            messagebox.showinfo("Success", "Hospital added successfully.")
        except:
            messagebox.showerror("Error", "Unable to add hospital.")

    def delete_hospital(self):
        hospital_id = simpledialog.askinteger("Input", "Enter the hospital id to delete:")
        try:
            query = f"DELETE FROM Hospital_Details WHERE user_id={hospital_id};"
            sqlcon.deletevalue(query)
            messagebox.showinfo("Success", "Hospital deleted successfully.")
        except:
            messagebox.showerror("Error", "Unable to delete hospital.")

    def update_hospital(self):
        hospital_id = simpledialog.askinteger("Input", "Enter the hospital id to update:")
        update_choice = simpledialog.askinteger("Input", "Enter the number of the detail to update:\n1. Hospital Name\n2. Hospital Address\n3. Hospital Contact Number")

        if update_choice == 1:
            new_value = simpledialog.askstring("Input", "Enter the new hospital name:")
            column = "hospital_name"
        elif update_choice == 2:
            new_value = simpledialog.askstring("Input", "Enter the new hospital address:")
            column = "location"
        elif update_choice == 3:
            new_value = simpledialog.askstring("Input", "Enter the new hospital contact number:")
            column = "contact_info"
        else:
            messagebox.showerror("Error", "Invalid choice.")
            return

        try:
            query = f"UPDATE Hospital_Details SET {column} = '{new_value}' WHERE user_id = {hospital_id};"
            sqlcon.updatevalue(query)
            messagebox.showinfo("Success", "Hospital updated successfully.")
        except:
            messagebox.showerror("Error", "Unable to update hospital.")

    def add_new_doctor(self):
        doctor_id = simpledialog.askinteger("Input", "Enter the doctor's aadhar id:")
        try:
            query = f"SELECT first_name, last_name, contact_info FROM Aadhaar WHERE aadhar = {doctor_id};"
            result = sqlcon.qretiever(query)
            if result:
                first_name, last_name, contact_info = result[0]
                hospital_id = simpledialog.askinteger("Input", "Enter the hospital id:")
                specialization = simpledialog.askstring("Input", "Enter doctor's specialization:")
                query1 = f"INSERT INTO Doctors (first_name, last_name, hospital_id, contact_info, specialization, aadhar_number) VALUES('{first_name}', '{last_name}', {hospital_id}, '{contact_info}', '{specialization}', {doctor_id});"
                sqlcon.insertvalue(query1)
                messagebox.showinfo("Success", "Doctor added successfully.")
            else:
                messagebox.showerror("Error", "Doctor not found in Aadhaar database.")
        except:
            messagebox.showerror("Error", "Unable to retrieve doctor information.")

    def delete_doctor(self):
        doctor_id = simpledialog.askinteger("Input", "Enter the doctor id to delete:")
        try:
            query = f"DELETE FROM Doctors WHERE doctor_id = {doctor_id};"
            sqlcon.deletevalue(query)
            messagebox.showinfo("Success", "Doctor deleted successfully.")
        except:
            messagebox.showerror("Error", "Unable to delete doctor.")

    def update_doctor_hospital(self):
        doctor_id = simpledialog.askinteger("Input", "Enter the doctor id:")
        new_hospital_id = simpledialog.askinteger("Input", "Enter the new hospital id:")
        try:
            query = f"UPDATE Doctors SET hospital_id = {new_hospital_id} WHERE doctor_id = {doctor_id};"
            sqlcon.updatevalue(query)
            messagebox.showinfo("Success", "Doctor's hospital updated successfully.")
        except:
            messagebox.showerror("Error", "Unable to update doctor's hospital.")

    def display_mode(self):
        display_choice = simpledialog.askinteger("Input", "Enter the number of the detail to display:\n1. All Doctors\n2. All Users\n3. All Hospitals")
        
        if display_choice == 1:
            query = "SELECT * FROM Doctors;"
        elif display_choice == 2:
            query = "SELECT * FROM Aadhaar;"
        elif display_choice == 3:
            query = "SELECT * FROM Hospital_Details;"
        else:
            messagebox.showerror("Error", "Invalid choice.")
            return
        
        try:
            result = sqlcon.qretiever(query)
            
            display_text = "\n".join(str(record) for record in result)
            messagebox.showinfo("Display", display_text)
        except:
            messagebox.showerror("Error", "Unable to display information.")
def main(root1):
    root = root1
    root.wm_minsize(960,640)
    app = MedicalRecordsApp(root,root1)
    root.mainloop()



