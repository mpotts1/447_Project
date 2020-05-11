import mysql.connector


def get_rooms():
    cnx = mysql.connector.connect(user='user', password='team_terminal', host='96.244.68.135', port=3306,
                                  database='SCHEDULER', buffered=True)
    db = cnx.cursor()
    db.execute("SELECT * FROM room")
    db.close()
    cnx.close()

    rooms = []
    for room in db:
        temp_room = {"room_building": room[0],
                     "room_num": room[1],
                     "room_capacity": int(room[2]),
                     "room_is_tech": room[3],
                     "room_type": room[4]
                     }
        rooms.append(temp_room)
    return rooms


def get_rooms_on_day(start_time, dur, days, capacity, is_tech, class_type):
    
    cnx = mysql.connector.connect(user='user', password='team_terminal', host='96.244.68.135', port=3306,
                                  database='SCHEDULER', buffered=True)
    db = cnx.cursor()

    for day in days:

        data = {
            'nTime': start_time,
            'nDur': dur,
            'day': day,
            'minCap': capacity,
            'nTech': is_tech,
            'nType': class_type
        }

        query = ("SELECT r_building as building, r_no as num "
                 "FROM room "
                 "WHERE r_tech = %(nTech)s AND r_capacity >= %(minCap)s AND r_type = %(nType)s AND (r_building, r_no) NOT IN ("
                 "SELECT r_building, r_no "
                 "FROM c_d "
                 "WHERE (c_day = %(day)s) AND "
                 "((TIMEDIFF(c_start_time, %(nTime)s)+0 >= 0 AND TIMEDIFF(ADDTIME(%(nDur)s, %(nTime)s), c_start_time)+0 > 0) OR "
                 "(TIMEDIFF(%(nTime)s, c_start_time)+0 >= 0 AND TIMEDIFF(ADDTIME(c_duration, c_start_time), %(nTime)s)+0 > 0)))")

        db.execute(query, data)

    rooms = []
    for room in db:
        rooms.append(room)

    db.close()
    cnx.close()

    return rooms

#Example
#get_rooms_on_day(start_time="14:00:00", dur= "00:50:00", days=["MON", "WED"], capacity=30, is_tech=0, class_type="LECTURE")


def add_class(instructor, capacity, dur, start_time, dept, class_number, section, room_building, room_number, days):

    cnx = mysql.connector.connect(user='user', password='team_terminal', host='96.244.68.135', port=3306,
                                  database='SCHEDULER', buffered=True)
    db = cnx.cursor()

    duration = "00:"+str(dur)+":00"
    class_data = (instructor, capacity, duration, start_time, dept, class_number, section, room_building, room_number)

    query = ("INSERT INTO class VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    db.execute(query, class_data)

    for day in days:

        query = ("INSERT INTO class_day VALUES(%s, %s, %s, %s)")
        db.execute(query, (dept, class_number, section, day))

    cnx.commit()
    db.close()
    cnx.close()

#Example
#add_class("Test_instr", 222, 50, "8:00:00", "CMSC", "111", 1, "PUP","105", ["MON", "WED", "FRI"])

def get_list_classes():
    cnx = mysql.connector.connect(user='user', password='team_terminal', host='96.244.68.135', port=3306,
                                  database='SCHEDULER', buffered=True)
    db = cnx.cursor()
    db.execute("SELECT * FROM class")

    classes = []
    for _class in db:
        temp_class = {"instructor": _class[0],
                      "students": int(_class[1]),
                      "duration": _class[2],
                      "start_time": _class[3],
                      "dept": _class[4],
                      "number": _class[5],
                      "section": int(_class[6]),
                      "room_building": _class[7],
                      "room_num": _class[8]
                     }
        classes.append(temp_class)
        #print(temp_class["class_instructor"])
    db.close()
    cnx.close()
    return classes
