-- https://leetcode.com/problems/find-books-with-no-available-copies/description/

-- # Write your MySQL query statement below

select library_books.book_id, title, author, genre, publication_year, total_copies as current_borrowers
from library_books
join borrowing_records on library_books.book_id = borrowing_records.book_id
where return_date is null
group by library_books.book_id, title, author, genre, publication_year, total_copies
having total_copies = count(return_date is null)
order by total_copies desc, title;