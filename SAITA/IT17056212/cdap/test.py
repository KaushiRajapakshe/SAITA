# from Controllers.Query import Queries
# from Util.DBConnection import DBConnection
# import ctypes
# import datetime
# from tkinter import*
# from win32api import GetMonitorInfo, MonitorFromPoint
from Util.ScriptGenerator import ScriptGenerator

# x = '2'
# print(DBConnection.select_query("SELECT error_msg,error_code,connection_type,issue_id FROM network_errors_msg"))
# print(DBConnection.select_param_query('SELECT error_msg FROM network_errors_msg where issue_id=%s', (x,)))
# print(Queries.get_errorsmsg_by_issueid(2))
# print(Queries.get_all_networkerrors())


y = ScriptGenerator()
y.process_sequence(6)

#i = input("solution id: ")
#while i != -1:
#    y.process_sequence(i)
#    i = input("solution id: ")
