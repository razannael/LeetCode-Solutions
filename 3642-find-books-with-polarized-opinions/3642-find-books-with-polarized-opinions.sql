# Write your MySQL query statement below
select * from books JOIN (
    select book_id, 
    max(session_rating) - min(session_rating) as rating_spread, 
    ROUND(sum(session_rating != 3)/count(*), 2) as polarization_score
    from reading_sessions group by book_id 
    having count(*) >= 5 and max(session_rating) >= 4 and min(session_rating) <= 2
)T
using(book_id) where polarization_score >= 0.6
order by polarization_score desc, title desc;