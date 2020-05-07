import mysql.connector
from Data.Veriables import sql_server, sql_db, sql_uname, sql_password
from Data.Log import *


class DBConnection(object):
    mydb = None

    @classmethod
    def get_connection(cls, new=False):
        """Creates return new Singleton database connection"""
        if new or not cls.mydb:
            cls.mydb = mysql.connector.connect(
                host=sql_server,
                user=sql_uname,
                passwd=sql_password,
                database=sql_db,
            )
            add_log(log_types[2], "DBConnection", "Create new DB object")

        return cls.mydb

    @classmethod
    def execute_query(cls, query, value):
        """execute query on singleton db connection"""
        add_log(log_types[2], "DBConnection", "values : "+str(value)+"  query :  "+str(query))
        connection = cls.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
        except mysql.ProgrammingError:
            add_log(log_types[0], "DBConnection", "Get cursor so create new connection")
            connection = cls.get_connection(new=True)  # Create new connection
            cursor = connection.cursor(dictionary=True)
        cursor.execute(query, value)
        result = cursor.fetchall()
        cursor.close()
        return result
