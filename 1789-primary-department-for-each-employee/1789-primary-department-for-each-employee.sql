# Write your MySQL query statement below
select employee_id , department_id  
from Employee  
where primary_flag = 'Y'

UNION

select employee_id , department_id 
from employee 
group by employee_id
having count(*) = 1 
and max(primary_flag) = 'N'