# Write your MySQL query statement below
SELECT name AS Employee from Employee e WHERE e.salary > (select salary from Employee WHERE id = e.managerId) 