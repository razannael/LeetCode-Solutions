# Write your MySQL query statement below
with usermaxdate as (
    select user_id, max(event_date) as latest_date from subscription_events group by user_id
), 
activesubs as (
    select
        s.user_id,
        s.plan_name as current_plan,
        s.monthly_amount as current_monthly_amount
    from 
        subscription_events s join usermaxdate u 
            on 
                s.user_id = u.user_id and 
                s.event_date = u.latest_date
    where s.event_type <> 'cancel'
),
onedowngrade_60 as (
    select 
        s.user_id,
        a.current_plan,
        a.current_monthly_amount,
        min(s.event_date) as mindate,
        max(s.event_date) as maxdate
    from 
        activesubs a join subscription_events s 
        on 
            a.user_id = s.user_id 
    group by s.user_id 
        having 
            sum(s.event_type='downgrade') >= 1 
            and
            datediff(max(event_date), min(event_date)) >= 60
),
maxhistoricalamt as (
    select o.*, max(monthly_amount) as max_historical_amount
    from
        onedowngrade_60 o join subscription_events s
        on
            o.user_id = s.user_id
    where s.event_date <> o.maxdate
    group by s.user_id
)
select 
    user_id, current_plan, current_monthly_amount, max_historical_amount, 
    datediff(maxdate,mindate) as days_as_subscriber 
from 
    maxhistoricalamt 
where 
    current_monthly_amount < max_historical_amount/2 
order by 
    days_as_subscriber desc, user_id asc