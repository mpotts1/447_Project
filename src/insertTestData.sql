-- Scheduler database for 447-05 spring 2020 project
-- Written by Joey Slovick for Team 1/Team Terminal

-- insertTestData: inserts valid data into existing tables

-- Last modified date: 2020-03-28

use SCHEDULER;

-- 						build	num		cap		tech	type
insert into room values("SOND",	"201",	40,		false,	"ACTVLRN");
insert into room values("SOND",	"202",	45,		false,	"ACTVLRN");
insert into room values("SOND",	"203",	100,	true,	"THEATER");
insert into room values("SOND",	"301",	200,	false,	"LECTURE");

-- 						instructor				studnts	durat	start	dept	class	sec	build	num
insert into class values("Marcus Smith",		31,		011500,	113000,	"CMPE",	"201",	1, 	"SOND", "201");
insert into class values("Jean Perez",			110,	005000,	140000,	"SOCY",	"101",	11, "SOND",	"301");
insert into class values("Maria Ali",			121,	005000,	110000,	"GES",	"110",	6,	"SOND", "301");
insert into class values("Marcus Smith",		28,		011500,	130000,	"CMPE",	"201",	2, 	"SOND", "201");
insert into class values("Rick Johnson",		20,		023000,	143000,	"PHYS",	"122L",	4,	"SOND",	"202");

-- 							dept		class	sec	day
insert into class_day values("CMPE",	"201",	1, 	"MON");
insert into class_day values("CMPE",	"201",	1, 	"WED");
insert into class_day values("SOCY",	"101",	11,	"MON");
insert into class_day values("SOCY",	"101",	11,	"WED");
insert into class_day values("SOCY",	"101",	11,	"FRI");
insert into class_day values("GES",		"110",	6,	"TUE");
insert into class_day values("GES",		"110",	6,	"THU");
insert into class_day values("CMPE",	"201",	2, 	"MON");
insert into class_day values("CMPE",	"201",	2, 	"WED");
insert into class_day values("PHYS",	"122L",	4, 	"THU");

select * from c_d order by c_start_time asc;