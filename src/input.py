from src.get_classes import get_available_class


def get_class_available(instructor, students, duration, time, dept, number, section, day_of_week):

    input = {"instructor": instructor, "students": students, "duration": duration, "time": time, "dept": dept, "number": number, "section": section, "day_of_week": day_of_week}
    data_types = {
        "instructor" : str,
        "students" : int,
        "duration" : int,
        "time" : str,
        "dept" : str,
        "number" : str,
        "section": int,
        "day_of_week" : list
    }

    invalid_data = []
    for key in data_types.keys():
        if not(isinstance(input[key], data_types[key])):
            print(data_types[key], type(input[key]))
            invalid_data.append(key)

    if(len(invalid_data) > 0):
        return invalid_data

    #Will return a list of all available rooms from constraints
    return get_available_class(instructor, students, duration, time, dept, number, section, day_of_week)

#parameter is a single element in the return from get_class_available
def add_class(TBD):
    print("Add class")
    #Add class to database, return success of failure

''' need primary key(c_dept, c_number, c_section) '''
def remove_class(dept, number, section):
    print("Remove Class")


def modify_class(dept, number, section):
    print("Modify Class")



#Test/Example Function input
#Good
#get_class_available("Test Instructor", 3, 90, "12:30","CMSC", "447", 0, ["Monday", "Wednesday"])

#Bad
#get_class_available("Test Instructor", "3", "90", 1230, "CMSC", 447, "0", "[Monday,Wednesday]")