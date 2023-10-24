-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/

-- # Write your MySQL query statement below

select Products.product_name, sum(Orders.unit) as unit
from Products
left join Orders on Products.product_id = Orders.product_id
where date('2020-02-01') <= Orders.order_date and Orders.order_date < date('2020-03-01')
group by Products.product_name
having sum(Orders.unit) >= 100;