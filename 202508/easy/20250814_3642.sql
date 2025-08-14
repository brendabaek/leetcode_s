-- https://leetcode.com/problems/find-books-with-polarized-opinions/

--# Write your MySQL query statement below

select books.*, rating_spread, polarization_score
from books
inner join
        (
        select book_id,
            max(session_rating) - min(session_rating) as rating_spread,
            round(sum(if(session_rating = 3, 0, 1))/count(session_id), 2) as polarization_score
        from reading_sessions
        group by book_id
        having count(distinct session_id) >= 5 and max(session_rating) >= 4 and min(session_rating) <= 2 
        ) as s on books.book_id = s.book_id
where polarization_score >= 0.6
order by polarization_score desc, title desc;