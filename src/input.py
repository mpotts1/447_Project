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

def add_class(instructor, students, duration, time, dept, number, section, day_of_week):




''' need primary key(c_dept, c_number, c_section) '''
def remove_class(dept, number, section):



def modify_class():

