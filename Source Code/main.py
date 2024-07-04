import mysql.connector
import os
import install_database
import admin
import factchecker
import user
import searching

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="fact_checking")
mycursor=mycon.cursor()

def general_menu():
    print("WELCOME")
    print("What would you like to do?: ")
    print("1. Install the Software")
    print("2. Admin Login")
    print("3. Factchecker Login")
    print("4. User Login")
    print("5. User Signup")
    print("6. Search for Data Using Keyword")
    print("7. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        install_database.installation_menu()
    elif choice==2:
        admin.adminlogin()
    elif choice==3:
        factchecker.fact_checker_login()
    elif choice==4:
        user.user_login()
    elif choice==5:
        user.user_signup()
    elif choice==6:
        searching.search_data()
    elif choice==7:
        print("Thank you, have a nice day!")
    else:
        print("Invalid Choice!")

general_menu()
