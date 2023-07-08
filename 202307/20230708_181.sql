-- ## https://leetcode.com/problems/employees-earning-more-than-their-managers/

-- # Write your MySQL query statement below

select o.name as Employee
from Employee as o
join Employee as t on o.managerId = t.id
where o.salary > t.salary;