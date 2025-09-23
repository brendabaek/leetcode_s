-- https://leetcode.com/problems/tree-node/

-- # Write your MySQL query statement below

select distinct id, if(p_id is null, 'Root', if(c_id is null, 'Leaf', 'Inner')) as type
from(select Tree.id, Tree.p_id, t1.id as c_id
    from Tree
    left join Tree as t1 on Tree.id = t1.p_id) as t2;