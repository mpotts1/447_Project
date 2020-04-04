import mysql.connector

class Room:


    def __init__(self, building, num, capacity, tech, type):
        self.building = building
        self.num = num
        self.capacity = capacity
        self.tech = tech
        self.type = type

    def is_empty(self, time, duration, day_of_week):
        isEmpty = True
        cnx = mysql.connector.connect(user = 'user', password = 'team_terminal', host = 'localhost', port = 3306, database = 'SCHEDULER', buffered = True)
        db = cnx.cursor()
        query = "SELECT (c_start_time, c_duration) FROM c_d WHERE c_day = %s"
        for day in day_of_week:
            c_day = day
            db.execute(query, (c_day))
            for (c_start_time, c_duration) in db: