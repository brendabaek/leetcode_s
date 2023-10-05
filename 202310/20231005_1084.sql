-- https://leetcode.com/problems/sales-analysis-iii/

-- # Write your MySQL query statement below

select Sales.product_id, Product.product_name
from Sales
left join Product on Product.product_id = Sales.product_id
group by Sales.product_id
having '2019-01-01' <= min(sale_date) and max(sale_date) <= '2019-03-31';