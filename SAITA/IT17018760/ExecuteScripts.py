import csv
import operator
import re
import subprocess
import logging
import mysql


class Execute:
    path = {}
    rew = {}
    lent = {}
    ch = 0

    def __init__(self):
        path = {}
        rew = {}
        lent = {}
        self.ch=0

    @classmethod
    def getDictionary(self,CSVName):
        print("CSVName")
        k = 0
        with open("CSVFILES/" + CSVName) as f:
            read = csv.DictReader(f)
            for line in read:
                self.path[str(k)] = line['path']
                self.rew[str(k)] = line['reward']
                self.lent[str(k)] = line['len']
                k += 1
            f.close()
            self.rew = dict(sorted(self.rew.items(), key=operator.itemgetter(1), reverse=True))

    def get_path(self):

        return_path = None
        del_num = None
        if len(self.rew) == 1:
            for re in self.rew:
                return_path = self.path[re]
                del_num = re
                break
        elif len(self.rew) > 1:
            pr = []
            k = None
            for re in self.rew:
                if k is None:
                    k = self.rew[re]
                    pr.append(re)
                    continue
                if not k == self.rew[re]:
                    break
                pr.append(re)
            if len(pr) == 1:
                return_path = self.path[pr[0]]
                del_num = pr[0]
            elif len(pr) > 1:
                temp = {}
                for p in pr:
                    temp[p] = self.lent[p]
                temp = dict(sorted(temp.items(), key=operator.itemgetter(1)))
                for t in temp:
                    return_path = self.path[t]
                    del_num = t
                    break
        if not del_num is None:
            del self.path[del_num]
            del self.rew[del_num]
            del self.lent[del_num]
        return return_path

p1=Execute()



k = []
ch = 0





class Exe:

    def issuesolve(self):
        issueget=input("Is your issue solved? ")
        return issueget


    def run_script(self,CSVName,errorID):
        p1.getDictionary(CSVName)
        while True:
            k = p1.get_path()
            if k is None:
                break

            ab=k.replace("  ", ",")
            f = open('log_file.txt', 'w')
            f.write(ab )
            f.close()
            f1 = open('log_file.txt', 'a')
            f1.write("\n")
            f1.write(CSVName)
            f1.write("\n")
            f1.write(str(errorID))
            f1.write("\n")
            f1.write(str(k))
            f1.close()

            ard=ab.split(',')

            for letter in ard:
               #print (letter)
                #print("pula")
                res1 = "".join(re.findall("[A-Z0-9a-z]+", letter))
                #print(res1)

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="saita"
                )


                mycursor = mydb.cursor()
                mycursor.execute("SELECT code FROM node WHERE nodeID = %s", (res1,))
                myresult = mycursor.fetchall()
                for code in myresult:
                    #print(code[0])
                    fullCode=code[0]

                    mycursor.execute("SELECT ParamID FROM node WHERE nodeID = %s", (res1,))
                    myresult1 = mycursor.fetchall()
                    for paramid in myresult1:
                        paramID=paramid[0]
                        #print(paramid[0])

                    mycursor.execute("SELECT ParamName FROM parameter WHERE ParamID = %s ", (paramID,))
                    myresult2 = mycursor.fetchall()
                    for paramname in myresult2:
                        paramName=paramname[0]
                        #print(paramname[0])



                    if paramid[0] != 0:   #Has parameter
                        mycursor.execute("SELECT DefaultParameter FROM error_parameter WHERE ParamID = %s AND ErrorID=%s", (paramID,errorID,))
                        myresult3 = mycursor.fetchall()
                        for paracode in myresult3:
                            paramCode=paracode[0]
                            #print(paracode[0])

                        newc=fullCode.replace(paramName,paramCode)
                        #print(newc)
                        process = subprocess.Popen(["powershell", newc],shell=True, stdout=subprocess.PIPE)

                    else:
                        process = subprocess.Popen(["powershell", fullCode], shell=True, stdout=subprocess.PIPE)































            issueget=None
            issueget = self.issuesolve()
           # print(issueget)
            if issueget == "yes":
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

                nms = [1,line[1], str(addReward), line[3]]
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

            elif issueget == "no":

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




            else:
                return "Wrong input.Systen Exit"

