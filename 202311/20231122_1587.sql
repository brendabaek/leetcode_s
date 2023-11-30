-- https://leetcode.com/problems/bank-account-summary-ii/

-- # Write your MySQL query statement below

select name, sum(Transactions.amount) as balance
from Users
left join Transactions on Users.account = Transactions.account
group by Users.account
having sum(Transactions.amount) > 10000;