import pymysql
from Data.Variables import *


class DBConnection(object):
    db = None

    # Open database connection
    @classmethod
    def get_connection(cls, new=False):
        if new or not cls.db:
            cls.db = pymysql.connect(sql_server, sql_uname, sql_password, sql_db)

        return cls.db

    # prepare a cursor object using cursor() method

    # execute SQL query using execute() method.
    # cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    # data = cursor.fetchone()
    # print("Database version : %s " % data)

    @classmethod
    def select_query(cls, query):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    @classmethod
    def select_param_query(cls, query, value):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, value)
        results = cursor.fetchall()
        cursor.close()
        return results

    # def param_select_query(query, data):
    #    print(query, data)
    #  sql = query
    #  cursor.execute(sql, data)
    #   results = cursor.fetchall()
    #  return results

# x = 1
# netBinaryData = select_query("SELECT nq_one,nq_two,nq_three,nq_four,category FROM network_categorizer")
# netErrorData = select_query("SELECT error_msg,error_code,connection_type,issue_id FROM network_errors_msg")
# test = param_select_query("SELECT error_msg FROM network_errors_msg where issue_id=$d", x)
# for row in results:
#    fname = row[1]


# disconnect from server
