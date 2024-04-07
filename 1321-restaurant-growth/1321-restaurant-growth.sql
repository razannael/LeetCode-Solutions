# Write your MySQL query statement below
WITH C1 AS (SELECT DISTINCT visited_on FROM Customer)
SELECT C1.visited_on, SUM(C2.amount) AS amount, ROUND((SUM(C2.amount))/7, 2) AS average_amount FROM C1, Customer C2 WHERE DATEDIFF(C1.visited_on, C2.visited_on) BETWEEN 0 AND 6
AND DATEDIFF(C1.visited_on, (SELECT MIN(visited_on) FROM C1)) >= 6
GROUP BY 1
ORDER BY 1