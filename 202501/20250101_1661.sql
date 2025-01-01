-- https://leetcode.com/problems/average-time-of-process-per-machine/

-- # Write your MySQL query statement below

select Activity.machine_id, round(avg(a.timestamp - Activity.timestamp), 3) as processing_time
from Activity
join Activity as a
on Activity.machine_id = a.machine_id and Activity.process_id = a.process_id
and Activity.activity_type = 'start' and a.activity_type = 'end'
group by Activity.machine_id;