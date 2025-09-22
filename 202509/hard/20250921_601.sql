-- https://leetcode.com/problems/human-traffic-of-stadium/

-- # Write your MySQL query statement below

select id, visit_date, people
from(
    select *,
        if(lead(id, 2) over(order by id) is not null, lead(id, 2) over(order by id),
            if(lead(id, 1) over(order by id) - id = 1 and id - lag(id, 1) over(order by id) = 1, id + 2,
                if(id - lag(id, 2) over(order by id) = 2, id + 2, null))) as lead_id,
        if(lag(id, 2) over(order by id) is not null, lag(id, 2) over(order by id),
            if(id - lag(id, 1) over(order by id) = 1 and lead(id, 1) over(order by id) - id = 1, id - 2,
                if(lead(id, 2) over(order by id) - id = 2, id - 2, null))) as lag_id 
    from Stadium
    where people >= 100
    ) as s
where lead_id -  id = 2 or id - lag_id = 2;