drop_hike = "DROP TABLE IF EXISTS HIKE"
create_hike = """CREATE TABLE HIKE(
hr_id INTEGER,
letter_date date NOT NULL,
emp_id varchar(20) NOT NULL,
emp_name varchar(20) NOT NULL,
emp_designation varchar(20) NOT NULL,
emp_ctc float NOT NULL,
effective_date date NOT NULL
)"""
insert_hike = "INSERT INTO HIKE VALUES(1,'Soham Parekh','2021-01-01','ABCDE','Engineer',5.1,'2021-01-02')"
select_hike = "SELECT * FROM HIKE"


drop_offer = "DROP TABLE IF EXISTS OFFER"
create_offer = """CREATE TABLE OFFER(
hr_id INTEGER ,
letter_date date NOT NULL,
emp_address varchar(100) NOT NULL,
emp_name varchar(20) NOT NULL,
emp_designation varchar(20) NOT NULL,
joining_date date NOT NULL,
emp_ctc float NOT NULL
)"""
insert_offer = "INSERT INTO OFFER VALUES(1,'2021-01-01','RANDOM ADDRESS','Soham Parekh','Engineer','2021-01-02',7.5)"
select_offer = "SELECT * FROM OFFER"

drop_relieve = "DROP TABLE IF EXISTS RELIEVE"
create_relieve = """CREATE TABLE RELIEVE(
hr_id INTEGER ,
curr_date date NOT NULL,
emp_name varchar(20) NOT NULL,
emp_id varchar(20) NOT NULL,
letter_date date NOT NULL,
resig_date date NOT NULL
)"""
insert_relieve = "INSERT INTO RELIEVE VALUES(1,'2021-01-01','Soham Parekh',1,'2021-01-02','2021-01-03')"
select_relieve = "SELECT * FROM RELIEVE"

drop_resign = "DROP TABLE IF EXISTS EMPLOYEE"
create_resign = """CREATE TABLE EMPLOYEE(
hr_id INTEGER,
emp_id varchar(20) NOT NULL,
emp_name varchar(20) NOT NULL,
emp_designation varchar(20) NOT NULL,
emp_dept varchar(20) NOT NULL,
emp_gender varchar(20) NOT NULL,
emp_pan varchar(20) NOT NULL,
emp_dob date NOT NULL,
emp_father varchar(20) NOT NULL,
emp_qualification varchar(20) NOT NULL,
emp_perm_address varchar(100) NOT NULL,
emp_curr_address varchar(100) NOT NULL,
emp_email varchar(50) NOT NULL,
emp_phone varchar(50) NOT NULL,
emp_whatsapp varchar(50) NOT NULL,
emp_referrer varchar(50) NOT NULL,
emp_institute varchar(50) NOT NULL,
offer_date date NOT NULL,
offer_desig varchar(50) NOT NULL,
offer_ctc float NOT NULL,
resig_date date NOT NULL,
company_name varchar(50) NOT NULL,
tech varchar(50) NOT NULL,
new_company varchar(50) NOT NULL,
bank_acc varchar(50) NOT NULL,
join_date date NOT NULL,
curr_desig varchar(50) NOT NULL,
curr_ctc float NOT NULL,
rel_date date NOT NULL,
location varchar(50) NOT NULL,
pf_acc varchar(50) NOT NULL,
bank_name varchar(50) NOT NULL
)"""
insert_resign = """INSERT INTO EMPLOYEE VALUES(
1,
"EQDPP",
'Soham Parekh',
'SE',
'COMP',
'M',
'PAN',
'23-06-2000',
'Dad',
'BTech',
'Address',
'Address',
'Email',
'1234',
'1234',
'refer',
'COEP',
'2021-01-01',
'Engineer',
3.2,
'2021-01-01',
'Company blah',
'Python',
'New Company',
'12345',
'2021-01-01',
'Engineer',
1.9,
'2021-01-01',
'Pune',
'1234',
'SBI')"""
select_resign = "SELECT * FROM EMPLOYEE"

drop_experience = "DROP TABLE IF EXISTS EXPERIENCE"
create_experience = """CREATE TABLE EXPERIENCE(
hr_id INTEGER ,
curr_date date NOT NULL,
emp_name varchar(20) NOT NULL,
emp_id varchar(20) NOT NULL,
emp_designation varchar(20) NOT NULL,
emp_dept varchar(20) NOT NULL,
join_date date NOT NULL,
leave_date date NOT NULL
)"""
insert_experience = "INSERT INTO EXPERIENCE VALUES(1,'2021-01-01','Soham Parekh',1,'Engineer','Security','2021-01-02','2021-01-03')"
select_experience = "SELECT * FROM EXPERIENCE"

drop_payslip = "DROP TABLE IF EXISTS PAYSLIP"
create_payslip = """CREATE TABLE PAYSLIP(
hr_id INTEGER ,
letter_month varchar(20) NOT NULL,
letter_year varchar(20) NOT NULL,
emp_name varchar(20) NOT NULL,
emp_id varchar(20) NOT NULL,
emp_band varchar(20) NOT NULL,
emp_dept varchar(20) NOT NULL,
emp_designation varchar(20) NOT NULL,
emp_dob date NOT NULL,
emp_pan varchar(20) NOT NULL,
emp_doj date NOT NULL,
location varchar(20) NOT NULL,
nwd float NOT NULL,
dw float NOT NULL,
lop float NOT NULL,
esi float NOT NULL,
pf float NOT NULL,
emp_ctc float NOT NULL
)"""
insert_payslip = 'INSERT INTO PAYSLIP VALUES(1,"jan","2021","soham","EQDPP","c1","comp","se","2021-01-01","PAN","2021-01-03","hyd",20,10,20,7.4)'
select_payslip = "SELECT * FROM PAYSLIP"

drop_srhr = "DROP TABLE IF EXISTS SRHR"
create_srhr = """CREATE TABLE SRHR(
   ID INTEGER PRIMARY KEY,
   NAME varchar(50) NOT NULL,
   PASSWORD varchar(50) NOT NULL,
   EMAIL varchar(50) NOT NULL
)"""
insert_srhr = "INSERT INTO SRHR VALUES(null,'admin','pwd','admin@gmail.com')"
select_srhr = "SELECT * FROM SRHR"

drop_jrhr = "DROP TABLE IF EXISTS JRHR"
create_jrhr = """CREATE TABLE JRHR(
   _id INTEGER PRIMARY KEY,
   NAME varchar(50) NOT NULL,
   PASSWORD varchar(50) NOT NULL,
   EMAIL varchar(50) NOT NULL
)"""
insert_jrhr = "INSERT INTO JRHR VALUES(null,'jrhr','pwd','jrhr@gmail.com')"
select_jrhr = "SELECT * FROM JRHR"
