# Write your MySQL query statement below
SELECT  Employee.name , Bonus.bonus FROM employee LEFT JOIN bonus
 on employee.empId = bonus.empId WHERE IFNULL(Bonus.bonus, 0) < 1000;