#Get Input from UI

#Basic class functions

'''Data needed -
    CLASS
	c_instructor	varchar(30),
    c_students		numeric(3,0),
    c_duration		numeric(3,0), -- expects duration in minutes
    c_start_time	time,
    c_dept			varchar(4),
    c_number		varchar(4), check (c_number between "100" and "999Z"),
    c_section		numeric(2,0), check (c_section >= 0),

    CLASS DAY
    dayOfWeek		varchar(9), check(dayOfWeek in("Monday","Tuesday","Wednesday","Thursday","Friday")),
    '''

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

    #Call some other function here to generate constraints,


#parameter is a single element in the return from get_class_available
def add_class():



''' need primary key(c_dept, c_number, c_section) '''
def remove_class(dept, number, section):
    print("Remove Class")


def modify_class():
    print("Modify Class")



#Test/Example Function input
#Good
#get_class_available("Test Instructor", 3, 90, "12:30","CMSC", "447", 0, ["Monday", "Wednesday"])

#Bad
#get_class_available("Test Instructor", "3", "90", 1230, "CMSC", 447, "0", "[Monday,Wednesday]")