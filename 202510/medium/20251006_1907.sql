-- https://leetcode.com/problems/count-salary-categories/

-- # Write your MySQL query statement below

select R.category, if(t.cnt is null, 0, t.cnt) as accounts_count
from (
    select if(income < 20000, 'Low Salary', if(income > 50000, 'High Salary', 'Average Salary')) as category,
        count(account_id) as cnt
    from Accounts
    group by category
    ) as t
right join (
    select *
    from (
        select 'Low Salary' as category
        union all
        select 'Average Salary'
        union all
        select 'High Salary'
        ) as r
    ) as R on t.category = R.category;