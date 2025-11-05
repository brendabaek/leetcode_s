-- https://leetcode.com/problems/find-loyal-customers/

-- # Write your MySQL query statement below

select t1.customer_id
from (
    select customer_id, sum(if(transaction_type = 'refund', 1, 0)) / count(transaction_type) as rate
    from customer_transactions
    group by customer_id
    having rate < 0.2 and count(transaction_type) >= 3
    ) as t1
join (
    select customer_id, if(datediff(max(transaction_date), min(transaction_date)) >= 30, customer_id, 0) as c_id
    from customer_transactions
    group by customer_id
    having c_id != 0
    ) as t2 on t1.customer_id = t2.c_id
order by customer_id;