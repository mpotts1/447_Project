# need to (pip) install mysql-connector-python

import mysql.connector
cnx = mysql.connector.connect(user = 'user', password = 'team_terminal', host = '96.244.68.135', port = 3306, database = 'SCHEDULER')
db = cnx.cursor()

##

# data hardcoded for this example; could replace with variables populated earlier

dept = "CMSC"
course = "202"
sec = 15

query = ("DELETE FROM class_day WHERE c_dept = %s and c_number = %s and c_section = %s")

db.execute(query,(dept, course, sec))

query =("DELETE FROM class WHERE c_dept = %s and c_number = %s and c_section = %s")

db.execute(query,(dept, course, sec))

cnx.commit()

##

db.close()
cnx.close()