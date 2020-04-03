# need to (pip) install mysql-connector-python

import mysql.connector
cnx = mysql.connector.connect(user = 'user', password = 'team_terminal', host = 'localhost', port = 3306, database = 'SCHEDULER')
db = cnx.cursor()

schedule_begin_time = 080000 # doors open at 8am, as per the customer questions
schedule_end_time = 220000 # doors close at 10pm, as per the customer questions

###

select_room = ("SELECT (c_duration+0) FROM (c_d JOIN room USING (r_building, r_no)) where (r_building = %s and r_no = %s)")

db.execute(select_room, ('ITE', '201')) # hardcoded ITE 201 as an example; could replace literals with variables populated earlier

count = 0
for(c_duration) in db:
    count += c_duration
    
    
percent = count/(schedule_end_time-schedule_begin_time)/5 # divide by 5 because count includes all 5 days

###

db.close()
cnx.close()

