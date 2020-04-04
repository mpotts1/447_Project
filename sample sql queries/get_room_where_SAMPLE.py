# need to (pip) install mysql-connector-python

import mysql.connector
cnx = mysql.connector.connect(user = 'user', password = 'team_terminal', host = '96.244.68.135', port = 3306, database = 'SCHEDULER')
db = cnx.cursor()

##

 # data hardcoded for this example; could replace with variables populated earlier
data = {
    'nTime' : "14:00:00",
    'nDur'  : "00:50:00",
    'day1'  : "MON",
    'day2'  : "WED",
    'day3'  : "FRI",
    'minCap': 30,
    'nTech' : 0,
    'nType' : "LECTURE"
}

#The nested SQL query, starting with the SELECT statement on line 27, selects all rooms that are disqualified due to time overlap with another class
#The outer SQL query, starting with the SELECT statement on line 24, selects all rooms that match the capacity and type constraints that are not in the product of the nested query

query = ("SELECT r_building as building, r_no as num "
         "FROM room "
         "WHERE r_tech = %(nTech)s AND r_capacity >= %(minCap)s AND r_type = %(nType)s AND (r_building, r_no) NOT IN ("
             "SELECT r_building, r_no "
             "FROM c_d "
             "WHERE (c_day = %(day1)s OR c_day = %(day2)s OR c_day = %(day3)s) AND "
                 "((TIMEDIFF(c_start_time, %(nTime)s)+0 >= 0 AND TIMEDIFF(ADDTIME(%(nDur)s, %(nTime)s), c_start_time)+0 > 0) OR "
                 "(TIMEDIFF(%(nTime)s, c_start_time)+0 >= 0 AND TIMEDIFF(ADDTIME(c_duration, c_start_time), %(nTime)s)+0 > 0)))")

# 4 scenarios can disqualify a room based on time overlap with another class:

# 1) The new class starts before and ends during an existing class
# 2) The new class starts during and ends after an existing class
# 3) The new class starts before and ends after an existing class ("surrounding" it)
# 4) The new class starts after and ends before an existing class ("surrounded by" it)
                                             
# 1 and 3 are handled by the statement on line 30
# 2 and 4 are handled by the statement on line 31
                                             
# Edge cases: If one class ends exactly at the start time of another, it is not caught by the nested statement, so the outer statement is allowed to select it

# This query can be altered for use by 1 or 2 day classes by removing 'OR c_day = %(day#)s' from the statement on line 29 and the entry in the dictionary, labeled in this sample as 'data'
# This query can be altered to allow laxer requests (ie r_tech doesn't matter) by removing the unneeded entry from line 26 and the corresponding entry from the dictionary

db.execute(query, data)

print('Availible rooms: ')

for(building, num) in db:
    print(str(building) + ' ' + str(num))
    
###

db.close()
cnx.close()