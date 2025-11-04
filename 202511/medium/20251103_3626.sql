-- https://leetcode.com/problems/find-stores-with-inventory-imbalance/

-- # Write your MySQL query statement below

select i1.store_id, store_name, location,
    i2.product_name as most_exp_product, i3.product_name as cheapest_product, round(i3.quantity / i2.quantity, 2) as imbalance_ratio
from (
    select store_id, max(price) as most_exp_price, min(price) as cheapest_price
    from inventory
    group by store_id
    having count(store_id) >= 3
    ) as i1
join inventory as i2 on i1.store_id = i2.store_id and i1.most_exp_price = i2.price
join inventory as i3 on i1.store_id = i3.store_id and i1.cheapest_price = i3.price
join stores on i1.store_id = stores.store_id
where i3.quantity / i2.quantity > 1
order by imbalance_ratio desc, store_name