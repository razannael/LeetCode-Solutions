# Write your MySQL query statement below
WITH join1 AS (
	SELECT CASE 
			WHEN MONTH(s.sale_date) IN (12,01,02) THEN 'Winter'
			WHEN MONTH(s.sale_date) IN (03,04,05) THEN 'Spring'
			WHEN MONTH(s.sale_date) IN (6,7,8) THEN 'Summer'
			WHEN MONTH(s.sale_date) IN (9,10,11) THEN 'Fall'
       END AS Season,
       p.category,
       s.quantity, 
       s.price
       FROM Sales AS s JOIN Products AS p
       ON s.product_id = p.product_id
), aggregate2 AS(
	SELECT Season, category, 
    SUM(quantity) AS total_quantity,
    SUM(price*quantity) AS total_revenue
    FROM join1
    GROUP BY Season, category
), filter3 AS(
	SELECT *,
    RANK() OVER(PARTITION BY season ORDER BY total_quantity desc, total_revenue desc) AS ranking
    FROM aggregate2
)
SELECT season, category, total_quantity, total_revenue FROM filter3
WHERE ranking=1;