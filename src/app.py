import flask

from flask import Flask
from flask import request, render_template, redirect, url_for

from src.input import get_rooms_available
from src.input import add_class
from src.input import remove_class
from src.sql_handler import get_list_classes

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

@app.route("/getRooms/")
def getListRooms():
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
        days += "TUES,"
    if request.args.get('wednesday') == "on":
        days += "WED,"
    if request.args.get('thursday') == "on":
        days += "THURS,"
    if request.args.get('friday') == "on":
        days += "FRI"
    day_of_week = days.split(",")
    print(days)
    result = get_rooms_available(instructor, students, duration, time, dept, number, section, day_of_week)
    print(day_of_week)
    return render_template('rooms.html', rooms = result, instr = instructor, stud = students, dur = duration, tim = time, dep = dept, num = number, sect = section, day = days)

#Example http request
#http://127.0.0.1:5000/getRooms?instructor=TestInstr&students=20&duration=90&time=12:30&dept=CMSC&number=447&section=1&day_of_week=MON,WED

@app.route("/addClass/")
def addClass():
    instructor = request.args.get('instructor')
    students = int(request.args.get('students'))
    duration = request.args.get('duration')
    time = request.args.get('time')
    dept = request.args.get('dept')
    number = request.args.get('number')
    section = int(request.args.get('section'))
    day_of_week = request.args.get('day_of_week').split(",")
    room_building = request.args.get('r_building')
    room_number = request.args.get('r_number')
    print(request.args.get('day_of_week'))
    #print(day_of_week)
    result = add_class(instructor, students, duration, time, dept, number, section, room_building, room_number, day_of_week)

    return redirect(url_for('home'))

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

    return render_template('removeClass.html', classes = result)

if __name__ == "__main__":
    app.run()