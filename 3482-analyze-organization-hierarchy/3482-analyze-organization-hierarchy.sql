# Write your MySQL query statement below
with recursive Hierarchy as (
    select employee_id,employee_name,manager_id,salary,1 as level 
    from employees where manager_id is null
    union all
    select e.employee_id,e.employee_name,e.manager_id,e.salary,h.level+1
    from employees e join Hierarchy h on e.manager_id = h.employee_id
),
Subordinates as (
    select manager_id,employee_id as subordinate_id from employees 
    where manager_id is not null
    union all 
    select s.manager_id,e.employee_id from subordinates s
    join employees e on e.manager_id = s.subordinate_id
),
ManagerStats as (
    select s.manager_id,COUNT(*) as team_size, SUM(e.salary) as team_salary
    from subordinates s join employees e on s.subordinate_id = e.employee_id
    group by s.manager_id
),
FinalResult as (
    select h.employee_id,h.employee_name,h.level,COALESCE(ms.team_size,0)as team_size,
    h.salary + COALESCE(ms.team_salary,0) as budget from Hierarchy h left join
    ManagerStats ms on h.employee_id = ms.manager_id
)
select * from finalResult order by level ASC,budget desc,employee_name ASC;