# Write your MySQL query statement below
select lb.book_id, title, author, genre, publication_year, borrowed_copies as current_borrowers 
from library_books lb INNER JOIN
(select book_id, count(*) as borrowed_copies from borrowing_records 
where return_date is null 
group by book_id) br
ON lb.book_id = br.book_id and lb.total_copies = br.borrowed_copies
order by current_borrowers desc, title;