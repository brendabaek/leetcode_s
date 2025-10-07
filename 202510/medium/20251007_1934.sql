-- https://leetcode.com/problems/confirmation-rate/

-- # Write your MySQL query statement below

select Signups.user_id, if(confirmation_rate is null, 0, confirmation_rate) as confirmation_rate
from Signups
left join (
    select user_id, round(sum(if(action = 'confirmed', 1, 0)) / count(time_stamp), 2) as confirmation_rate
    from Confirmations
    group by user_id
) as t
on Signups.user_id = t.user_id