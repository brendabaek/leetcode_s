-- https://leetcode.com/problems/restaurant-growth/

-- # Write your MySQL query statement below

select *
from (select visited_on,
        sum(sum(amount)) over (order by visited_on rows between 6 preceding and current row) as amount,
        round(sum(sum(amount)) over (order by visited_on rows between 6 preceding and current row) / 7, 2) as average_amount
    from Customer
    group by visited_on) as c
where visited_on >= (select min(visited_on) from Customer) + interval 6 day;