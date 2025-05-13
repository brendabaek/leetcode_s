-- https://leetcode.com/problems/find-products-with-valid-serial-numbers/

-- # Write your MySQL query statement below

select *
from products
where description regexp '(^|\\s)SN[0-9]{4}-[0-9]{4}(\\s|$)';