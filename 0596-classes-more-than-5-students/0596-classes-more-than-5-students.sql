# Write your MySQL query statement below
SELECT class from Courses 
Group by class
Having Count(student) >= 5