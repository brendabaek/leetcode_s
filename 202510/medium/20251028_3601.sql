-- https://leetcode.com/problems/find-drivers-with-improved-fuel-efficiency/

-- # Write your MySQL query statement below

select t1.driver_id,
    driver_name,
    round(first_half_avg, 2) as first_half_avg,
    round(second_half_avg, 2) as second_half_avg,
    round(second_half_avg - first_half_avg, 2) as efficiency_improvement
from (
    select driver_id, sum(distance_km/fuel_consumed)/count(*) as first_half_avg
    from trips
    where month(trip_date) <= 6
    group by driver_id
    ) as t1
join (
    select driver_id, sum(distance_km/fuel_consumed) / count(*) as second_half_avg
    from trips
    where month(trip_date) > 6
    group by driver_id
    ) as t2 on t1.driver_id = t2.driver_id
join drivers on t1.driver_id = drivers.driver_id
where second_half_avg - first_half_avg > 0
order by efficiency_improvement desc, driver_name;