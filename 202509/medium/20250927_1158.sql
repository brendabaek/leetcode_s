-- https://leetcode.com/problems/market-analysis-i/

-- # Write your MySQL query statement below

select user_id as buyer_id , join_date, count(order_date) as orders_in_2019
from Users
left join (
    select buyer_id, order_date
    from Orders
    where '20190101' <= order_date and order_date <= '20191231'
    ) as o on Users.user_id = o.buyer_id
group by user_id, join_date;