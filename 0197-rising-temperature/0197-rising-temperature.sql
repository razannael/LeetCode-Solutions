# Write your MySQL query statement below
select w1.id 
from Weather w1 inner join Weather w2 
on to_days(w1.recordDate)-1 = to_days(w2.recordDate )
and w1.temperature > w2.temperature;