-- https://leetcode.com/problems/triangle-judgement/

-- # Write your MySQL query statement below

select *, if( (x >= y+z) or (y >= x+z) or (z >= x+y), "No", "Yes") as triangle
from Triangle