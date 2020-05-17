-- Scheduler database for 447-05 spring 2020 project
-- Written by Joey Slovick for Team 1/Team Terminal

-- clearTables: deletes all rows from tables, leaves the empty tables themselves (ie you don't need to run the create script again to insert into them)
-- For testing purposes only.

-- Last modified date: 2020-03-28

use SCHEDULER;

set SQL_SAFE_UPDATES = 0;

delete from class_day;
delete from class;
delete from room;

select * from room order by r_building desc, r_no asc;
select * from c_d order by c_start_time asc;