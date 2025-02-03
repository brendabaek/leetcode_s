-- https://leetcode.com/problems/employees-with-missing-information/

-- # Write your MySQL query statement below

select employee_id
from
    (select employee_id
    from Employees
    union all
    select employee_id
    from Salaries) as a
group by employee_id
having count(employee_id) = 1
order by employee_id;