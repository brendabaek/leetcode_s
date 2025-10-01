-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/

-- # Write your MySQL query statement below

with recursive w_sum as (
    select turn, person_name, weight as s
    from Queue
    where turn = 1

    union all

    select Queue.turn, Queue.person_name, w_sum.s + Queue.weight as s
    from w_sum
    join Queue on Queue.turn = w_sum.turn + 1
    where s < 1000
)
select person_name from w_sum where s <= 1000 order by s desc limit 1;