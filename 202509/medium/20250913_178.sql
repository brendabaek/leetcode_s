-- https://leetcode.com/problems/rank-scores/

-- # Write your MySQL query statement below

select score, dense_rank() over (order by score desc) as 'rank' from Scores;