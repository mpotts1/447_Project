import constraint
import src.sql_handler
import datetime


def room_size_cons(classes):
    for _class in classes:
        room = room_dict[get_roomID(_class)]
        if room["room_capacity"] < _class["students"]:
            return False
    return True

def room_type_cons(classes):
    for _class in classes:
        roomID = get_roomID(_class)
        room = room_dict[roomID]
        if room["room_type"] != _class["room_type"]:
            return False
    return True

def double_book_room_cons(classes):
    weekdays = ["MON", "TUE", "WED", "THU", "FRI"]
    buffer = datetime.timedelta(0, 600)
    for class1 in classes:
        for class2 in classes:
            if get_classID(class1) != get_classID(class2):
                for day in weekdays:
                    if day in class1["days_of_week"] and day in class2["days_of_week"]:
                        s_hour1, s_min1, s_sec1 = class1["start_time"].split(':')
                        class1_start = datetime.time(int(s_hour1), int(s_min1), int(s_sec1))
                        d_hour1, d_min1, d_sec1 = class1["duration"].split(':')
                        class1_dur = datetime.timedelta(0, int(d_sec1), 0, 0, int(d_min1), int(d_hour1))
                        class1_end = class1_start + class1_dur
                        s_hour2, s_min2, s_sec2 = class2["start_time"].split(':')
                        class2_start = datetime.time(int(s_hour2), int(s_min2), int(s_sec2))
                        d_hour2, d_min2, d_sec2 = class2["duration"].split(':')
                        class2_dur = datetime.timedelta(0, int(d_sec2), 0, 0, int(d_min2), int(d_hour2))
                        class2_end = class2_start + class2_dur
                        if class1_start > class2_start and class1_start < class2_end + buffer:
                            return False
                        if class2_start > class1_start and class2_start < class1_end + buffer:
                            return False
    return True

def populate_room_dict(rooms):
    global room_dict
    for room in rooms:
        roomID = get_roomID(room)
        roomIDs.update({roomID : room})

def get_roomID(dict):
    return dict["room_building"] + str(dict["room_num"])

def get_classID(_class):
    return _class["dept"] + str(_class["number"]) + ":" + str(_class["section"])

def room_scheduler(rooms, classes):
    populate_room_dict(rooms)
    problem = constraint.Problem()

    global class_dict
    for _class in classes:
        classID = get_classID(_class)
        class_dict.update({classID : _class})
        class_rooms = []
        for room in rooms:
            _class["room_building"] = room["room_building"]
            _class["room_num"] = room["room_num"]
            class_rooms.append(_class)
        problem.addVariable(classID, class_rooms)

    problem.addConstraint(room_size_cons, class_dict.keys())
    problem.addConstraint(double_book_room_cons, class_dict.keys())

    return solutions