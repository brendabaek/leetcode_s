-- https://leetcode.com/problems/product-price-at-a-given-date/

-- # Write your MySQL query statement below

select m.product_id, if(Products.new_price is null, 10, Products.new_price) as price
from Products
right join (
    select distinct Products.product_id, n.change_date
    from Products
    left join (
        select product_id, max(change_date) as change_date
        from Products
        where change_date <= '20190816'
        group by product_id) as n on Products.product_id = n.product_id
    ) as m on Products.product_id = m.product_id and Products.change_date = m.change_date;