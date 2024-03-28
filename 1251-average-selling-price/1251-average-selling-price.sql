# Write your MySQL query statement below
SELECT prices.product_id , COALESCE(Round(SUM( Price * Units ) / SUM( Units ),2) ,0)
as average_price
from prices left join UnitsSold 
on prices.product_id = UnitsSold.product_id
AND UnitsSold.purchase_date BETWEEN prices.start_date AND prices.end_date
 Group By product_id;