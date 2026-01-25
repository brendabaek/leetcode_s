-- https://leetcode.com/problems/find-emotionally-consistent-users/

-- # Write your MySQL query statement below

select t1.user_id, reaction as dominant_reaction, round(count(reaction) / t1.total, 2) as reaction_ratio
from reactions
join(
    select user_id, count(content_id) as total
    from reactions
    group by user_id
    having total >= 5
    ) as t1 on reactions.user_id = t1.user_id
group by user_id, reaction
having reaction_ratio >= 0.6
order by reaction_ratio desc, user_id;