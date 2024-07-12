import src.med_reco as user

def main(id):
    q=f"SELECT * FROM Aadhaar WHERE aadhar={id};"
    profile = user.qretiever(f"SELECT * FROM Aadhaar WHERE aadhar={id};")
    past_treatments = user.qretiever(f"SELECT * FROM Recovered_People WHERE patient_id={id};")
    present_treatments = user.qretiever(f"SELECT * FROM Currently_Under_Treatment WHERE patient_id={id};")

    while True:
        print("========================================")
        print("Welcome to the Medical Record System - User")
        print("========================================")
        print("PROFILE:")
        
        user.display(q)
        print("========================================")
        print("1. Show all treatments")
        print("2. Show present undergoing treatments")
        print("3. Delete a patient's record")
        print("4. Logout")
        print("5. Exit")
        print("========================================")
        choice = int(input("Enter your choice: "))
        print("========================================")

        if choice == 1:
            print("Past treatments:")
            print(past_treatments)
            print("Present treatments:")
            print(present_treatments)
        elif choice == 2:
            print("Present treatments:")
            print(present_treatments)
        elif choice == 3:
            print("Enter the id of the record of the treatment you want to delete. (Allowed to delete only past treatments)")
            treatment_id = int(input("Enter the id: "))
            query=f"DELETE FROM Recovered_People WHERE recovered_people_id={treatment_id};"
            user.deletevalue(query)
            print("Record deleted successfully!")
        elif choice == 4:
            print("Logging out...")
            return
            break
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")