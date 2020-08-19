import csv

import mysql.connector
import os.path

from ExecuteScripts import Exe
from QLearningAlgorithm import pula

class GatherIssue(object):
    IssuedService = None
    @classmethod
    def TakeIssue(cls):

        filesize = os.path.getsize("log_file.txt")
        if filesize != 0:                           #Restart PC logic
            print("The file is not empty: ")
            file1 = open('log_file.txt', 'r')
            Lines = file1.readlines()

            count = 0
            txtarray=[]
            # Strips the newline character
            for line in Lines:
                readingtxt="{}".format(line.strip())
                print(readingtxt)
                txtarray.append(readingtxt)
            print(txtarray)

            CSVName = txtarray[1]
            errorID =txtarray[2]
            k=txtarray[3]


            issueget = input("Is your issue solved?")
            print(issueget)
            if issueget == "yes":
                print("it says yes")

                with open("CSVFILES/" + CSVName, 'rt') as f:
                    reader = csv.reader(f)
                    results = filter(lambda x: k in x, reader)
                    for line in results:
                        print(line)

                    addReward = int(line[2]) + 1;
                    print(addReward)

                lines = list()
                with open("CSVFILES/" + CSVName, 'r') as readFile:
                    reader = csv.reader(readFile)
                    for row in reader:
                        lines.append(row)
                        for field in row:
                            if field == k:
                                lines.remove(row)

                with open('index.csv', 'w') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(lines)

                nms = [1, line[1], str(addReward), line[3]]
                print(nms)
                f = open('index.csv', 'a')
                with f:
                    writer = csv.writer(f)
                    writer.writerow(nms)

                with open('index.csv') as inputt, open("CSVFILES/" + CSVName, 'w') as output:
                    non_blank = (line for line in inputt if line.strip())
                    output.writelines(non_blank)

                f = open('log_file.txt', 'w')
                f.write("")
                return "Thank you for join with SAITA"

            else:
                with open("CSVFILES/" + CSVName, 'rt') as f:
                    reader = csv.reader(f)
                    results = filter(lambda x: k in x, reader)
                    for line in results:
                        print(line)
                    addReward = int(line[2]) - 1;
                    print(addReward)

                lines = list()
                with open("CSVFILES/" + CSVName, 'r') as readFile:
                    reader = csv.reader(readFile)
                    for row in reader:
                        lines.append(row)
                        for field in row:
                            if field == k:
                                lines.remove(row)

                with open('index.csv', 'w') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(lines)

                nms = [1, line[1], str(addReward), line[3]]
                print(nms)
                f = open('index.csv', 'a')
                with f:
                    writer = csv.writer(f)
                    writer.writerow(nms)

                with open('index.csv') as inputt, open("CSVFILES/" + CSVName, 'w') as output:
                    non_blank = (line for line in inputt if line.strip())
                    output.writelines(non_blank)
                output.close()
                inputt.close()
                return Exe().run_script(CSVName, errorID)








        else:
            print("The file is  empty: ")

            issue = input("Enter the issue")   #Gather issue for 1st time

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












GatherIssue.TakeIssue()