# Write your MySQL query statement below
select
    customer_id, count(order_id) as total_orders,
    round(sum(
            if(
                (hour(order_timestamp) between 11 and 13) or 
                (hour(order_timestamp) between 18 and 20),
                1, 0
            )
        )/count(order_id)
    ,2)*100 as peak_hour_percentage,
    round(avg(order_rating),2) as average_rating
from restaurant_orders
group by customer_id
    having
        total_orders >= 3 and
        peak_hour_percentage >= 60 and
        average_rating >= 4 and
        sum(if(order_rating is not null, 1, 0))/count(order_id) > 0.5
order by
    average_rating desc, customer_id desc