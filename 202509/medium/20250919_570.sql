-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

-- # Write your MySQL query statement below

select name
from Employee
inner join (select managerId as Id from Employee where managerId is not null
    group by managerId having count(id) >= 5) as e on Employee.id = e.id;