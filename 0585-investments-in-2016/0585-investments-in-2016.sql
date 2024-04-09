# Write your MySQL query statement below
select round(sum(src.tiv_2016),2) as tiv_2016
      from Insurance src 
     where 1 < (select count(pid) from Insurance i where i.tiv_2015 = src.tiv_2015)
       and 0 = (select count(pid) from Insurance i where i.pid <> src.pid and i.lat = src.lat and i.lon = src.lon);