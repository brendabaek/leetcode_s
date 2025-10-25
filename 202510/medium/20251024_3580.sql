-- https://leetcode.com/problems/find-consistently-improving-employees/

-- # Write your MySQL query statement below

select p5.employee_id, name, sum(imp) as improvement_score
from (
    select p2.employee_id, rating - lead(rating) over (partition by p2.employee_id order by rn) as imp
    from (
        select *
        from (
            select *, row_number() over (partition by employee_id order by review_date desc) as rn
            from performance_reviews
            ) as p1
        where rn <= 3
        ) as p2
    right join (
        select employee_id 
        from (
            select *, row_number() over (partition by employee_id order by review_date desc) as rn
            from performance_reviews
            ) as p3
        where rn = 3
        ) as p4 on p2.employee_id = p4.employee_id
    ) as p5
left join employees on p5.employee_id = employees.employee_id
where imp > 0 or imp is null
group by p5.employee_id
having count(p5.employee_id) = 3
order by improvement_score desc, name;