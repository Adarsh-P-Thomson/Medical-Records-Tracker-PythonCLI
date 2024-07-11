import src.med_reco as med
def main():
    #this function is main handler of admin mode 
    choice=15
    stat=True
    i=0
    while stat:
        print("======================================")
        print("Welcome to Admin Mode")
        print("======================================")
        print("1. Add new user")
        print("2. Delete user")
        print("3. Update user")
        print("4. Add new hospital")
        print("5. Delete hospital")
        print("6. Update hospital")
        print("7. Add new doctor")
        print("8. Delete doctor")
        print("9. Update doctor")
        print("10. Add new patient")
        print("11. Delete patient")
        print("12. Update patient")
        print("13. Logout")
        print("14. Exit")
        print("======================================")
        choice = int(input("Enter your choice: "))
        if choice not in ( i in range (1,15)):
            print("Invalid choice")
            continue
        if choice == 1:
            aad=input("Enter the aadhar card no.:")
            firstname=input("Enter the name:")
            lastname=input("Enter the last name:")
            dob=input("Enter the date of Birth:(yyyy-mm-dd):")
            gender=input("Enter the gender:")
            contact=int(input("Enter the contact no.:"))
            address=input("Enter the residence address:")
            try:
                med.insertvalue(f"INSERT INTO Aadhar (aadhar,first_name,last_name,dob,gender,contact_info,address)
                            VALUES({aad},{firstname},{lastname},{dob},{gender},{contact},{address});")
            except:
                print("Error")
                continue
            print("User Added sucessfully.")
        
        elif choice == 2:
            aad=int(input("Enter the aadhar card no. to delete:"))
            try:
                med.deletevalue(f"DELETE FROM Aadhar WHERE aadhar={aad}")
            except:
                print("Error! Unable to Delete")
        elif choice==3:
            print("Enter what data would you like to change:")
            print("1.Name")
            print("2.Last Name")
            print("3.Date of Birth")
            print("4.Gender")
            print("5.Contact Number")
            print("6.Address")
            choice_update = int(input("Enter your choice: "))
            aad = int(input("Enter the aadhar card no. to update: "))
            if choice_update == 1:
                new_name = input("Enter the new name: ")
                try:
                    med.updatevalue(f"UPDATE Aadhar SET first_name = '{new_name}' WHERE aadhar = {aad}")
                except:
                    print("Error! Unable to Update")
            elif choice_update == 2:
                new_lastname = input("Enter the new last name: ")
                try:
                    med.updatevalue(f"UPDATE Aadhar SET last_name = '{new_lastname}' WHERE aadhar = {aad}")
                except:
                    print("Error! Unable to Update")
            elif choice_update == 3:
                new_dob = input("Enter the new date of birth (yyyy-mm-dd): ")
                try:
                    med.updatevalue(f"UPDATE Aadhar SET dob = '{new_dob}' WHERE aadhar = {aad}")
                except:
                    print("Error! Unable to Update")
            elif choice_update == 4:
                new_gender = input("Enter the new gender: ")
                try:
                    med.updatevalue(f"UPDATE Aadhar SET gender = '{new_gender}' WHERE aadhar = {aad}")
                except:
                    print("Error! Unable to Update")
            elif choice_update == 5:
                new_contact = int(input("Enter the new contact number: "))
                try:
                    med.updatevalue(f"UPDATE Aadhar SET contact_info = {new_contact} WHERE aadhar = {aad}")
                except:
                    print("Error! Unable to Update")
            elif choice_update == 6:
                new_address = input("Enter the new address: ")
                try:
                    med.updatevalue(f"UPDATE Aadhar SET address = '{new_address}' WHERE aadhar = {aad}")
                except:
                    print("Error! Unable to Update")
            else:
                print("Invalid choice")
        
        elif choice == 4:
            hospital_id = int(input("Enter the hospital id: "))
            hospital_name = input("Enter the hospital name: ")
            try:
                med.insertvalue(f"INSERT INTO Hospital (hospital_id, hospital_name) VALUES ({hospital_id}, '{hospital_name}')")
            except:
                print("Error")
                continue
            print("Hospital Added successfully.")
        
        elif choice == 5:
            hospital_id = int(input("Enter the hospital id to delete: "))
            try:
                med.deletevalue(f"DELETE FROM Hospital WHERE hospital_id = {hospital_id}")
            except:
                print("Error! Unable to Delete")
        
        elif choice == 6:
            print("Enter what data would you like to change: ")
            print("1.Hospital Name")
            choice_update = int(input("Enter your choice: "))
            hospital_id = int(input("Enter the hospital id to update: "))
            if choice_update == 1:
                new_hospital_name = input("Enter the new hospital name: ")
                try:
                    med.updatevalue(f"UPDATE Hospital SET hospital_name = '{new_hospital_name}' WHERE hospital_id = {hospital_id}")
                except:
                    print("Error! Unable to Update")
            else:
                print("Invalid choice")
        
        elif choice == 7:
            doctor_id = int(input("Enter the doctor id: "))
            doctor_name = input("Enter the doctor name: ")
            hospital_id = int(input("Enter the hospital id: "))
            try:
                med.insertvalue(f"INSERT INTO Doctor (doctor_id, doctor_name, hospital_id) VALUES ({doctor_id}, '{doctor_name}', {hospital_id})")
            except:
                print("Error")
                continue
            print("Doctor Added successfully.")
        
        elif choice == 8:
            doctor_id = int(input("Enter the doctor id to delete: "))
            try:
                med.deletevalue(f"DELETE FROM Doctor WHERE doctor_id = {doctor_id}")
            except:
                print("Error! Unable to Delete")
        
        elif choice == 9:
            print("Enter what data would you like to change: ")
            print("1.Doctor Name")
            print("2.Hospital ID")
            choice_update = int(input("Enter your choice: "))
            doctor_id = int(input("Enter the doctor id to update: "))
            if choice_update == 1:
                new_doctor_name = input("Enter the new doctor name: ")
                try:
                    med.updatevalue(f"UPDATE Doctor SET doctor_name = '{new_doctor_name}' WHERE doctor_id = {doctor_id}")
                except:
                    print("Error! Unable to Update")
            elif choice_update == 2:
                new_hospital_id = int(input("Enter the new hospital id:"))
                try:
                    med.updatevalue(f"UPDATE Doctor SET hospital_id = {new_hospital_id} WHERE doctor_id = {doctor_id}")
                except:
                    print("Error! Unable to Update")
            else:
                print("Invalid choice")
        
        elif choice == 10:
            patient_id = int(input("Enter the patient id: "))
            patient_name = input("Enter the patient name: ")
            doctor_id = int(input("Enter the doctor id: "))
            try:
                med.insertvalue(f"INSERT INTO Patient (patient_id, patient_name, doctor_id) VALUES ({patient_id}, '{patient_name}', {doctor_id})")
            except:
                print("Error")
                continue
            print("Patient Added successfully.")
        
        elif choice == 11:
            patient_id = int(input("Enter the patient id to delete: "))
            try:
                med.deletevalue(f"DELETE FROM Patient WHERE patient_id = {patient_id}")
            except:
                print("Error! Unable to Delete")
        
        elif choice == 12:
            print("Enter what data would you like to change: ")
            print("1.Patient Name")
            print("2.Doctor ID")
            choice_update = int(input("Enter your choice: "))
            patient_id = int(input("Enter the patient id to update: "))
            if choice_update == 1:
                new_patient_name = input("Enter the new patient name: ")
                try:
                    med.updatevalue(f"UPDATE Patient SET patient_name = '{new_patient_name}' WHERE patient_id = {patient_id}")
                except:
                    print("Error! Unable to Update")
            elif choice_update == 2:
                new_doctor_id = int(input("Enter the new doctor id: "))
                try:
                    med.updatevalue(f"UPDATE Patient SET doctor_id = {new_doctor_id} WHERE patient_id = {patient_id}")
                except:
                    print("Error! Unable to Update")
            else:
                print("Invalid choice")
        
        elif choice == 13:
            print("Logging out...")
            stat = False
            return
        
        elif choice == 14:
            print("Exiting...")
            stat = False
            exit()
        
        else:
            print("Invalid choice")
