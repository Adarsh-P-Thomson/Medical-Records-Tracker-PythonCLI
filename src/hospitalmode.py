import src.med_reco as user

def main(id):
    profile = user.query_retriever(f"SELECT * FROM Hospital_Details WHERE user_id={id};")
    past_treatments = user.query_retriever(f"SELECT * FROM Recovered_People WHERE hospital_id={id};")
    current_treatments = user.query_retriever(f"SELECT * FROM Currently_Under_Treatment WHERE hospital_id={id};")

    while True:
        print_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print_past_treatments(past_treatments)
        elif choice == 2:
            print_current_treatments(current_treatments)
        elif choice == 3:
            delete_patient_record(id, past_treatments)
        elif choice == 4:
            add_new_patient(id)
        elif choice == 5:
            return
        elif choice == 6:
            exit()

def print_menu():
    print("========================================")
    print("Welcome to the Medical Record System -HOSPITAL")
    print("========================================")
    print("1. Show all past treatments")
    print("2. Show present undergoing treatments")
    print("3. Delete a patient's record")
    print("4. Add a new patient")
    print("5. Logout")
    print("6. Exit")
    print("========================================")

def print_past_treatments(past_treatments):
    print("Past Treatments:")
    print(past_treatments)

def print_current_treatments(current_treatments):
    print("Current Treatments:")
    print(current_treatments)

def delete_patient_record(id, past_treatments):
    print("Enter the id of the record of the treatment you want to delete.")
    print(past_treatments)
    record_id = int(input("Enter the id: "))
    query=f"DELETE FROM Recovered_People WHERE recovered_people_id={record_id};"
    user.query_retriever(query)

def add_new_patient(id):
    patient_id = int(input("Enter the id of the patient: "))
    disease_id = int(input("Enter the disease id the Patient is suffering from: "))
    drugs_taken = input("Enter the drugs taken for treatment: ")
    start_date = input("Enter treatment start date (yyyy-mm-dd): ")
    treatment_status = input("Enter 1 if still under treatment or 2 if has recovered: ")

    if treatment_status == "1":
        query=f"INSERT INTO Currently_Under_Treatment (hospital_id, patient_id, start_date, drugs_taken) VALUES ({id}, {patient_id}, '{start_date}', '{drugs_taken}');"
        user.qretiever(query)
    else:
        end_date = input("Enter treatment end date (yyyy-mm-dd): ")
        query=f"INSERT INTO Recovered_People (hospital_id, patient_id, start_date, recovery_date, drugs_taken) VALUES ({id}, {patient_id}, '{start_date}', '{end_date}', '{drugs_taken}');"
        user.qretriever(query)