-- ## https://leetcode.com/problems/delete-duplicate-emails/

-- # Write your MySQL query statement below

delete
  from Person
  where id not in
    ( select min_id
      from
      ( select min(c.id) as min_id
        from Person as c
        group by c.email) tmp) ;