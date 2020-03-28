-- Scheduler database for 447-05 spring 2020 project
-- Written by Joey Slovick for Team 1/Team Terminal

-- createAll: creates the database itself, all relevant tables, and any necessary triggers or views

-- Last modified date: 2020-03-08

create database SCHEDULER;

use SCHEDULER;

create table room(
	r_building		varchar(4), check (r_building in("SHER","FA","PAHB","ENGR","CHEM","SOND","ITE","BIO","ILSB","M/P","PHYS","PUP","UC","TRC", "AD","RAC","LH1","LIB")),
    r_no			varchar(5), check (r_no between "001" and "599Z"),
    r_capacity		numeric(3,0), check (r_capacity is not null),
    r_tech			bool,
    r_type			varchar(7), check (r_type in("ActvLrn","Lecture","CompLab","Theater")),
    primary key(r_building, r_no)
    );
    
create table class(
	c_instructor	varchar(30),
    c_students		numeric(3,0),
    c_duration		numeric(3,0), -- expects duration in minutes
    c_start_time	time,
    c_dept			varchar(4),
    c_number		varchar(4), check (c_number between "100" and "999Z"),
    c_section		numeric(2,0), check (c_section >= 0),
    primary key(c_dept, c_number, c_section)
    );
    
create table class_day(
    c_dept			varchar(4),
    c_number		varchar(4), check (c_number between "100" and "999Z"),
    c_section		numeric(2,0), check (c_section >= 0),
    dayOfWeek		varchar(9), check(dayOfWeek in("Monday","Tuesday","Wednesday","Thursday","Friday")),
    foreign key (c_dept, c_number, c_section) references class(c_dept, c_number, c_section)
    );
    
create table occupies(
	r_building		varchar(7), check (r_building in("SHER","FA","PAHB","ENGR","CHEM","SOND","ITE","BIO","ILSB","M/P","PHYS","PUP","UC","TRC", "AD","RAC","LH1","LIBRARY")),
    r_no			varchar(5), check (r_no between "001" and "599Z"),
    c_dept			varchar(4),
    c_number		varchar(4), check (c_number between "100" and "999Z"),
    c_section		numeric(2,0), check (c_section >= 0),
    foreign key (r_building, r_no) references room(r_building, r_no),
    foreign key (c_dept, c_number, c_section) references class(c_dept, c_number, c_section)
    );