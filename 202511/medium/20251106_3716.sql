-- https://leetcode.com/problems/find-churn-risk-customers/

-- # Write your MySQL query statement below

select distinct subscription_events.user_id
    , t1.current_plan
    , t1.current_monthly_amount
    , t2.max_historical_amount
    , t2.days_as_subscriber
from subscription_events
join (
    select distinct user_id
        , plan_name as current_plan
        , monthly_amount as current_monthly_amount
    from subscription_events
    where (user_id, event_date) in (select user_id, max(event_date) as max_event_date from subscription_events group by user_id)
        and plan_name = 'basic'
    ) as t1 on subscription_events.user_id = t1.user_id
join (
    select user_id
        , max(monthly_amount) as max_historical_amount
        , datediff(max(event_date), min(event_date)) as days_as_subscriber
    from subscription_events
    group by user_id
    ) as t2 on subscription_events.user_id = t2.user_id
where subscription_events.event_type = 'downgrade' and t2.days_as_subscriber >= 60
group by subscription_events.user_id
order by t2.days_as_subscriber desc, subscription_events.user_id;