-- https://leetcode.com/problems/find-overbooked-employees/

-- # Write your MySQL query statement below

select m1.employee_id, employee_name, department, count(year_week) as meeting_heavy_weeks
from (
    select employee_id, concat(year(meeting_date), '-', week(meeting_date, 1)) as year_week, sum(duration_hours) as meeting_hours
    from meetings
    group by employee_id, year_week
    having meeting_hours > 20
    ) as m1
join employees on m1.employee_id = employees.employee_id
group by m1.employee_id, employee_name, department
having meeting_heavy_weeks > 1
order by meeting_heavy_weeks desc, employee_name;