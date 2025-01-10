-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/

-- # Write your MySQL query statement below

select Employees.employee_id, Employees.name, count(distinct e.employee_id) as reports_count, round(avg(e.age)) as average_age
from Employees
join Employees as e on Employees.employee_id = e.reports_to
group by Employees.employee_id, Employees.name;