-- https://leetcode.com/problems/customers-who-bought-all-products/

-- # Write your MySQL query statement below

select distinct customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(distinct product_key) from Product);