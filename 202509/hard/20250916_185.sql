-- https://leetcode.com/problems/department-top-three-salaries/

-- # Write your MySQL query statement below

select Department.name as Department, e.name as Employee, e.salary as Salary
from Department
join (select *,
    dense_rank() over(partition by departmentId order by salary desc) as rk
    from Employee) as e on Department.id = E.departmentId
where e.rk <= 3;