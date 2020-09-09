# from Controllers.Query import Queries
# from Util.DBConnection import DBConnection
# import ctypes
# import datetime
# from tkinter import*
# from win32api import GetMonitorInfo, MonitorFromPoint
from Util.ScriptGenerator import ScriptGenerator
from Util.Logistic_ranking import Logistic
from Controllers.Ranking_controller import RankingController

# x = '2'
# print(DBConnection.select_query("SELECT error_msg,error_code,connection_type,issue_id FROM network_errors_msg"))
# print(DBConnection.select_param_query('SELECT error_msg FROM network_errors_msg where issue_id=%s', (x,)))
# print(Queries.get_errorsmsg_by_issueid(2))
# print(Queries.get_all_networkerrors())


y = ScriptGenerator()
y.process_sequence(6)

# i = input("solution id: ")
# while i != -1:
#    y.process_sequence(i)
#    i = input("solution id: ")

# z=Logistic()
# z.ranking([1,3,48])

# import csv

# w, x, y, z = 1, 2, 3, 4
# csvRow = [w, x, y, z]
# csvfile = "../Data/user_issue_history.csv"
# with open(csvfile, "a", newline='') as fp:
#    wr = csv.writer(fp, dialect='excel')
#    wr.writerow(csvRow)


#a = RankingController()
#b = a.process_decisiontree_result({60: '10%', 3: '33%', 29: '25%', 80: '33%', 48: '33%', })
#print(b)
