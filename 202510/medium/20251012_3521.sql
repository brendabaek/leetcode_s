-- https://leetcode.com/problems/find-product-recommendation-pairs/

-- # Write your MySQL query statement below

select product1_id, product2_id, p4.category as product1_category, p5.category as product2_category, customer_count
from (
    select p1.product_id as product1_id, p2.product_id as product2_id, count(distinct p1.user_id) as customer_count
    from ProductPurchases as p1
    join ProductPurchases as p2 on P1.user_id = P2.user_id
    where p1.product_id < p2.product_id
    group by p1.product_id, p2.product_id
    having count(distinct p1.user_id) > 2
    order by p1.user_id, p1.product_id
    ) as p3
join ProductInfo as p4 on p3.product1_id = p4.product_id
join ProductInfo as p5 on p3.product2_id = p5.product_id
order by customer_count desc, product1_id, product2_id;