-- Create the healthrecord database
CREATE DATABASE healthrecord;
USE healthrecord;

-- Create Aadhaar table for user details
CREATE TABLE Aadhaar (
    aadhar bigint(12) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE,
    gender VARCHAR(10),
    contact_info VARCHAR(100),
    address TEXT
);

-- Create Hospital_Details table
CREATE TABLE Hospital_Details (
    user_id bigint AUTO_INCREMENT PRIMARY KEY,
    hospital_name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    contact_info VARCHAR(100)
    
);

-- Create Users table for login
CREATE TABLE Users (
    aadhar bigint(12) PRIMARY KEY, -- Aadhaar card number for user login
    password VARCHAR(100) NOT NULL,
    FOREIGN KEY (aadhar) REFERENCES Aadhaar(aadhar) ON DELETE CASCADE
);

-- Create Hospitals table for login
CREATE TABLE Hospitals (
    login_id bigint  PRIMARY KEY,
    password VARCHAR(100) NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    FOREIGN KEY (login_id) REFERENCES Hospital_Details(user_id) ON DELETE CASCADE
);

-- Create Admins table for login
CREATE TABLE Admins (
    username VARCHAR(100) PRIMARY KEY UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    aadhar bigint(12) UNIQUE NOT NULL,
    FOREIGN KEY (aadhar) REFERENCES Aadhaar(aadhar) ON DELETE CASCADE
);


-- Create Diseases table
CREATE TABLE Diseases (
    disease_id bigint AUTO_INCREMENT PRIMARY KEY,
    disease_name VARCHAR(100) NOT NULL
);

-- Create Drugs table
CREATE TABLE Drugs (
    drug_id bigint AUTO_INCREMENT PRIMARY KEY,
    drug_name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Create Doctors table
CREATE TABLE Doctors (
    doctor_id bigint AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    contact_info VARCHAR(100),
    aadhar_number bigint(12) UNIQUE NOT NULL,
    hospital_id bigint NOT NULL,
    FOREIGN KEY (aadhar_number) REFERENCES Aadhaar(aadhar) ON DELETE CASCADE,
    FOREIGN KEY (hospital_id) REFERENCES Hospital_Details(user_id) ON DELETE CASCADE
);

-- Create Currently_Under_Treatment table
CREATE TABLE Currently_Under_Treatment (
    currently_under_treatment_id bigint AUTO_INCREMENT PRIMARY KEY,
    patient_id bigint(12) NOT NULL,
    hospital_id bigint NOT NULL,
    disease_id bigint NOT NULL,
    start_date DATE NOT NULL,
    drugs_taken TEXT,
    FOREIGN KEY (patient_id) REFERENCES Aadhaar(aadhar) ON DELETE CASCADE,
    FOREIGN KEY (hospital_id) REFERENCES Hospital_Details(user_id) ON DELETE CASCADE,
    FOREIGN KEY (disease_id) REFERENCES Diseases(disease_id) ON DELETE CASCADE
);

-- Create Recovered_People table
CREATE TABLE Recovered_People (
    recovered_people_id bigint AUTO_INCREMENT PRIMARY KEY,
    patient_id bigint(12) NOT NULL,
    hospital_id bigint NOT NULL,
    disease_id bigint NOT NULL,
    start_date DATE NOT NULL,
    recovery_date DATE NOT NULL,
    drugs_taken TEXT,
    FOREIGN KEY (patient_id) REFERENCES Aadhaar(aadhar) ON DELETE CASCADE,
    FOREIGN KEY (hospital_id) REFERENCES Hospital_Details(user_id) ON DELETE CASCADE,
    FOREIGN KEY (disease_id) REFERENCES Diseases(disease_id) ON DELETE CASCADE
);