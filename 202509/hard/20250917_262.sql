-- https://leetcode.com/problems/trips-and-users/

-- # Write your MySQL query statement below

select request_at as 'Day', round(sum(if(status = 'completed', 0, 1)) / count(status), 2) as 'Cancellation Rate'
from (
    select request_at, status
    from Trips
    join Users as u1 on u1.users_id = Trips.client_id
    join Users as u2 on u2.users_id = Trips.driver_id
    where u1.banned = 'No' and u2.banned = 'No' and '2013-10-01' <= Trips.request_at and Trips.request_at <= '2013-10-03'
    ) as new_table
group by request_at;