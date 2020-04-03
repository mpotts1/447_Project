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


def get_list_classes():
    cnx = mysql.connector.connect(user='user', password='team_terminal', host='96.244.68.135', port=3306,
                                  database='SCHEDULER', buffered=True)
    db = cnx.cursor()
    db.execute("SELECT * FROM class")
    db.close()
    cnx.close()

    classes = []
    for _class in db:
        temp_class = {"class_instructor": _class[0],
                      "class_students": int(_class[1]),
                      "class_duration": _class[2],
                      "class_start_time": _class[3],
                      "class_dept": _class[4],
                      "class_number": _class[5],
                      "class_section": int(_class[6]),
                      "room_building": _class[7],
                      "room_num": _class[8]
                     }

    classes.append(temp_class)
    return classes
