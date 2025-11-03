select session_id ,user_id ,
round(timestampdiff(minute,min(event_timestamp),max(event_timestamp))) session_duration_minutes ,
sum(event_type='scroll') scroll_count 
from app_events 
group by 1,2
having session_duration_minutes>30
and
scroll_count>4
and
sum(event_type='click')/scroll_count *1.0 <0.2
and 
sum(event_type ='purchase')=0
order by 4 desc,1