import mysql.connector
import random
import pandas as pd
con=mysql.connector.connect(host="localhost",passwd="SET PASSWORD",user="root",database="CREATE DATABASE")
if con.is_connected():
    print("Successfully connected")
else:
    print("Not connected")
def ast(): # Function to add Student 
    n=input("Students Name:")
    c=input("Class Name:")
    a=input("Address:")
    p=input("Phone:")
    ad=int()
    data=(n,c,a,p,ad)
    sql='insert into student values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully ")
    print(">-----------------------------------------------------------<")
    main()
def rst(): # Function to Remove Student
    c=input("Class Name:")
    ad=input("Addmition No:")
    data=(c,ad)
    sql='delete from student where CLASS=%s and Admission_Number= %s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
    main()    
def addt(): # Function to add Teacher
    fn=input("First Name:")
    ln=input("Last Name:")
    n=str(random.randint(0,9999))
    name=fn+" "+ln
    p=input("Post:")
    s=input("Salary:")
    a=input("Address:")
    ph=input("Phone:")
    n1=str(random.randint(0,999999))
    ac="RBIN"+n1
    tid=fn+n+"@scna"
    data=(name,p,s,a,ph,ac,tid)
    sql='insert into teacher values(%s,%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Executed Successfully")
    print(">-----------------------------------------------------------<")
    main()    
def upst(): # Function to update Student
    print("-----------------------------------\nCHOOSE WHAT YOU WANT TO UPDATE\n-----------------------------------")
    print("1.Student Name")
    print("2.Phone Number")
    print("3.Class")
    print("4.Address")
    print("5.Home")
    print("-----------------------------------")
    choice=input("Enter Task No:")
    if(choice=="1"):
        nst()
    elif(choice=="2"):
        phno()
    elif(choice=="3"):
        clss()
    elif(choice=="4"):
        adrs()
    elif(choice=="5"):
        main()    
    else:
        print("Wrong Choice")
        upst()
def nst(): # To update Name of student
    n=input("Please Enter Name:")
    ad=input("Please Enter Admission no:")
    data=(n,ad)
    sql="update student set name=%s where admission_no=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
def phno(): # To update Phone Number of student
    ph=input("Please Enter Phone Number:")
    ad=input("Please Enter Admission no:")
    data=(ph,ad)
    sql="update student set phone=%s where admission_no=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
def clss(): # To update Class of Student 
    cs=input("Please Enter Class:")
    ad=input("Please Enter Admission no:")
    data=(cs,ad)
    sql="update student set class=%s where admission_no=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
def adrs(): # To update Address of Student
    cs=input("Please Enter Address:")
    ad=input("Please Enter Admission no:")
    data=(cs,ad)
    sql="update student set Address=%s where admission_no=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
def remt(): # To Remove Teacher
    ac=input("Account No:")
    data=(ac)
    sql="delete from teacher where Account='%s'"%(ac)
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data updated")
    print(">-----------------------------------------------------------<")
    main()
def updt(): # Function to update Teacher's Details
    print("-----------------------------------\nCHOOSE WHAT YOU WANT TO UPDATE\n-----------------------------------")
    print("1.Name")
    print("2.Phone Number")
    print("3.Post")
    print("4.Salary")
    print("5.Address")
    print("6.Account ")
    print("7.Home")
    print("-----------------------------------")
    choice=input("Enter Task No:")
    print(">---------------------------<")
    if(choice=="1"):
        nt()
    elif(choice=="2"):
        phnt()
    elif(choice=="3"):
        pst()
    elif(choice=="4"):
        slry()
    elif(choice=="5"):
        adrst()
    elif(choice=="6"):
        acunt()
    elif(choice=="7"):
        main()
    else:
        print("Wrong Choice")
        updt()
def nt(): # Function to update Name of teacher 
    nm=input("Please Enter Name:")
    tid=input("Please Enter Teacher ID:")
    data=(nm,tid)
    sql="update teacher set Name=%s where id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
def phnt(): # Function to update Phone Number of teacher
    phn=input("Please Enter New Phone Number:")
    tid=input("Please Enter Teacher ID:")
    data=(phn,tid)
    sql="update teacher set Phone=%s where id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
def pst(): # Function to update Post of teacher
    post=input("Please Enter Post:")
    tid=input("Please Enter Teacher ID:")
    data=(post,tid)
    sql="update teacher set Post=%s where id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
def slry(): # Function to update Salary of teacher
    sal=input("Please Enter Salary:")
    tid=input("Please Enter Teacher_ID:")
    data=(sal,tid)
    sql="update teacher set Salary=%s where id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
def adrst(): # Function to update Address Of teacher
    adss=input("Please Enter New Address:")
    tid=input("Please Enter Teacher ID:")
    data=(adss,tid)
    sql="update teacher set address=%s where id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
def acunt(): # Funcion to update Account Number of teacher
    acnt=input("Please Enter New Account Number:")
    tid=input("Please Enter Teacher ID:")
    data=(acnt,tid)
    sql="update teacher set Account=%s where id=%s"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
def submitf(): # Function to submit fees
    n=input("Students Name:")
    c=input("Class Name:")
    r=input("Admission Number:")
    m=input("Month and Year:")
    f=input("fees:")
    d=input("Date:")
    data=(n,c,r,m,f,d)
    sql="insert into fees values(%s,%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-----------------------------------------------------------<")
    main()
def pays(): # Function to pay salary
    n=input("Teachers name:")
    m=input("Month:")
    p=input("Yes/No:")
    data=(n,m,p)
    sql="insert into salary values(%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data entred Successfully")
    print(">-----------------------------------------------------------<")
    main()
def dclass(): # Funcion to Display Class Records
    cl=input("Class:")
    data=(cl)
    sql="select * from student where class='%s'"%(cl)
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    na2=pd.DataFrame(d,columns=["Name","Class","Address","Phone","Admission_Number"])
    print(na2)
    print()
    main()
def dteacher(): # Funcion to Display Teachers Records
    sql="select * from teacher "
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    na1=pd.DataFrame(d,columns=["Name","Post","Salary","Address","Phone","Account","Teacher ID"])
    print(na1)
    main()
def excsv(): # Function to Extract Records 
    print("-----------------------------------\nCHOOSE WHAT YOU WANT TO UPDATE\n-----------------------------------")
    print("1.Extract Students Record")
    print("2.Extract Teachers Record")
    print("3.Extract Salary Record")
    print("4.Extract Fees Record")
    print("5.Home")
    print("-----------------------------------")
    choice=input("Enter Task No:")
    print(">---------------------------<")
    if(choice=="1"):
       cl=input("Class:")
       data=(cl)
       sql="select * from student where class=%s"%(cl)
       c=con.cursor()
       c.execute(sql,data)
       d=c.fetchall()
       na2=pd.DataFrame(d,columns=["Name","Class","Address","Phone","Admission_Number"])
       print(na2)
       confr=input("Do You want to Extract Above File (y/n):")
       if confr=="y":
           na2.to_csv("C:\\Users\\users1\\Documents\\Class.csv")
           print("Extraction Successful")
           excsv()
       else:
           excsv()
    elif(choice=="2"):
        sql="select * from teacher"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        na1=pd.DataFrame(d,columns=["Name","Post","Salary","Address","Phone","Account","Teacher ID"])
        print(na1)
        confr=input("Do You want to Extract Above File (y/n):")
        if confr=="y":
            na1.to_csv("C:\\Users\\users1\\Documents\\Teachers.csv")
            print("Extraction Successful")
            excsv()
        else:
            main()
    elif(choice=="3"):
        sql="select * from salary"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        na3=pd.DataFrame(d,columns=["T_Name","Month","Yes_No"])
        print(na3)
        confr=input("Do You want to Extract Above File (y/n):")
        if confr=="y":
            na3.to_csv("C:\\Users\\users1\\Documents\\Salary.csv")
            print("Extraction Successful")
            excsv()
        elif confr=="n":
            excsv()
        else:
            print("Wrong Choice")
            excsv()
    elif(choice=="4"):
        sql="select*from fees"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        na5=pd.DataFrame(d,columns=["S_Name","Class","Roll_Number","Month or Year","Fees","Date"])
        print(na5)
        confr=input("Do You want to Extract Above File (y/n):")
        if confr=="y":
            na5.to_csv("C:\\Users\\users1\\Documents\\Fees.csv")
            print("Extraction Successful")
            excscv()
        else:
            excsv()
    elif(choice=="5"):
        main()
    else:
        print("Wrong Choice")
        excsv()    
def sysclose(): # Function to Exit system 
    exit()
def main(): # This is the main Function 
    print("-----------------------------------\nWELCOME TO SCHOOL MANAGEMENT SYSTEM\n-----------------------------------")
    print("01.ADD STUDENT")
    print("02.REMOVE STUDENT")
    print("03.UPDATE STUDENT")
    print("04.ADD TEACHER")
    print("05.REMOVE TEACHER")
    print("06.UPDATE TEACHER")
    print("07.SUBMIT FEES")
    print("08.PAY SALARY")
    print("09.DISPLAY CLASS")
    print("10.TEACHERS LIST")
    print("11.EXTRACT RECORD")
    print("12.CLOSE SYSTEM")
    print("-----------------------------------")
    choice=input("Enter Task No:")
    if(choice=="1"):
        ast()
    elif(choice=="2"):
        rst()
    elif(choice=="3"):
        upst()
    elif(choice=="4"):
        addt()
    elif(choice=="5"):
        remt()
    elif(choice=="6"):
        updt()
    elif(choice=="7"):
        submitf()
    elif(choice=="8"):
        pays()
    elif(choice=="9"):
        dclass()
    elif(choice=="10"):
        dteacher()
    elif(choice=="11"):
        excsv()
    elif(choice=="12"):
        con.close()
        if con.is_connected():
            print("Unable To Close Connection")
        else:
            print("Connection Closed")
            conf=input("Do you want close system (y/n):")
            if conf=="y":
                exit()
            else:
                main()
    else:
        print("Wrong Choice")
        main()
print('-----------------------------\nSANT CHAVARA NATIONAL ACADEMY\n-----------------------------')
def pswd(): # Password Function
    login=input("Enter Login_Id:")
    p=input("Enter Password:")
    login_id="SET LOGIN ID"
    passwd="SET PASSWORD"
    if login==login_id and p==passwd:
        main()
    else:
        print("Wrong LoginId Or Password")
        print("Please Try Again")
        pswd()
pswd()        
