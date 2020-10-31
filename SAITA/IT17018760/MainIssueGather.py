import csv

import mysql.connector
import os.path
from Data.Variables import *
from QLearningAlgorithm import pula
from SayText import SayText

class GatherIssue(object):
    IssuedService = None
    @classmethod
    def TakeIssue(cls,issue,ex):



        mydb = mysql.connector.connect(
            host=sql_server,
            user=sql_uname,
            password=sql_password,
            database=sql_db
        )
        cls.valuex = 0
        yesnolist = ['yes', 'Yes', 'no', 'No']
        if issue in yesnolist:
            SayText.get_say_text().say(system_terminate)
            exit()


        else:

            mycursor = mydb.cursor()
            mycursor.execute("""SELECT typeID,errorID FROM service_error WHERE error = %s""", (issue,))
            myresult = mycursor.fetchall()
            for x in myresult:
                cls.valuex = x[0]
                cls.errorID=x[1]



                #print(cls.valuex)
            print(CSVGenClass.CSVGenrator(cls.valuex,cls.errorID,ex))
            #return cls.valuex


class CSVGenClass:
    @classmethod
    def CSVGenrator(ccc,valuex,errorID,ex):

        mydb = mysql.connector.connect(
            host=sql_server,
            user=sql_uname,
            password=sql_password,
            database=sql_db
        )

        mycursor = mydb.cursor()
        mycursor.execute("""SELECT csvName FROM error_type WHERE typeID = %s""", (valuex,))
        myresult1 = mycursor.fetchall()
        for y in myresult1:
            CSVName = y[0]





        if os.path.isfile(csvfilepath + CSVName):
            SayText.get_say_text().say(file_exist)
            ex.setData(CSVName,errorID)
            return ex.run_script()
            print("CSV File Is Exist In The Local Folder.")


        else:
            SayText.get_say_text().say(file_not_exist)
            print("CSV File Is Not Exist In The Local Folder And Created.")
            f = open(csvfilepath + CSVName + "", 'w')
            with f:
                writer = csv.writer(f)
            return pula().PathGenerator(CSVName,valuex,errorID,ex)











