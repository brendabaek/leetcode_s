-- https://leetcode.com/problems/find-students-who-improved/

-- # Write your MySQL query statement below

select s1.student_id, s1.subject, s1.score as first_score, s2.score as latest_score
from (select student_id, subject, min(exam_date) as min_date, max(exam_date) as max_date
    from Scores
    group by student_id, subject
    having min_date < max_date
    ) as t
join Scores as s1 on (s1.student_id, s1.subject, s1.exam_date) = (t.student_id, t.subject, t.min_date)
join Scores as s2 on (s2.student_id, s2.subject, s2.exam_date) = (t.student_id, t.subject, t.max_date)
where s1.score < s2.score
order by student_id, subject;