# Write your MySQL query statement below

with filtered_data as(
    select id,visit_date,people
    from Stadium
    where people >= 100
),
group_key as (
    select id,visit_date,people,
    (id-row_number() over(order by id)) as grp_key
    from filtered_data
),
count_grouped as (
    select id,visit_date,people,
    count(id) over(partition by grp_key) as cnt
    from group_key
)
select id,visit_date,people
from count_grouped where cnt>=3 order by id 