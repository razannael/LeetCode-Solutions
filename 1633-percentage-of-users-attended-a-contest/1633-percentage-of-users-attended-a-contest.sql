# Write your MySQL query statement below
with total_user as (
    select 
        count(*) as cnt
    from
        Users 
)
select
    contest_id, round((count(user_id)*100/t.cnt),2) as percentage
from 
    Register r, total_user t
group by  contest_id
order by percentage desc, contest_id