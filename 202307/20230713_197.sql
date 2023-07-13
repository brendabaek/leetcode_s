-- ## https://leetcode.com/problems/rising-temperature/

-- # Write your MySQL query statement below

select w.id
from Weather as w
left join Weather as a on w.recordDate = date_add(a.recordDate, interval 1 day)
where w.temperature > a.temperature;