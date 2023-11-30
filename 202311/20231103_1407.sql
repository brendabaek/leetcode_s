-- https://leetcode.com/problems/top-travellers/

-- # Write your MySQL query statement below
    select Users.name, ifnull(sum(Rides.distance), 0) as travelled_distance
    from Users
    left join rides on Users.id = Rides.user_id
    group by Users.id, Users.name
    order by 2 desc, 1;