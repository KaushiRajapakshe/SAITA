import csv

import mysql.connector
import os.path

issue=input("Enter the issue")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="saita"
)
valuex=0
CSVName="Not Exist"
mycursor = mydb.cursor()
mycursor.execute("""SELECT typeID FROM service_error WHERE error = %s""", (issue,))

myresult = mycursor.fetchall()

for x in myresult:
    valuex=x[0]
print(valuex)

mycursor.execute("""SELECT csvName FROM error_type WHERE typeID = %s""", (valuex,))
myresult1 = mycursor.fetchall()

for y in myresult1:
    CSVName=y[0]
print(CSVName)



if os.path.isfile("CSVFILES/"+CSVName):
    print ("File exist")
else:
    print ("File not exist")
    f = open("CSVFILES/"""+CSVName+"", 'w')
    with f:
        writer = csv.writer(f)







