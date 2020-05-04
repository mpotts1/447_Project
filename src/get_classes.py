import constraint
import src.sql_handler


def room_time_constraint(room, time, duration, day_of_week):
    if room.is_empty(time, duration, day_of_week):
        return True

def room_size_constraint(room, students):
    if room["room_capacity"] >= students:
        return True

def room_tech_constraint(room):
    return room["room_is_tech"]

def room_type_constraint(room, type):
    if room["room_type"] == type:
        return True

def get_available_room(instructor, students, duration, time, dept, number, section, day_of_week):
    problem = constraint.Problem()
    rooms = src.sql_handler.get_rooms_on_day(time, duration, day_of_week, students, 0, "LECTURE")
    return rooms


    #problem.addVariable(room, rooms)
    

    #solutions = problem.getSolutions()
    #return solutions




#Example
rooms = src.sql_handler.get_rooms()
for room in rooms:
    print(room)
    #Individual element
    print(room["room_building"])

#classes = src.sql_handler.get_list_classes()
#print(classes)