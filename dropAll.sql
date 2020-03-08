-- Scheduler database for 447-05 spring 2020 project
-- Written by Joey Slovick for Team 1/Team Terminal

-- dropAll: deletes all database elements and the database itself
-- For testing purposes only.

-- Last modified date: 2020-03-08

use SCHEDULER;

drop table occupies;
drop table class_day;
drop table class;
drop table room;

drop database SCHEDULER;