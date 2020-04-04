# need to (pip) install mysql-connector-python

import mysql.connector
cnx = mysql.connector.connect(user = 'user', password = 'team_terminal', host = '96.244.68.135', port = 3306, database = 'SCHEDULER')
db = cnx.cursor()

##

 # data hardcoded for this example; could replace with variables populated earlier
dept = "CMSC"
course = "202"
sec = 15
class_data = ("Li Chang", 149, "00:50:00","13:00:00",dept,course,sec,"LH1","101")

query = ("INSERT INTO class VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")

db.execute(query, class_data)

query = ("INSERT INTO class_day VALUES(%s, %s, %s, %s)")

db.execute(query, (dept, course, sec, "MON"))
db.execute(query, (dept, course, sec, "WED"))

cnx.commit()

##

db.close()
cnx.close()