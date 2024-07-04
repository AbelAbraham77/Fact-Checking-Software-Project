import mysql.connector
import os


mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="fact_checking")
mycursor=mycon.cursor()

#A function to add fact checkers to the database.        
def add_fact_checkers():
    fname=input("Enter Name: ")
    fusername=input("Enter Username: ")
    fpassword=input("Enter Password: ")

    sql_add_fact_checkers="Insert into factchecker_login(fname, fusername, fpassword) values('{}','{}','{}')".format(fname, fusername, fpassword)
    mycursor.execute(sql_add_fact_checkers)
    mycon.commit()

#A function to view all the factcheckers in the database.
def view_fact_checkers():
    sql_view_fact_checkers="select * from factchecker_login"
    mycursor.execute(sql_view_fact_checkers)
    myrecords=mycursor.fetchall()

    for i in myrecords:
        print("Name: ", i[1], "Username: ", i[2])

#A function to update the details of a factchecker in the database.
def update_fact_checkers():
    print("1. Update Name")
    print("2. Update Username")
    print("3. Update Password")

    update_choice=int(input("Enter your choice: "))
    if update_choice==1:
        fid=int(input("Enter the Fact Checker ID: "))
        new_fname=input("Enter the new name: ")
        sql_update_factchecker_name="update factchecker_login set fname='{}' where fid={}".format(new_fname, fid)
        mycursor.execute(sql_update_factchecker_name)
        mycon.commit()
    elif update_choice==2:
        fid=int(input("Enter the Fact Checker ID: "))
        new_fusername=input("Enter the new username: ")
        sql_update_factchecker_username="update factchecker_login set fusername='{}' where fid={}".format(new_fusername, fid)
        mycursor.execute(sql_update_factchecker_username)
        mycon.commit()
    elif choice==3:
        fid=int(input("Enter the Fact Checker ID: "))
        new_fpassword=input("Enter the new password: ")
        sql_update_factchecker_password="update factchecker_login set fpassword='{}' where fid={}".format(new_fpassword, fid)
        mycursor.execute(sql_update_factchecker_password)
        mycon.commit()
    else:
        print("Invalid Choice!")

#A function to delete a fact checker.
def delete_fact_checkers():
    fid=int(input("Enter the ID of the record to be deleted: "))
    sql_delete_fact_checkers="delete from factchecker_login where fid={}".format(fid)
    mycursor.execute(sql_delete_fact_checkers)
    mycon.commit()
    print("Fact Checker deleted successfully")

#A function to view all the reported data from the data table.
def view_reported_data_admin():
    sql_view_reported_data="select * from data where status=0"
    mycursor.execute(sql_view_reported_data)
    myrecords=mycursor.fetchall()
    for i in  myrecords:
        print('\n',"Data ID: ", i[0], '\n', "Heading: ",i[1],'\n', "Description: ",i[2],'\n',"URL: ",i[3],'\n',"Date of Entry: ",i[5],'\n',"Time of entry: ",i[6])
        if i[7]==0:
            print("Status: Pending") #Displays the status of the reported data.
        elif i[7]==1:
            print("Status: Checked, Data is True")
        elif i[7]==-1:
            print("Status: Checked, Data is False")
                  
        print()

#A function to view all users in the database.    
def view_users():
    sql_view_users="select * from user_login"
    mycursor.execute(sql_view_users)
    myrecords=mycursor.fetchall()

    for i in myrecords:
        print("Name: ", i[1], "Username: ", i[2])

#A function to update the details of a user in the database.
def update_user():
    print("1. Update Name")
    print("2. Update Username")
    print("3. Update Password")

    update_choice=int(input("Enter your choice: "))
    if update_choice==1:
        uid=int(input("Enter the User ID: "))
        new_uname=input("Enter the new name: ")
        sql_update_user_name="update user_login set uname='{}' where uid={}".format(new_uname, uid)
        mycursor.execute(sql_update_user_name)
        mycon.commit()
    elif update_choice==2:
        uid=int(input("Enter the User ID: "))
        new_uusername=input("Enter the new username: ")
        sql_update_user_username="update user_login set uusername='{}' where uid={}".format(new_uusername, uid)
        mycursor.execute(sql_update_user_username)
        mycon.commit()
    elif update_choice==3:
        uid=int(input("Enter the User ID: "))
        new_upassword=input("Enter the new password: ")
        sql_update_user_password="update user_login set upassword='{}' where uid={}".format(new_upassword, uid)
        mycursor.execute(sql_update_user_password)
        mycon.commit()
    else:
        print("Invalid Choice!")

#A function to delete a user.
def delete_user():
    uid=int(input("Enter the ID of the record to be deleted: "))
    sql_delete_user="delete from user_login where uid={}".format(uid)
    mycursor.execute(sql_delete_user)
    mycon.commit()
   print("User successfully deleted")

#A function to backup all the data onto a text file.
def backup_data():
    file=open("backup.txt", "a")
    data=[]
    
    sql_view_data="select * from data"
    mycursor.execute(sql_view_data)
    myrecords=mycursor.fetchall()
    for i in myrecords:
        file.write(f"Data ID: {i[0]} \n")
        file.write(f"Heading: {i[1]} \n")
        file.write(f"Description: {i[2]} \n")
        file.write(f"URL: {i[3]} \n")
        file.write(f"Reporter Username: {i[4]} \n")
        file.write(f"Date of Entry: {i[5]} \n")
        file.write(f"Time of Entry: {i[6]} \n")
        if i[7]==1:
            file.write("Status: Data True \n")
        elif i[7]==-1:
            file.write("Status: Data False \n")
        elif i[7]==0:
            file.write("Status: Pending \n")
        else:
            file.write(f"Status: {i[7]} \n")
        file.write(" \n")
        
    print("Backup Generated Successfully")
    
    file.close()
    os.startfile("backup.txt") #Opens the text file on the computer.

#A function that displays the admin menu and executes the function called depending on the admin's choice.
def adminmenu():
    ch='y'
    while ch=='y' or ch=='Y':
        print("------------")
        print("1. Add Fact Checkers")
        print("2. View Fact Checkers")
        print("3. Update Fact Checkers")
        print("4. Delete Fact Checkers")
        print("5. View Reported Data")
        print ("6. View Users")
        print("7. Update User")
        print("8. Delete User")
        print("9. Backup Data")

        choice=int(input("Enter your choice: "))
        if choice==1:
            add_fact_checkers()
        elif choice==2:
            view_fact_checkers()
        elif choice==3:
            update_fact_checkers()
        elif choice==4:
            delete_fact_checkers()
        elif choice==5:
            view_reported_data_admin()
        elif choice==6:
            view_users()
        elif choice==7:
            update_user()
        elif choice==8:
            delete_user()
        elif choice==9:
            backup_data()
        else:
            print("Invalid Choice!")
        ch=input("Do you want to continue? y/n")

#A function to authenticate an admin user.   
def adminlogin():
    user=input("Enter username: ")
    password=input("Enter password: ")
    sql="select * from admin_login where ausername='{}' and apassword='{}'".format(user, password)
    mycursor.execute(sql)
    myrecords=mycursor.fetchall()
    
    count=0
    for i in myrecords:
        print("Name: ", i[1])
        print("Logged in successfully")
        count=1
        adminmenu()

    if count==0:
        print("Access Denied")
     
