WITH 
filter AS(
    SELECT 
        user_id
        ,category
    FROM productpurchases p1
    INNER JOIN productinfo p2
        ON p1.product_id=p2.product_id
)
SELECT 
    f1.category AS category1
    ,f2.category AS category2
    ,COUNT(DISTINCT f1.user_id) AS customer_count
FROM filter f1
INNER JOIN filter f2
    ON f1.user_id=f2.user_id 
    AND f1.category<f2.category
GROUP BY f1.category, f2.category
HAVING COUNT(DISTINCT f1.user_id)>=3
ORDER BY customer_count DESC, f1.category, f2.category  
