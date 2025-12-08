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
--     )
-- select * from t1;

    t2 as (
        select t1.employee_id, t1.employee_id as tmp_id, t1.employee_name, t1.level, t1.salary, t1.manager_id
        from t1
        left join t1 as t3 on t3.manager_id = t1.employee_id
        where t3.manager_id is null
        
        union all

        select t1.employee_id
            , t2.manager_id as tmp_id
            , t1.employee_name
            , t1.level
            , t1.salary
            , t1.manager_id
        from t1
        join t2 on t2.manager_id = t1.employee_id
        where t2.manager_id = t1.employee_id

        union all

        select t1.employee_id
            , t2.manager_id as tmp_id
            , t1.employee_name
            , t1.level
            , t1.salary
            , t1.manager_id
        from t1
        join t2 on t2.manager_id = t1.employee_id
        where t2.manager_id = t1.employee_id
--     t3 as (
--         select t2.employee_id
--             , t2.employee_name
--             , t2.level
--             , t2.team_size
--             , t2.salary
--             , t4.budget
--         from t2
--         left join
--     )
    )

select * from t2
-- where employee_id = null or employee_id = 2 or employee_id = 3 or employee_id = 4 or employee_id = 6;


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