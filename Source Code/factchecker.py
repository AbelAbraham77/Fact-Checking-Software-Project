import mysql.connector
import os

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="fact_checking")
mycursor=mycon.cursor()

#A function to view the reported data.       
def view_reported_data_factchecker():
    sql="select * from data where status=0 "
    mycursor.execute(sql)
    myrecords=mycursor.fetchall()
    for i in  myrecords:
        print("Heading: ",i[1],'\n', "Description: ",i[2],'\n',"URL: ",i[3],'\n',"Date of Entry: ",i[5],'\n',"Time of entry: ",i[6],'\n',"Status:",i[7])
        print()

#A function to update the status of reported data.
def update_status():
    fcid=int(input("Enter the ID of the Data: "))
    status=input("Enter the status of the data (T/F): ")
    if status=="t" or status=="T":
        sql="update data set status=1 where fcid={}".format(fcid) #Set the status of the reported data to 1 (True).
        mycursor.execute(sql)
        mycon.commit()
        
    elif status=="f" or status=="F":
        sql="update data set status=-1 where fcid={}".format(fcid) #Set the status of the reported data to -1 (False).
        mycursor.execute(sql)
        mycon.commit()
        

#A function that displays the fact checker menu and executes the function called depending on the fact checker's choice.       
def factchecker_menu():
    ch='y'
    while ch=='y' or ch=='Y':
        print("------------")
        print("1. View reported data")
        print("2. Update status")

        choice=int(input("Enter your choice"))
        if choice==1:
            view_reported_data_factchecker()  
        elif choice==2:
            update_status()
        
        else:
            print("Invalid choice:")
        ch=input("Do you want to continue? y/n ")


#A function to authenticate a factchecker.
def fact_checker_login():
    user=input("Enter username: ")
    password=input("Enter password: ")
    sql="Select * from factchecker_login where fusername='{}' and fpassword='{}'".format(user,password)
    mycursor.execute(sql)
    myrecords=mycursor.fetchall()

    count=0
    for i in  myrecords:
        print("Name: ",i[1])
        print("Logged in successfully")
        factchecker_menu()
        count=1

    if count==0:
        print("Access Denied")
