import mysql.connector as sql
conn = sql.connect(host ='localhost',user ='root',password='Sant1234',database ='school')
if conn.is_connected():
    print("successfully connected")
    c1=conn.cursor()
    c1.execute("create table fees( S_Name varchar(50),Class varchar(5),Admission_Number varchar(10),Month_or_year varchar(6),fees varchar(10));")
    c1.execute("create table salary( T_Name varchar(50),Month varchar(15),Yes_No varchar(3));")
    c1.execute("create table student( Name varchar(30) NOT NULL,Class varchar(2) NOT NULL,Address varchar(50),Phone varchar(10),Admission_Number mediumint NOT NULL AUTO_INCREMENT PRIMARY KEY);")
    c1.execute("create table teacher( Name varchar(20),Post varchar(20),Salary varchar(8),address varchar(20),Phone varchar(10),Account varchar(10),id varchar(20) PRIMARY KEY);")
    print("Table created")
else:
    print("Not Connected")
