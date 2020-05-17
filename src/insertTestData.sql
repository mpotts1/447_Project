-- Scheduler database for 447-05 spring 2020 project
-- Written by Joey Slovick for Team 1/Team Terminal

-- insertTestData: inserts valid data into existing tables

-- Last modified date: 2020-03-28

use SCHEDULER;

-- 						build	num		cap		tech	type
insert into room values("PUP",	"105",	120,	false,	"LECTURE");
insert into room values("ENGR",	"122",	100,	true,	"LECTURE");
insert into room values("ENGR",	"122A",	100,	true,	"LECTURE");
insert into room values("ITE",	"227",	60,		false,	"THEATER");
insert into room values("ILSB",	"237",	60,		true,	"ACTVLRN");
insert into room values("SOND",	"109",	50,		false,	"SEMINAR");
insert into room values("CHEM",	"030",	50,		false,	"LECTURE");
insert into room values("SHER",	"014",	50,		false,	"SEMINAR");
insert into room values("BIO",	"120",	40,		false,	"THEATER");
insert into room values("ILSB",	"233",	40,		true,	"ACTVLRN");
insert into room values("M/P",	"106",	40,		false,	"THEATER");
insert into room values("SHER",	"013",	40,		false,	"SEMINAR");
insert into room values("SHER",	"151",	30,		false,	"SEMINAR");

select * from c_d group by c_day order by c_start_time asc;
select * from room;