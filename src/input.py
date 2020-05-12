import src.sql_handler


def get_rooms_available(instructor, students, duration, time, dept, number, section, day_of_week):

    _input = {"instructor": instructor, "students": students, "duration": duration, "time": time, "dept": dept, "number": number, "section": section, "day_of_week": day_of_week}

    data_types = {
        "instructor": str,
        "students": int,
        "duration": int,
        "time": str,
        "dept": str,
        "number": str,
        "section": int,
        "day_of_week": list
    }

    invalid_data = []
    for key in data_types.keys():
        if not(isinstance(_input[key], data_types[key])):
            print(data_types[key], type(_input[key]))
            invalid_data.append(key)

    if(len(invalid_data) > 0):
        return invalid_data

    #Will return a list of all available rooms from constraints
    return src.sql_handler.get_rooms_on_day(time, duration, day_of_week, students, 0, "LECTURE")

#parameter is a single element in the return from get_class_available
def add_class(instructor, capacity, dur, start_time, dept, class_number, section, room_building, room_number, days):
    return(src.sql_handler.add_class(instructor, capacity, dur, start_time, dept, class_number, section, room_building, room_number, days))

''' need primary key(c_dept, c_number, c_section) '''
def remove_class(dept, number, section):
    print("Remove Class")


def modify_class(dept, number, section):
    print("Modify Class")



#Test/Example Function input
#Good
#get_class_available("Test Instructor", 3, 90, "12:30","CMSC", "447", 0, ["MON", "WED"])

#Bad
#get_class_available("Test Instructor", "3", "90", 1230, "CMSC", 447, "0", "[Monday,Wednesday]")