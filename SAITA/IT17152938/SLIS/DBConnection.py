import mysql.connector


class DBConnection(object):
    mydb = None

    @classmethod
    def get_connection(cls, new=False):
        """Creates return new Singleton database connection"""
        if new or not cls.mydb:
            cls.mydb = mysql.connector.connect(
                host="192.168.1.102",
                user="root",
                passwd="passw0rd",
                database="saita_slis_db",
            )

        return cls.mydb

    @classmethod
    def execute_query(cls, query, value):
        """execute query on singleton db connection"""
        connection = cls.get_connection()
        try:
            cursor = connection.cursor()
        except mysql.ProgrammingError:
            connection = cls.get_connection(new=True)  # Create new connection
            cursor = connection.cursor()
        cursor.execute(query,value)
        result = cursor.fetchall()
        cursor.close()
        return result
