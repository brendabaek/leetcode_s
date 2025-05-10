-- https://leetcode.com/problems/find-valid-emails/

-- # Write your MySQL query statement below

select user_id, email
from Users
where email like '%.com' and
    substring_index(email, '@', 1) regexp'^[a-z0-9_]+$' and
    substring_index(substring_index(email, '.com', 1), '@', -1) regexp '^[a-z]+$';