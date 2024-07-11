
import src.med_reco as user
def main(id):
    profile=user.qretiever(f"SELECT * FROM Aadhaar WHERE aadhar={id};")
    pastreat=user.qretiever(f"SELECT * FROM Recovered_People WHERE patient_id={id};")
    pretreat=user.qretiever(f"SELECT * FROM Currently_Under_Treatment WHERE patient_id={id};")
    while True:
        print("========================================")
        print("Welcome to the Medical Record System -User")
        print("========================================")
        print("PROFILE:")
        print (profile)
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
            print(pastreat)
            print(pretreat)
        elif choice==2:
            print(pretreat)
        elif choice==3:
            print("Enter the id of the record of the treatment you want to delete.(Allowed to delete only past treatments)")
            id=int(input("Enter the id:"))
            user.qretiever(f"DELETE FROM Recovered_People WHERE recovered_people_id={id}")