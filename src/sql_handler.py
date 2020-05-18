import mysql.connector


def get_rooms():
    cnx = mysql.connector.connect(user='user', password='team_terminal', host='96.244.68.135', port=3306,
                                  database='SCHEDULER', buffered=True)
    db = cnx.cursor()

    db.execute("SELECT * FROM room")


    rooms = []

    for room in db:
        temp_room = {"room_building": room[0],
                     "room_num": room[1],
                     "room_capacity": int(room[2]),
                     "room_is_tech": room[3],
                     "room_type": room[4]
                     }
        rooms.append(temp_room)
    db.close()
    cnx.close()
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

    duration = dur_convert(dur)
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
    db.close()
    cnx.close()
    return classes

#This function takes in a class dict and adds a field containing a list of the days of the week on which that
#class occurs
#Assumes _class is a dict with at least the the fields for department, number, and section
def get_class_day(_class):
    cnx = mysql.connector.connect(user='user', password='team_terminal', host='96.244.68.135', port=3306,
                                  database='SCHEDULER', buffered=True)
    db = cnx.cursor()

    data = {
        'dept' : _class["dept"],
        'num' : _class["number"],
        'sect' : _class["section"],
        }

    query = ("SELECT c_day "
             "FROM class_day "
             "WHERE c_dept = %(dept)s AND c_number = %(num)s AND c_section = %(sect)s ")

    db.execute(query, data)
    class_days = []
    for c_day in db:
        class_days.append(c_day[0])

    db.close()
    cnx.close()

    _class.update({"days_of_week" : class_days})
    return _class

def delete_class(dept, number, section):
    cnx = mysql.connector.connect(user='user', password='team_terminal', host='96.244.68.135', port=3306,
                                  database='SCHEDULER', buffered=True)
    db = cnx.cursor()

    query = ("DELETE FROM class_day WHERE c_dept = %s and c_number = %s and c_section = %s")
    db.execute(query, (dept, number, section))

    query = ("DELETE FROM class WHERE c_dept = %s and c_number = %s and c_section = %s")
    db.execute(query, (dept, number, section))

    cnx.commit()

    db.close()
    cnx.close()

#delete_class( "CMSC", 421, 5)

#A function that takes in a dict of classes (a solution from room_scheduler) and updates the database
def assign_room(solution):
    cnx = mysql.connector.connect(user='user', password='team_terminal', host='96.244.68.135', port=3306,
                                  database='SCHEDULER', buffered=True)
    db = cnx.cursor()

    for classID in solution:
        temp_class = solution[classID]
        data = {
            'c_dept' : temp_class['dept'],
            'c_number' : temp_class['number'],
            'c_section' : temp_class['section'],
            'r_building' : temp_class['room_buidling'],
            'r_no' : temp_class['room_num']
            }
        query = 'UPDATE class SET r_building= %(r_building)s, r_no = %(r_no)s WHERE (c_dept = %(c_dept)s AND c_number = %(c_number)s AND c_section = %(c_section)s)'
        db.execute(query, data)
    
    cnx.commit()
    db.close()
    cnx.close()

def dur_convert(dur):

    if(dur == 50):
        return "00:50:00"

    if(dur == 75):
        return "01:05:00"

    if(dur == 150):
        return "02:30:00"

    return "00:00:00"