use healthrecord;
select * from aadhaar;
INSERT INTO `healthrecord`.`aadhaar`
(`aadhar`,
`first_name`,
`last_name`,
`dob`,
`gender`,
`contact_info`,
`address`)
VALUES
(123456789012,
'adarsh',
'clocke',
'2003-09-18',
'male',
623554226,
"idk where");
INSERT INTO `healthrecord`.`admins`
(`username`,
`password`,
`aadhar`)
VALUES
('adarsh',
'password123',
123456789012);



