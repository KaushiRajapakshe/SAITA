import csv

from MainIssueGather import GatherIssue
import mysql.connector
import os.path

from ExecuteScripts import Exe
from QLearningAlgorithm import pula


class IssueControl(object):
    @classmethod
    def IssueTaker(taker):

        filesize = os.path.getsize("log_file.txt")
        if filesize != 0:  # Restart PC logic
            print("The file is not empty: ")
            file1 = open('log_file.txt', 'r')
            Lines = file1.readlines()

            count = 0
            txtarray = []
            # Strips the newline character
            for line in Lines:
                readingtxt = "{}".format(line.strip())
                print(readingtxt)
                txtarray.append(readingtxt)
            print(txtarray)

            CSVName = txtarray[1]
            errorID = txtarray[2]
            k = txtarray[3]

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
            taker.issue = input("Enter the issue")
            print(GatherIssue().TakeIssue(taker.issue))








IssueControl().IssueTaker()