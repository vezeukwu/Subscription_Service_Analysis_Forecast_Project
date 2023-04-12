use project;
select * from actions2load;

#The most common events = ReadingOwnedBook with a count of 24628
SELECT event_type, COUNT(*) as frequency FROM actions2load group BY event_type order by frequency desc; 

#The least common events  = UnknownOriginLivebookLinkOpened
SELECT event_type, COUNT(*) as frequency FROM actions2load group BY event_type order by frequency asc;

#Account id with the highest number of event = caffe2b03e6057845c52212acaaa1a34	1574
SELECT account_id, count(*) as frequency FROM actions2load group by account_id order by frequency desc;

#Account ids with the least number of event 
SELECT account_id, count(*) as frequency FROM actions2load group by account_id order by frequency asc;

#How many times events occurred based on different times of the day
SELECT event_time, EXTRACT(HOUR FROM event_time) AS hour FROM actions2load;
SELECT TIME(datetime_column) AS time FROM table_name;

SELECT event_type, event_time, time(event_time) AS time_of_day FROM actions2load;
select time_format((event_time), '%H:%i') as time_of_day, count(*) as event_count from actions2load group by time_of_day order by time_of_day;

