# Write your MySQL query statement below
SELECT name FROM employee WHERE id IN 
(SELECT managerId from employee group by managerId having count(*) >=5 );