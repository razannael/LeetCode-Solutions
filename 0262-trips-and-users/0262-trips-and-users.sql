-- Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03" with at least one trip. Round Cancellation Rate to two decimal points.

SELECT T.request_at AS Day ,  
ROUND(SUM(CASE WHEN T.status = 'cancelled_by_driver' OR T.status = 'cancelled_by_client' THEN 1 ELSE 0 END) / COUNT(T.status),2)  AS `Cancellation Rate`
FROM Trips T JOIN Users C
ON T.client_id = C.users_id
JOIN Users D
ON T.driver_id = D.users_id
WHERE C.banned = 'No' AND D.banned ='No' AND T.request_at >= '2013-10-01' AND T.request_at <= '2013-10-03'
GROUP BY T.request_at



-- SELECT SUM(CASE WHEN YEAR(ord_date) = 1993 THEN qty ELSE 0 END) AS total_sales