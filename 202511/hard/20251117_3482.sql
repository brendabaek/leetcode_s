-- https://leetcode.com/problems/analyze-organization-hierarchy/

-- ing
-- # Write your MySQL query statement below

with recursive
    t1 as (
        select employee_id, employee_name, 1 as level, manager_id, salary
        from Employees
        where manager_id is null

        union all

        select Employees.employee_id, Employees.employee_name, t1.level + 1 as level, Employees.manager_id, Employees.salary
        from Employees
        join t1 on t1.employee_id = Employees.manager_id
    ),

    t2 as (
        select t1.employee_id, t1.employee_name, t1.level, 0 as team_size, t1.salary, t1.salary as budget, t1.manager_id
        from t1
        left join t1 as t3 on t3.manager_id = t1.employee_id
        where t3.manager_id is null
        
        union all

        select t1.employee_id
            , t1.employee_name
            , t1.level
            , t2.team_size + 1 as team_size
            , t1.salary
            , t2.budget + t1.salary as budget
            , t1.manager_id
        from t1
        join t2 on t2.manager_id = t1.employee_id
        where t2.manager_id = t1.employee_id
    )

select * from t2 limit 30;


-- select t2.employee_id
--     , t2.employee_name
--     , t2.level
--     , sum(t2.team_size) as team_size
--     , if(sum(t2.team_size) > 1, sum(t2.budget) - (t2.salary * (cnt - 1)), sum(t2.budget)) as budget
--     , t2.salary
--     , t4.cnt
-- from t2
-- left join (select manager_id, count(manager_id) as cnt from t2 group by manager_id) as t4 on t2.employee_id = t4.manager_id
-- group by employee_id, employee_name, level
-- order by level, budget desc, employee_name;