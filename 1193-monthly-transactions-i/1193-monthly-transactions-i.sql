SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month
    ,country
    ,COUNT(id) AS trans_count
    ,SUM(CASE WHEN state='approved' THEN 1 ELSE 0 END) AS approved_count
    ,SUM(amount) AS trans_total_amount
    ,SUM(CASE WHEN state='approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM transactions
GROUP BY month, country

/*group by month and country is very imp
We create groups:
2018-12, US → rows with id 121 & 122
2019-01, US → row with id 123
2019-01, DE → row with id 124

%Y → 2025
%y → 25
%M → September
%m → 09
%d → 12

Capital = full form (%Y = 2025, %M = September).
Small = short form (%y = 25, %b = Sep).
*/