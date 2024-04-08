# Write your MySQL query statement below
select id, sum(num) as num
from
    (select requester_id as id, count(requester_id) num
    from requestaccepted
    group by 1
    union all
    select accepter_id as id, count(accepter_id) num
    from requestaccepted
    group by 1) t
group by 1
order by 2 desc
limit 1