# Write your MySQL query statement below
select distinct l.num as ConsecutiveNums
 from logs l join logs l2 
 on l.id=l2.id+1 and l.num=l2.num 
 join logs l3
  on l3.id+1=l2.id and l3.num=l2.num
