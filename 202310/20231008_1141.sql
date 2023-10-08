-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

-- # Write your MySQL query statement below

select activity_date as day, count(distinct user_id) as active_users
from Activity
where date_sub('2019-07-27', interval 30 day) < activity_date and activity_date <= date('2019-07-27')
group by activity_date;