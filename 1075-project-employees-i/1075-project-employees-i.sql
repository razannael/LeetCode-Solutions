# Write your MySQL query statement below
SELECT project.project_id, ROUND(AVG(employee.experience_years), 2) as average_years
FROM project join employee
on project.employee_id = employee.employee_id
GROUP BY project_id;