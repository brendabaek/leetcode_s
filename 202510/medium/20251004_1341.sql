-- https://leetcode.com/problems/movie-rating/

-- # Write your MySQL query statement below

(
select title as results
from MovieRating
left join Movies on MovieRating.movie_id = Movies.movie_id
where left(created_at, 7) = "2020-02"
group by MovieRating.movie_id
order by avg(rating) desc, title
limit 1
)
union all

(
select Users.name as results
from MovieRating
left join Users on MovieRating.user_id = Users.user_id
group by MovieRating.user_id
order by count(movie_id) desc, Users.name
limit 1
);