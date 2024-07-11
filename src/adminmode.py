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
            aad=input("Enter the aadhar card no. to delete:")
            
            
            
            