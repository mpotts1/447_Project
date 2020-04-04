# need to (pip) install mysql-connector-python

import mysql.connector
cnx = mysql.connector.connect(user = 'user', password = 'team_terminal', host = '96.244.68.135', port = 3306, database = 'SCHEDULER')
db = cnx.cursor()

daily_open_time = (21+50/60) - 8 # per the customer specifications, class scheduled from 8am to 9:50pm

###

# hardcoded SOND 301 as an example; could replace with variables populated earlier

building = 'SOND'
room = '301'

select_room = ("SELECT HOUR(c_duration)+0 AS hr, MINUTE(c_duration)+0 AS mi, SECOND(c_duration)+0 AS sec FROM (c_d JOIN room USING (r_building, r_no)) WHERE (r_building = %s and r_no = %s)")

db.execute(select_room, (building, room)) 
aggregate = 0.0

for(hr, mi, sec) in db:
    aggregate += float(hr) + float(mi)/60 + float(sec)/60/60
    
percent = 100*aggregate/daily_open_time/5 # divide by 5 because aggregate includes all 5 days in this example

print('Utilization for room ' + building + ' ' + room + ': ' + str(percent) + '%')
###

db.close()
cnx.close()