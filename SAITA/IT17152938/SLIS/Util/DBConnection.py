import mysql.connector
from Data.Veriables import *


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

        return cls.mydb

    @classmethod
    def execute_query(cls, query, value):
        """execute query on singleton db connection"""
        connection = cls.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
        except mysql.ProgrammingError:
            connection = cls.get_connection(new=True)  # Create new connection
            cursor = connection.cursor(dictionary=True)
        cursor.execute(query, value)
        result = cursor.fetchall()
        cursor.close()
        return result
