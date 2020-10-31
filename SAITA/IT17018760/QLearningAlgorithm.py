import re
import mysql.connector
from collections import defaultdict
from Data.Variables import *
import csv
from SayText import SayText




class Graph:
    all_path = []
    k = 0
    def __init__(self, vertices):
        all_path = []
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):

        visited[u] = True
        path.append(u)
        if u == d:
            self.all_path.append(str(path))
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
        path.pop()
        visited[u] = False
    def printAllPaths(self, s, d):
        visited = [False] * (self.V)
        path = []
        self.printAllPathsUtil(s, d, visited, path)
        k=[]
        for pa in self.all_path:

            pa="".join(str(x) for x in pa)
            ps=pa.replace(","," ")


            k.append(ps)

        return k


class pula:
    @classmethod
    def PathGenerator(self,csvname,typeid,errorID,ex):
        params=None;
        self.params=csvname
        self.params=typeid

        mydb = mysql.connector.connect(
            host=sql_server,
            user=sql_uname,
            password=sql_password,
            database=sql_db
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM node_join")
        myresult = mycursor.fetchall()

        g = Graph(1000)
        for x in myresult:
            g.addEdge(x[1], x[2])



        mycursor.execute("""SELECT nodeID FROM service_start_node WHERE typeID = %s""", (typeid,))
        myresult = mycursor.fetchall()
        for x in myresult:
            valuey = x[0]

        s = valuey
        d = 100

        k = g.printAllPaths(s, d)

        def remove(string):
            return string.replace("  ", ",")

        arr = []

        for l in k:
            arr.append([l, 0, (len("".join(re.findall(r'[A-Z0-9a-z]', l))) - 2)])

        CSVName = csvname
        f = open(csvfilepath + CSVName, 'w')
        with f:
            writer = csv.DictWriter(f, fieldnames=["path", "reward", "len"])
            writer.writeheader()
            writer = csv.writer(f)
            writer.writerows(sorted(arr, key=len))

        with open(csvfilepath + CSVName) as input, open(inputCSV, 'w') as output:
            non_blank = (line for line in input if line.strip())
            output.writelines(non_blank)

        def copy_csv(filename):
            import pandas as pd
            df = pd.read_csv(inputCSV)
            df.to_csv(csvfilepath + CSVName)

        SayText.get_say_text().say(generating_csv)
        copy_csv(inputCSV)
        ex.setData(CSVName, errorID)
        return ex.run_script()




