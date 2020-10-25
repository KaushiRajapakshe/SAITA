import csv
import operator
import re
import subprocess
from Data.Variables import *
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
        self.ch = 0

    @classmethod
    def getDictionary(self, CSVName):
        k = 0
        with open(csvfilepath + CSVName) as f:
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
        # print(return_path)
        return return_path


k = []
ch = 0


class Exe:
    csvName = None
    errid = None
    doid = None
    p1 = None

    def __init__(self, CSVName=None, errorID=None):
        if CSVName != None:
            self.p1 = Execute()
            self.p1.getDictionary(CSVName)
        self.csvName = CSVName
        self.errid = errorID
        self.runpath = None

    def setData(self, CSVName, errorID):
        self.p1 = Execute()
        self.p1.getDictionary(CSVName)
        self.csvName = CSVName
        self.errid = errorID

    def issuesolve(self):
        issueget = input("Is your issue solved? ")
        return issueget

    def run_script(self):
        k = self.p1.get_path()
        self.runpath = k
        if k is None:
            return "All Path executed"

        ab = k.replace("  ", ",")
        f = open(executedLog, 'w')
        f.write(ab)
        f.close()
        f1 = open(executedLog, 'a')
        f1.write("\n")
        f1.write(self.csvName)
        f1.write("\n")
        f1.write(str(self.errid))
        f1.write("\n")
        f1.write(str(k))
        f1.close()

        ard = ab.split(',')

        for letter in ard:
            res1 = "".join(re.findall("[A-Z0-9a-z]+", letter))

            mydb = mysql.connector.connect(
                host=sql_server,
                user=sql_uname,
                password=sql_password,
                database=sql_db
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT code FROM node WHERE nodeID = %s", (res1,))
            myresult = mycursor.fetchall()
            for code in myresult:
                fullCode = code[0]

                mycursor.execute("SELECT ParamID FROM node WHERE nodeID = %s", (res1,))
                myresult1 = mycursor.fetchall()
                for paramid in myresult1:
                    paramID = paramid[0]

                mycursor.execute("SELECT ParamName FROM parameter WHERE ParamID = %s ", (paramID,))
                myresult2 = mycursor.fetchall()
                for paramname in myresult2:
                    paramName = paramname[0]

                if paramid[0] != 0:  # Has parameter
                    mycursor.execute("SELECT DefaultParameter FROM error_parameter WHERE ParamID = %s AND ErrorID=%s",
                                     (paramID, self.errid,))
                    myresult3 = mycursor.fetchall()
                    for paracode in myresult3:
                        paramCode = paracode[0]

                    newc = fullCode.replace(paramName, paramCode)
                    try:
                        process = subprocess.Popen(["powershell", newc], shell=True, stdout=subprocess.PIPE)
                    except:
                        pass
                else:
                    try:
                        process = subprocess.Popen(["powershell", fullCode], shell=True, stdout=subprocess.PIPE)
                    except:
                        pass
        return self
#if it is yes script running
    def say_yes(self):
        k = self.runpath
        with open(csvfilepath + self.csvName, 'rt') as f:
            reader = csv.reader(f)
            results = filter(lambda x: k in x, reader)
            for line in results:
                print("<Solution Path Executed>")

            addReward = int(line[2]) + 1;
            # print(addReward)

        lines = list()
        with open(csvfilepath + self.csvName, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == k:
                        lines.remove(row)

        with open(indexCSV, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        nms = [1, line[1], str(addReward), line[3]]
        f = open(indexCSV, 'a')
        with f:
            writer = csv.writer(f)
            writer.writerow(nms)

        with open(indexCSV) as inputt, open(csvfilepath + self.csvName, 'w') as output:
            non_blank = (line for line in inputt if line.strip())
            output.writelines(non_blank)

        f = open(executedLog, 'w')
        f.write("")
        return "Thank you for join with SAITA"

#if user said no to the chat screen
    def say_no(self):
        k = self.runpath
        with open(csvfilepath + self.csvName, 'rt') as f:
            reader = csv.reader(f)
            results = filter(lambda x: k in x, reader)
            for line in results:
                print("<Solution Path Executed.>")
            addReward = int(line[2]) - 1;
            # print(addReward)

        lines = list()
        with open(csvfilepath + self.csvName, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == k:
                        lines.remove(row)

        with open(indexCSV, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        nms = [1, line[1], str(addReward), line[3]]
        # print(nms)
        f = open(indexCSV, 'a')
        with f:
            writer = csv.writer(f)
            writer.writerow(nms)

        with open(indexCSV) as inputt, open(csvfilepath + self.csvName, 'w') as output:
            non_blank = (line for line in inputt if line.strip())
            output.writelines(non_blank)
        output.close()
        inputt.close()

        return self.run_script()
