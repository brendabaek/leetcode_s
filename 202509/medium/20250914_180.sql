-- https://leetcode.com/problems/consecutive-numbers/

-- # Write your MySQL query statement below

select distinct num as ConsecutiveNums
from (select *,
            -- lag(num, 1) over(order by id) as num0,
            lead(num, 1) over(order by id) as num1,
            lead(num, 2) over(order by id) as num2
        from Logs) as l
where num = num1 and num = num2;
-- where (num != num0 or num0 is null) and num = num1 and num = num2;