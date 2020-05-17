import constraint
import src.sql_handler
import datetime

room_dict = {}

#A constraint function to check if the room is a sufficient size
def room_size_cons(*class_args):
    room_size_met = True
    for _class in class_args:
        room = room_dict[get_roomID(_class)]
        if room['room_capacity'] < _class['students']:
            room_size_met = False
            break
    if room_size_met:
        return True

#A constraint function to check if a room is the correct type (Not implemented)
def room_type_cons(*class_args):
    room_type_met = True
    for _class in class_args:
        roomID = get_roomID(_class)
        room = room_dict[roomID]
        if room['room_type'] != _class['room_type']:
            room_type_met = False
            break
    if room_type_met:
        return True

#A constraint function to see avoid double booking a class
def double_book_room_cons(*class_args):
    double_book_room_met = True
    weekdays = ["MON", "TUE", "WED", "THU", "FRI"]
    buffer = datetime.timedelta(0, 600)
    for class1 in class_args:
        for class2 in class_args:
            if get_classID(class1) != get_classID(class2):
                for day in weekdays:
                    if day in class1['days_of_week'] and day in class2['days_of_week']:
                        class1_start = class1['start_time']
                        class1_dur = class1['duration']
                        class1_end = class1_start + class1_dur
                        class2_start = class2['start_time']
                        class2_dur = class2['duration']
                        class2_end = class2_start + class2_dur
                        if class1_start > class2_start and class1_start < class2_end + buffer:
                            double_book_room_met = False
                            break
                        if class2_start > class1_start and class2_start < class1_end + buffer:
                            double_book_room_met = False
                            break
    if double_book_room_met:
        return True

#A function that populates a global dict of all rooms so that functions can get room data
def populate_room_dict(rooms):
    global room_dict
    for room in rooms:
        roomID = get_roomID(room)
        room_dict.update({roomID : room})

#A function that can create a roomID string from class or room dicts
def get_roomID(dict):
    return str(dict['room_building']) + str(dict['room_num'])

#A function that can create a classID from a class dict
def get_classID(_class):
    return str(_class['dept']) + str(_class['number']) + ':' + str(_class['section'])

#A function to print solutions in a pleasing format
#The format is: ClassID: RoomID
def print_solution(solution):
    for classID in solution:
        print("{} : {}".format(classID, get_roomID(solution[classID])))

#This function takes in a list of room and class dicts and returns all of the configurations
# of classes and rooms within the constraints
#It is assumed that the class dicts are populated with all fields other than r_building and r_number
def room_scheduler(rooms, classes):
    populate_room_dict(rooms)
    problem = constraint.Problem()
    class_list = []
    for _class in classes:
        classID = get_classID(_class)
        class_list.append(classID)
        class_rooms = []
        if get_roomID(_class) != 'NoneNone' or get_roomID(_class) != 'NullNull':
            temp_class = {}
            for key in _class.keys():
                temp_class.update({key : _class[key]})
            class_rooms.append(temp_class)
        else:
            for room in rooms:
                temp_class = {}
                for key in _class.keys():
                    temp_class.update({key : _class[key]})
                temp_class.update({'room_building' : room['room_building']})
                temp_class.update({'room_num' : room['room_num']})
                class_rooms.append(temp_class)
        problem.addVariable(str(classID), class_rooms)

    problem.addConstraint(room_size_cons, class_list)
    problem.addConstraint(double_book_room_cons, class_list)
    
    solutions = problem.getSolutions()

    return solutions

def get_class_utilization(solution):
    unoccupied_seat_rating = 0
    for classID in solution:
        temp_class = solution[classID]
        class_size = temp_class['students']
        roomID = get_roomID(solution[classID])
        temp_room = room_dict[roomID]
        room_capacity = temp_room['room_capacity']
        unoccupied_seat_rating += room_capacity - class_size
    return unoccupied_seat_rating

def solution_sort_by_class_size():
