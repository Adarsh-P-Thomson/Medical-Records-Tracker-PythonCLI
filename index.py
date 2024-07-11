import src.med_reco as sqlcon
import src.usermode as userer
import src.hospitalmode as hos
import src.adminmode as adm

while True:
    print("======================================")
    print("WELCOME TO MEDICAL RECORDS TRACKER:")
    print("======================================")
    print("Enter the mode of entry:")
    print("1.USER MODE")
    print("2.HOSPITAL MODE")
    print("3.ADMIN MODE")
    print("4.EXIT")
    mode = int(input("Enter the mode: "))

    if mode == 1:  # user mode
        print("=======================================")
        id = int(input("Enter your Aadhar card no.: "))
        password = input("Enter your Password: ")
        if sqlcon.qretiever(f"SELECT password FROM Users WHERE aadhar={id};")[0] == password:
            userer.main(id)
        else:
            print("Invalid Credentials")
    elif mode == 2:  # hospital login
        print("=======================================")
        username = input("Enter Hospital username: ")
        id = int(input("Enter your Hospital id no.: "))
        password = input("Enter your Password: ")
        if sqlcon.qretiever(f"SELECT password FROM Hospitals WHERE login_id={id} AND username={username};")[0] == password:
            hos.main(id)
        else:
            print("Invalid Credentials")
    elif mode == 3:  # admin login
        print("=======================================")
        username = input("Enter Admin username: ")
        id = int(input("Enter your Admin Aadhar id no.: "))
        password = input("Enter your Password: ")
        if sqlcon.qretiever(f"SELECT password FROM Admins WHERE aadhar={id} AND username={username};")[0] == password:
            adm.main(id, username)
        else:
            print("Invalid Credentials")
    elif mode == 4:
        print("=======================================")
        print("\nThank you for using our service")
        break
    else:
        print("\nInvalid mode entered")