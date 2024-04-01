# Write your MySQL query statement below
# Write your MySQL query statement below

select round(
    sum(
        case
            when date_add(t.fed, interval 1 day) = a.event_date then 1
            else 0
        end
    ) / sum(
        case
            when a.event_date = t.fed then 1
            else 0
        end
    )
, 2) as fraction
from Activity a left join (
    select player_id, min(event_date) as fed
    from Activity
    group by player_id
) as t on a.player_id = t.player_id;