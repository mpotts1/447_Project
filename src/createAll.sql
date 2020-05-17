-- Scheduler database for 447-05 spring 2020 project
-- Written by Joey Slovick for Team 1/Team Terminal

-- createAll: creates the database itself, all relevant tables, and any necessary triggers or views

-- Last modified date: 2020-03-28

create database SCHEDULER;

use SCHEDULER;

create table room(
	r_building		enum("SHER","FA","PAHB","ENGR","CHEM","SOND","ITE","BIO","ILSB","M/P","PHYS","PUP","UC","TRC", "AD","RAC","LH1","LIB"),
    r_no			varchar(4), check (r_no between "001" and "599Z"),
    r_capacity		numeric(3,0), check (r_capacity is not null), check (r_capacity > 0),
    r_tech			bool,
    r_type			enum ("ACTVLRN","LECTURE","COMPLAB","THEATER","SEMINAR"),
    primary key(r_building, r_no)
    );
    
create table class(
	c_instructor	varchar(50),
    c_students		numeric(3,0), check (c_students is not null), check (c_students >= 0),
    c_duration		time,
    
    -- Note that the string format of time ("HH:MM:SS") is retrieved by default; adding to numeric 0 (as in the check clause above) results in the below formats
    -- Examples:
    
    -- format: 			HHMMSS
    -- 50 minutes: 		005000
    -- 75 minutes: 		011500
    -- 150 minutes: 	023000
    
    
    c_start_time	time, check (c_start_time+0 between 080000 and 220000),
    
    -- Examples:
    
    -- format:	HHMMSS
	-- 9am: 	090000
    -- 11:30am: 113000
    -- 2pm: 	140000
    -- 5:15pm: 	171500
    
    -- Note that attributes of the time datatype can be added together, so the end time can be derived by adding start time to duration
    
    -- Examples:
    
    -- 9am start time, 50 min = 	090000 + 005000 = 095000 (9:50am end time)
    -- 11:30am start time, 150 min =113000 + 023000 = 140000 (2pm end time)
    
    check (ADDTIME(c_start_time,c_duration)+0 < 215000), -- per the customer question document, classes scheduled through 9:50pm
    
    c_dept			varchar(4),
    c_number		varchar(4), check (c_number between "100" and "999Z"),
    c_section		numeric(2,0), check (c_section > 0),
    
	r_building		enum("SHER","FA","PAHB","ENGR","CHEM","SOND","ITE","BIO","ILSB","M/P","PHYS","PUP","UC","TRC", "AD","RAC","LH1","LIB"),
    r_no			varchar(4), check (r_no between "001" and "599Z"),
    foreign key (r_building, r_no) references room(r_building, r_no),
    
    primary key(c_dept, c_number, c_section)
    );
    
create table class_day(
    c_dept			varchar(4),
    c_number		varchar(4), check (c_number between "100" and "999Z"),
    c_section		numeric(2,0), check (c_section > 0),
    c_day			enum("MON","TUE","WED","THU","FRI"),
    foreign key (c_dept, c_number, c_section) references class(c_dept, c_number, c_section)
    );
    
create view c_d as select * from class join class_day using (c_dept, c_number, c_section);