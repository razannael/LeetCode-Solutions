# Write your MySQL query statement below
# Write your MySQL query statement below
select round(
    sum(
        case
            when d.customer_pref_delivery_date = t.fod then 1
            else 0
        end
) / sum(
    case
        when d.order_date = t.fod then 1
        else 0
    end
) * 100, 2) as immediate_percentage
from Delivery d inner join (
    select customer_id, min(order_date) as fod
    from Delivery
    group by customer_id
) as t on d.customer_id = t.customer_id