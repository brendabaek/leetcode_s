-- https://leetcode.com/problems/department-highest-salary/

-- # Write your MySQL query statement below

select Department.name as Department, Employee, Salary
from Department
join(select M.departmentID, Employee.name as Employee, Employee.salary as Salary
    from (
        select departmentID, max(salary) as msalary
        from Employee
        group by departmentID) as M
        join Employee on M.departmentID = Employee.departmentID and M.msalary = Employee.salary) as E
    on Department.id = E.departmentID;