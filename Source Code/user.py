import mysql.connector
import os

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="fact_checking")
mycursor=mycon.cursor()

#A function to add data to the table.
def add_data():
    heading=input("Enter the heading of the data: ")
    description=input("Enter the description: ")
    url=input("Enter the URL: ")
    date_of_entry=input("Enter date (in the format YYYY-MM-DD): ")
    time_of_entry=input("Enter time (in the format HH:MM:SS): ")

    sql_add_data="insert into data(heading, description, url, dateofentry, timeofentry) values('{}', '{}', '{}', '{}', '{}')".format(heading,description,url,date_of_entry,time_of_entry)
    mycursor.execute(sql_add_data)
    mycon.commit()

#A function to report data.    
def report_data():
    user=input("Enter username: ")
    data_id=int(input("Enter the ID of the data you want to report: "))
    sql_report_data="update data set status=0 where fcid={}".format(data_id)
    mycursor.execute(sql_report_data)
    mycon.commit()
    
    sql1="update data set reporter_username='{}' where fcid={}".format(user, data_id)
    mycursor.execute(sql1)
    mycon.commit()

#A function to view the status of a data that a user has reported.
def view_status(user):
    sql_view_status="select fcid, heading, status from data where reporter_username='{}'".format(user)
    mycursor.execute(sql_view_status)
    myrecords=mycursor.fetchall()
    for i in myrecords:
        if i[2]==0:
            print(f"Data ID: {i[0]}, Title: {i[1]}, Status: Pending")
            print(" \n")
        elif i[2]==1:
            print(f"Data ID: {i[0]}, Title: {i[1]}, Status: Data True")
            print(" \n")
        elif i[2]==-1:
            print(f"Data ID: {i[0]}, Title: {i[1]}, Status: Data False")
            print(" \n")

#A function that displays the user menu and executes the function called depending on the user's choice.    
def user_menu(user):
    ch='y'
    while ch=='y' or ch=='Y':
        print("------------")
        print("1. View Data")
        print("2. Add Data")
        print("3. Report Data")
        print("4. View status of reported data")

        choice=int(input("Enter your choice: "))
        if choice==1:
            view_data()
        elif choice==2:
            add_data()
        elif choice==3:
            report_data()
        elif choice==4:
            view_status(user)
        else:
            print("Invalid choice: ")
        ch=input("Do you want to continue? y/n: ")

#A function to authenticate a user.
def user_login():
    user=input("Enter username: ")
    password=input("Enter password: ")
    sql="select * from user_login where uusername='{}' and upassword='{}'".format(user,password)
    mycursor.execute(sql)
    myrecords=mycursor.fetchall()

    count=0
    for i in  myrecords:
        print("Name: ",i[1])
        print("Logged in successfully")
        count=1
        user_menu(user)

    if count==0:
        print("Access Denied")

#A function for user signup.
def user_signup():
    uname=input("Enter Name: ")
    uusername=input("Enter Username: ")
    upassword=input("Enter Password: ")

    sql_add_user="Insert into user_login(uname, uusername, upassword) values('{}','{}','{}')".format(uname, uusername, upassword)
    mycursor.execute(sql_add_user)
    mycon.commit()
    print("Signed Up successfully")

