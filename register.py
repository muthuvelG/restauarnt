#!G:\Python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

print("<br><center><h2>Thank you for Register <a href='/familyrestaurant'>Back to Home</a></h2></center>")

form=cgi.FieldStorage()
fname=form.getvalue("name")
fphonenumber=form.getvalue("phonenumber")
fmembers=form.getvalue("members")
fclass=form.getvalue("class")
flook=form.getvalue("look")

#print(fname,fphonenumber,fmembers,fclass,flook)


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="restaurant"
)

mycursor=mydb.cursor()

Sql="INSERT INTO booking(Name,PhoneNumber,Members,Class,Look)VALUES(%s,%s,%s,%s,%s)";
val=(fname,fphonenumber,fmembers,fclass,flook)

mycursor.execute(Sql,val)
mydb.commit()
