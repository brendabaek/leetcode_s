-- https://leetcode.com/problems/seasonal-sales-analysis/

-- # Write your MySQL query statement below

select season, category, total_quantity, total_revenue
from (
    select *, rank() over (partition by season order by total_quantity desc, total_revenue desc) as rnk
    from (
        select if(month(sale_date) in (12, 01, 02), 'Winter',
                if(month(sale_date) in (03, 04, 05), 'Spring',
                    if(month(sale_date) in (06, 07, 08), 'Summer', 'Fall'))) as season,
            category,
            sum(quantity) as total_quantity,
            sum(quantity * price) as total_revenue
        from sales
        join products on sales.product_id = products.product_id
        group by category, season
    ) as t1
) as t2
where rnk = 1
order by season;