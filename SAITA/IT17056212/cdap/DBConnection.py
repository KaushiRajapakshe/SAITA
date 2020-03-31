import pymysql

# Open database connection
db = pymysql.connect("localhost", "root", "12345", "saita")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)


def select_query(query):
    # print(query)
    sql = query
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


y = select_query("SELECT nq_one,nq_two,nq_three,nq_four,category FROM network_categorizer")
# z = select_query("SELECT error_msg,error_code,connection_type,issue_id FROM network_errors_msg")
# for row in results:
#    fname = row[1]


# disconnect from server
db.close()
