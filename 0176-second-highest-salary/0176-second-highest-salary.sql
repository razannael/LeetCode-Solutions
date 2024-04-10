# Write your MySQL query statement below
WITH OrderedSalaries AS (
  SELECT distinct(salary)
  FROM Employee
  ORDER BY salary DESC
  LIMIT 2
)
SELECT MIN(salary) AS SecondHighestSalary
FROM OrderedSalaries
WHERE (SELECT COUNT(DISTINCT salary) FROM OrderedSalaries) > 1;