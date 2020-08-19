import re
import mysql.connector
from ExecuteScripts import Exe
from collections import defaultdict
from ExecuteScripts import Execute
from csv import reader
import csv



class Graph:
    all_path = []
    k = 0
    def __init__(self, vertices):
        # No. of vertices
        all_path = []
        self.V = vertices
        # default dictionary to store graph
        self.graph = defaultdict(list)
        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            # print(path[0])
            self.all_path.append(str(path))
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
                    # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
        # Mark all the vertices as not visited
        visited = [False] * (self.V)
        # Create an array to store paths
        path = []
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)
        k=[]
        for pa in self.all_path:

            pa="".join(str(x) for x in pa)
            ps=pa.replace(","," ")


            k.append(ps)
        #print(k)

        return k

    # Create a graph given in the above diagram

class pula:
    @classmethod
    def PathGenerator(self,csvname,typeid,errorID):
        params=None;
        self.params=csvname
        self.params=typeid


        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="saita"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM node_join")
        myresult = mycursor.fetchall()

        g = Graph(1000)
        for x in myresult:
            # print(x[1], x[2])
            g.addEdge(x[1], x[2])



        mycursor.execute("""SELECT nodeID FROM service_start_node WHERE typeID = %s""", (typeid,))
        myresult = mycursor.fetchall()
        for x in myresult:
            valuey = x[0]
        # print(valuey)

        s = valuey
        d = 100
        print("Following are all different paths from %d to %d :" % (s, d))
        # print(g.printAllPaths(s, d))
        k = g.printAllPaths(s, d)

        def remove(string):
            return string.replace("  ", ",")

        arr = []

        for l in k:
            arr.append([l, 0, (len("".join(re.findall(r'[A-Z0-9a-z]', l))) - 2)])

        print(arr)
        CSVName = csvname
        f = open("CSVFILES/" + CSVName, 'w')
        with f:
            writer = csv.DictWriter(f, fieldnames=["path", "reward", "len"])
            writer.writeheader()
            writer = csv.writer(f)
            writer.writerows(sorted(arr, key=len))

        with open("CSVFILES/" + CSVName) as input, open('input.csv', 'w') as output:
            non_blank = (line for line in input if line.strip())
            output.writelines(non_blank)

        def copy_csv(filename):
            import pandas as pd
            df = pd.read_csv('input.csv')
            df.to_csv("CSVFILES/" + CSVName)

        copy_csv('input.csv')
        return Exe().run_script(CSVName,errorID)
        #return Execute().getDictionary(CSVName)




