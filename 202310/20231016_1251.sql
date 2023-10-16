-- https://leetcode.com/problems/average-selling-price/

-- # Write your MySQL query statement below

select Prices.product_id,
        case when sum(units) = 0 or sum(units) is null then 0 else
        round(sum(case when start_date <= purchase_date and purchase_date <= end_date then price * units else 0 end)
        / sum(case when start_date <= purchase_date and purchase_date <= end_date then units end), 2) end as average_price
from Prices
left outer join UnitsSold on UnitsSold.product_id = Prices.product_id
group by Prices.product_id;