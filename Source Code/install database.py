import mysql.connector
import os


mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="fact_checking")
mycursor=mycon.cursor()


sql_table_admin="create table if not exists admin_login (aid int primary key auto_increment, aname varchar(50), ausername varchar(50), apassword varchar(50))"
sql_table_factchecker="create table if not exists factchecker_login (fid int primary key auto_increment, fname varchar(50), fusername varchar(50), fpassword varchar(50))"
sql_table_user="create table if not exists user_login (uid int primary key auto_increment, uname varchar(50), uusername varchar(50), upassword varchar(50))"
sql_table_data="create table if not exists data (fcid int primary key auto_increment, heading varchar(150), description varchar(5000), url varchar(500), reporter_username varchar(50), dateofentry date, timeofentry time, status int)"

#A function to create the database and tables.
def first_install():
    mycursor.execute(sql_table_admin)
    mycursor.execute(sql_table_factchecker)
    mycursor.execute(sql_table_user)
    mycursor.execute(sql_table_data)
    mycon.commit()
    print("Software successfully installed.")

#A function to repair the database and tables.
def re_install():
    sql_reinstall1="drop table sql_table_admin"
    sql_reinstall2="drop table sql_table_factchecker"
    sql_reinstall3="drop table sql_table_user"
    sql_reinstall4="drop table sql_table_data"
    sql_reinstall5="drop table sql_table_keywords"
    mycursor.execute(sql_table_admin)
    mycursor.execute(sql_table_factchecker)
    mycursor.execute(sql_table_user)
    mycursor.execute(sql_table_data)
    mycon.commit()
    print("Software successfully re-installed.")


#A function to display menu for Installation and Re-installation.
def installation_menu():
    print("------------")
    print("Installation Menu: ")
    print("1. First Installation")
    print("2. Re-installation")

    choice=int(input("Enter your choice: "))
    if choice==1:
        first_install()
    elif choice==2:
        re_install()
    else:
        print("Invalid Choice!")
    
