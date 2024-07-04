import mysql.connector
import os

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="fact_checking")
mycursor=mycon.cursor()


#A function for a user to search for data using a keyword without having to login.
def search_data():
    keyword=input("Enter the keyword to be searched: ")
    sql="select * from data where description like '%{}%'".format(keyword)
    mycursor.execute(sql)
    myrecords=mycursor.fetchall()
    flag=0
    for i in myrecords:
        flag=1
        print("Data ID: ", i[0],'\n', "Heading: ",i[1],'\n', "Description: ",i[2],'\n',"URL: ",i[3],'\n',"Date of Entry: ",i[5],'\n',"Time of entry: ",i[6])
    if flag==0:
        print("No data with entered keyword.")
        
#A function to view all the data in the table.
def view_data():
    sql_view_data="select * from data"
    mycursor.execute(sql_view_data)
    myrecords=mycursor.fetchall()
    for i in  myrecords:
        print("Data ID: ", i[0],'\n', "Heading: ",i[1],'\n', "Description: ",i[2],'\n',"URL: ",i[3],'\n',"Date of Entry: ",i[5],'\n',"Time of entry: ",i[6])
        print()

