-- https://leetcode.com/problems/employees-whose-manager-left-the-company/

-- # Write your MySQL query statement below

select Employees.employee_id
from Employees
left join Employees as e on Employees.manager_id = e.employee_id
where Employees.salary < 30000 and Employees.manager_id is not null and e.employee_id is null
order by 1;