-- https://leetcode.com/problems/sales-person/

-- # Write your MySQL query statement below

select SalesPerson.name
from SalesPerson
left join Orders on SalesPerson.sales_id = Orders.sales_id
left join Company on Orders.com_id = Company.com_id
group by SalesPerson.name
having sum(if(Company.name = "RED", 1, 0)) = 0;