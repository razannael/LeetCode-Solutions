# Write your MySQL query statement below
SELECT
 e.employee_id,
 e.name,
 COUNT(t.reports_to) AS reports_count,
 ROUND(AVG(t.age)) AS average_age
 FROM employees e 
 LEFT JOIN 
 employees t
 ON e.employee_id = t.reports_to
 GROUP BY e.employee_id, name
 HAVING reports_count > 0
 ORDER BY e.employee_id;