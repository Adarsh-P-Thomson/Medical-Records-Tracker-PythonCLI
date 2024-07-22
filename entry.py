import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk  # You need to install Pillow for handling images

import src.med_reco as sqlcon
# import src.usermode as userer
# import src.hospitalmode as hos
# import src.adminmode as adm

class MedicalRecordsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Records Tracker")
        
        self.setup_main_page()

    def setup_main_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Add logo
        logo = Image.open("logo.png")
        logo = logo.resize((200, 200), Image.LANCZOS)
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(self.root, image=logo)
        logo_label.image = logo  # Keep a reference!
        logo_label.pack(pady=20)

        # User mode
        tk.Label(self.root, text="User Mode").pack()
        self.user_id_entry = tk.Entry(self.root)
        self.user_id_entry.pack()
        self.user_password_entry = tk.Entry(self.root, show='*')
        self.user_password_entry.pack()
        tk.Button(self.root, text="Login as User", command=self.on_user_mode).pack()

        # Hospital mode
        tk.Label(self.root, text="Hospital Mode").pack()
        self.hospital_username_entry = tk.Entry(self.root)
        self.hospital_username_entry.pack()
        self.hospital_id_entry = tk.Entry(self.root)
        self.hospital_id_entry.pack()
        self.hospital_password_entry = tk.Entry(self.root, show='*')
        self.hospital_password_entry.pack()
        tk.Button(self.root, text="Login as Hospital", command=self.on_hospital_mode).pack()

        # Admin mode
        tk.Label(self.root, text="Admin Mode").pack()
        self.admin_username_entry = tk.Entry(self.root)
        self.admin_username_entry.pack()
        self.admin_id_entry = tk.Entry(self.root)
        self.admin_id_entry.pack()
        self.admin_password_entry = tk.Entry(self.root, show='*')
        self.admin_password_entry.pack()
        tk.Button(self.root, text="Login as Admin", command=self.on_admin_mode).pack()

    def on_user_mode(self):
        id = self.user_id_entry.get()
        password = self.user_password_entry.get()
        self.authenticate_user(id, password)

    def on_hospital_mode(self):
        username = self.hospital_username_entry.get()
        id = self.hospital_id_entry.get()
        password = self.hospital_password_entry.get()
        self.authenticate_hospital(username, id, password)

    def on_admin_mode(self):
        username = self.admin_username_entry.get()
        id = self.admin_id_entry.get()
        password = self.admin_password_entry.get()
        self.authenticate_admin(username, id, password)

    def authenticate_user(self, id, password):
        query = f"SELECT password FROM Users WHERE aadhar = {id};"
        try:
            if sqlcon.qretiever(query)[0][0] == password:
                self.setup_user_mode(id)
            else:
                messagebox.showerror("Error", "Invalid Credentials")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def authenticate_hospital(self, username, id, password):
        query = f"SELECT password FROM Hospitals WHERE login_id={id} AND username='{username}';"
        try:
            if sqlcon.qretiever(query)[0][0] == password:
                self.setup_hospital_mode(id)
            else:
                messagebox.showerror("Error", "Invalid Credentials")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def authenticate_admin(self, username, id, password):
        query = f"SELECT password FROM Admins WHERE aadhar={id} AND username='{username}';"
        try:
            if sqlcon.qretiever(query)[0][0] == password:
                adm.main()
            else:
                messagebox.showerror("Error", "Invalid Credentials")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def setup_user_mode(self, id):
        for widget in self.root.winfo_children():
            widget.destroy()

        def logout():
            self.setup_main_page()

        def show_all_treatments():
            past_treatments = sqlcon.qretiever(f"SELECT * FROM Recovered_People WHERE patient_id={id};")
            present_treatments = sqlcon.qretiever(f"SELECT * FROM Currently_Under_Treatment WHERE patient_id={id};")
            messagebox.showinfo("Past Treatments", past_treatments)
            messagebox.showinfo("Present Treatments", present_treatments)

        def show_present_treatments():
            present_treatments = sqlcon.qretiever(f"SELECT * FROM Currently_Under_Treatment WHERE patient_id={id};")
            messagebox.showinfo("Present Treatments", present_treatments)

        def delete_record():
            treatment_id = simpledialog.askinteger("Input", "Enter the id of the treatment to delete:")
            query = f"DELETE FROM Recovered_People WHERE recovered_people_id={treatment_id};"
            sqlcon.deletevalue(query)
            messagebox.showinfo("Success", "Record deleted successfully!")

        tk.Label(self.root, text="User Mode").pack()
        tk.Button(self.root, text="Show All Treatments", command=show_all_treatments).pack()
        tk.Button(self.root, text="Show Present Treatments", command=show_present_treatments).pack()
        tk.Button(self.root, text="Delete a Treatment Record", command=delete_record).pack()
        tk.Button(self.root, text="Logout", command=logout).pack()

    def setup_hospital_mode(self, id):
        for widget in self.root.winfo_children():
            widget.destroy()

        def logout():
            self.setup_main_page()

        def show_past_treatments():
            past_treatments = sqlcon.qretiever(f"SELECT * FROM Recovered_People WHERE hospital_id={id};")
            messagebox.showinfo("Past Treatments", past_treatments)

        def show_present_treatments():
            current_treatments = sqlcon.qretiever(f"SELECT * FROM Currently_Under_Treatment WHERE hospital_id={id};")
            messagebox.showinfo("Current Treatments", current_treatments)

        def delete_record():
            treatment_id = simpledialog.askinteger("Input", "Enter the id of the treatment to delete:")
            query = f"DELETE FROM Recovered_People WHERE recovered_people_id={treatment_id};"
            sqlcon.deletevalue(query)
            messagebox.showinfo("Success", "Record deleted successfully!")

        def add_new_patient():
            patient_id = simpledialog.askinteger("Input", "Enter the id of the patient:")
            disease_id = simpledialog.askinteger("Input", "Enter the disease id the Patient is suffering from:")
            drugs_taken = simpledialog.askstring("Input", "Enter the drugs taken for treatment:")
            start_date = simpledialog.askstring("Input", "Enter treatment start date (yyyy-mm-dd):")
            treatment_status = simpledialog.askinteger("Input", "Enter 1 if still under treatment or 2 if has recovered:")

            if treatment_status == 1:
                query = f"INSERT INTO Currently_Under_Treatment (hospital_id, patient_id, start_date, drugs_taken) VALUES ({id}, {patient_id}, '{start_date}', '{drugs_taken}');"
                sqlcon.qretiever(query)
            else:
                end_date = simpledialog.askstring("Input", "Enter treatment end date (yyyy-mm-dd):")
                query = f"INSERT INTO Recovered_People (hospital_id, patient_id, start_date, recovery_date, drugs_taken) VALUES ({id}, {patient_id}, '{start_date}', '{end_date}', '{drugs_taken}');"
                sqlcon.qretiever(query)
            messagebox.showinfo("Success", "Patient added successfully!")

        tk.Label(self.root, text="Hospital Mode").pack()
        tk.Button(self.root, text="Show Past Treatments", command=show_past_treatments).pack()
        tk.Button(self.root, text="Show Present Treatments", command=show_present_treatments).pack()
        tk.Button(self.root, text="Delete a Treatment Record", command=delete_record).pack()
        tk.Button(self.root, text="Add a New Patient", command=add_new_patient).pack()
        tk.Button(self.root, text="Logout", command=logout).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalRecordsApp(root)
    root.mainloop()
