-- https://leetcode.com/problems/find-users-with-high-token-usage/

-- # Write your MySQL query statement below

select user_id, count(prompt) as prompt_count, round(sum(tokens)/count(tokens), 2) as avg_tokens
from prompts
group by user_id
having count(prompt) >= 3 and count(distinct tokens) > 1
order by avg_tokens desc, user_id;