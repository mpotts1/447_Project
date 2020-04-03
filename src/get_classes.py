import constraint
import src.sql_handler

def time_room_constraint(room, time, duration, day_of_week):
    if room.isEmpty(time, duration, day_of_week):
        return True

def get_available_class(instructor, students, duration, time, dept, number, section, day_of_week):
    problem = constraint.Problem()

    #problem.addVariable("room", [set of rooms]) #"Set of rooms" will be replaced by the column of rooms

    problem.addConstraint(time_room_constraint, ["time", "room", "duration", "day_of_week"])

    solutions = problem.getSolutions()
    return solutions




#Example
rooms = src.sql_handler.get_rooms()
for room in rooms:
    print(room)
    #Individual element
    print(room["room_building"])

classes = src.sql_handler.get_list_classes()
print(classes)