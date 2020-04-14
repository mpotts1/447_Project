import flask

from flask import Flask
from flask import request

from src.input import get_rooms_available



app = Flask(__name__)

@app.route("/")
def no_func():
    return "Flask app is running"


@app.route("/getRooms/")
def get_list_rooms():
    instructor = request.args.get('instructor')
    students = int(request.args.get('students'))
    duration = int(request.args.get('duration'))
    time = request.args.get('time')
    dept = request.args.get('dept')
    number = request.args.get('number')
    section = int(request.args.get('section'))
    day_of_week = request.args.get('day_of_week').split(",")
    result = get_rooms_available(instructor, students, duration, time, dept, number, section, day_of_week)

    return flask.jsonify(result)

#Example http request
#http://127.0.0.1:5000/getRooms?instructor=TestInstr&students=20&duration=90&time=12:30&dept=CMSC&number=447&section=1&day_of_week=MON,WED

if __name__ == "__main__":
    app.run()