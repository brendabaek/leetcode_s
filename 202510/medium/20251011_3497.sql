-- https://leetcode.com/problems/analyze-subscription-conversion/

-- # Write your MySQL query statement below

select u1.User_id, trial_avg_duration, paid_avg_duration
from (
    select user_id, max(activity_date) as t_date, round(avg(activity_duration), 2) as trial_avg_duration
    from UserActivity
    where activity_type = 'free_trial'
    group by user_id
) as u1
join (
    select user_id, min(activity_date) as p_date, round(avg(activity_duration), 2) as paid_avg_duration
    from UserActivity
    where activity_type = 'paid'
    group by user_id
) as u2 on u1.user_id = u2.user_id
where t_date < p_date