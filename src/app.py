import flask

from flask import Flask
from flask import request, render_template, redirect, url_for

from src.input import get_rooms_available
from src.input import add_class
from src.input import remove_class
from src.sql_handler import assign_room, get_list_classes, get_rooms, get_class_day
from src.room_scheduler import room_scheduler, find_best_solution_by_class_size

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/inputNewClass/")
def inputNewClass():
    return render_template('addClass.html')

@app.route("/inputOldClass/")
def inputOldClass():
    return render_template('removeClass.html')

@app.route("/scheduleify/")
def scheduleify():
    classes = get_list_classes()
    for _class in classes:
        get_class_day(_class)
    rooms = get_rooms()
    #print(classes)
    #print(rooms)
    solutions = room_scheduler(rooms, classes)
    #print(solutions)
    best = find_best_solution_by_class_size(solutions)
    print(best)
    assign_room(best)
    return render_template(url_for('displayClasses'))

@app.route("/addClass/")
def addClass():
    instructor = request.args.get('instructor')
    students = int(request.args.get('students'))
    duration = int(request.args.get('duration'))
    time = request.args.get('time')
    dept = request.args.get('dept')
    number = request.args.get('number')
    section = int(request.args.get('section'))
    days = ""
    if request.args.get('monday') == "on":
        days += "MON,"
    if request.args.get('tuesday') == "on":
        days += "TUE,"
    if request.args.get('wednesday') == "on":
        days += "WED,"
    if request.args.get('thursday') == "on":
        days += "THU,"
    if request.args.get('friday') == "on":
        days += "FRI,"
    days = days[0:-1]
    day_of_week = days.split(",")
    #print(days)
    add_class(instructor, students, duration, time, dept, number, section, None, None, day_of_week)
    #print(day_of_week)
    return redirect(url_for('home'))

#Example http request
#http://127.0.0.1:5000/getRooms?instructor=TestInstr&students=20&duration=90&time=12:30&dept=CMSC&number=447&section=1&day_of_week=MON,WED


@app.route("/displayClasses/")
def displayClasses():
    result = get_list_classes()
    return render_template('displayClasses.html', classes = result)

@app.route("/removeClass/")
def removeClass():
    dept = request.args.get('dept')
    number = request.args.get('number')
    section = int(request.args.get('section'))

    result = remove_class(dept, number, section)
    print(result)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()