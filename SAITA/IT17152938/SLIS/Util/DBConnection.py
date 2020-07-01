import mysql.connector
from Data.Veriables import sql_server, sql_db, sql_uname, sql_password
from Data.Log import *
from mysql.connector.errors import *


class DBConnection(object):
    mydb = None

    @classmethod
    def get_connection(cls, new=False):
        if new or not cls.mydb:
            try:
                cls.mydb = mysql.connector.connect(
                    host=sql_server,
                    user=sql_uname,
                    passwd=sql_password,
                    database=sql_db,
                )
                add_log(log_types[2], "DBConnection", "Create new DB object")
            except TimeoutError as err:
                add_log(log_types[0], "DBConnection", "TimeoutError : "+str(err))
            except InterfaceError as err:
                add_log(log_types[0], "DBConnection", "InterfaceError : " + str(err))
            except AttributeError as err:
                add_log(log_types[0], "DBConnection", "AttributeError : " + str(err))
            except ProgrammingError as err:
                add_log(log_types[0], "DBConnection", "ProgrammingError : " + str(err))

        return cls.mydb

    @classmethod
    def execute_query(cls, query, value, dic=True):
        """execute query on singleton db connection"""
        add_log(log_types[2], "DBConnection", "values : "+str(value)+"  query :  "+str(query))
        connection = cls.get_connection()
        try:
            cursor = connection.cursor(dictionary=dic)
        except mysql.ProgrammingError:
            add_log(log_types[0], "DBConnection", "Get cursor so create new connection")
            connection = cls.get_connection(new=True)  # Create new connection
            cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query, value)
            result = cursor.fetchall()
        except ProgrammingError as err:
            add_log(log_types[0], "DBConnection", "ProgrammingError : " + str(err))
            result = ""

        cursor.close()
        return result
