-- Insert sample data into Aadhaar table for doctors
INSERT INTO Aadhaar (aadhar, first_name, last_name, dob, gender, contact_info, address) VALUES
(200000000001, 'James', 'Brown', '1975-03-22', 'Male', 'james.brown@example.com', '101 Elm Street, Springfield'),
(200000000002, 'Michael', 'Johnson', '1980-04-15', 'Male', 'michael.johnson@example.com', '202 Maple Street, Springfield'),
(200000000003, 'Linda', 'Williams', '1985-05-10', 'Female', 'linda.williams@example.com', '303 Oak Street, Springfield'),
(200000000004, 'Robert', 'Jones', '1978-06-30', 'Male', 'robert.jones@example.com', '404 Pine Street, Springfield'),
(200000000005, 'Patricia', 'Davis', '1982-07-25', 'Female', 'patricia.davis@example.com', '505 Birch Street, Springfield'),
(200000000006, 'Thomas', 'Miller', '1974-08-19', 'Male', 'thomas.miller@example.com', '606 Cedar Street, Springfield'),
(200000000007, 'Sarah', 'Garcia', '1981-09-14', 'Female', 'sarah.garcia@example.com', '707 Dogwood Street, Springfield'),
(200000000008, 'Christopher', 'Martinez', '1976-10-09', 'Male', 'christopher.martinez@example.com', '808 Elm Street, Springfield'),
(200000000009, 'Jessica', 'Rodriguez', '1983-11-04', 'Female', 'jessica.rodriguez@example.com', '909 Fir Street, Springfield'),
(200000000010, 'Daniel', 'Lewis', '1979-12-01', 'Male', 'daniel.lewis@example.com', '1010 Gum Street, Springfield');

-- Insert corresponding user logins into Users table
INSERT INTO Users (aadhar, password) VALUES
(200000000001, 'docpassword1'),
(200000000002, 'docpassword2'),
(200000000003, 'docpassword3'),
(200000000004, 'docpassword4'),
(200000000005, 'docpassword5'),
(200000000006, 'docpassword6'),
(200000000007, 'docpassword7'),
(200000000008, 'docpassword8'),
(200000000009, 'docpassword9'),
(200000000010, 'docpassword10');

-- Insert sample data into Doctors table
INSERT INTO Doctors (first_name, last_name, specialization, contact_info, aadhar, hospital_id) VALUES
('James', 'Brown', 'Cardiologist', 'james.brown@example.com', 200000000001, 1),
('Michael', 'Johnson', 'Neurologist', 'michael.johnson@example.com', 200000000002, 2),
('Linda', 'Williams', 'Dermatologist', 'linda.williams@example.com', 200000000003, 3),
('Robert', 'Jones', 'Orthopedic Surgeon', 'robert.jones@example.com', 200000000004, 4),
('Patricia', 'Davis', 'Pediatrician', 'patricia.davis@example.com', 200000000005, 5),
('Thomas', 'Miller', 'General Practitioner', 'thomas.miller@example.com', 200000000006, 6),
('Sarah', 'Garcia', 'Oncologist', 'sarah.garcia@example.com', 200000000007, 7),
('Christopher', 'Martinez', 'Psychiatrist', 'christopher.martinez@example.com', 200000000008, 8),
('Jessica', 'Rodriguez', 'Endocrinologist', 'jessica.rodriguez@example.com', 200000000009, 9),
('Daniel', 'Lewis', 'Gastroenterologist', 'daniel.lewis@example.com', 200000000010, 10);
