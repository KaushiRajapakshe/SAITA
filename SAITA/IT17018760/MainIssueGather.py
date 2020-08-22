import csv

import mysql.connector
import os.path

from ExecuteScripts import Exe
from QLearningAlgorithm import pula

class GatherIssue(object):
    IssuedService = None
    @classmethod
    def TakeIssue(cls,issue):

        print("The file is  empty: ")

        #issue = input("Enter the issue")   #Gather issue for 1st time

        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="saita"
            )
        cls.valuex = 0

        mycursor = mydb.cursor()
        mycursor.execute("""SELECT typeID,errorID FROM service_error WHERE error = %s""", (issue,))
        myresult = mycursor.fetchall()
        for x in myresult:
            cls.valuex = x[0]
            cls.errorID=x[1]



            #print(cls.valuex)
        print(CSVGenClass.CSVGenrator(cls.valuex,cls.errorID))
        #return cls.valuex


class CSVGenClass:
    @classmethod
    def CSVGenrator(ccc,valuex,errorID):

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="saita"
        )
        mycursor = mydb.cursor()
        mycursor.execute("""SELECT csvName FROM error_type WHERE typeID = %s""", (valuex,))
        myresult1 = mycursor.fetchall()

        for y in myresult1:
            CSVName = y[0]
        print(CSVName)




        if os.path.isfile("CSVFILES/" + CSVName):
            return Exe().run_script(CSVName,errorID)
            print("File exist")
        else:
            print("File not exist")
            f = open("CSVFILES/""" + CSVName + "", 'w')
            with f:
                writer = csv.writer(f)

            return pula().PathGenerator(CSVName,valuex,errorID)











