WITH
max_prices AS(
    SELECT 
        store_id
        ,MAX(price) AS max_price
        ,MIN(price) AS min_price
    FROM inventory
    GROUP BY store_id
    HAVING COUNT(DISTINCT product_name) >=3
)
,max_min_prod AS(
    SELECT 
        i.store_id
        ,i.product_name
        ,i.quantity
        ,i.price
    FROM inventory i
    JOIN max_prices mp
        ON i.store_id=mp.store_id
        AND (i.price=mp.max_price OR i.price=mp.min_price)
)
SELECT 
    s.store_id
    ,s.store_name
    ,s.location
    ,me.product_name AS most_exp_product
    ,ch.product_name AS cheapest_product
    ,ROUND(ch.quantity / me.quantity, 2) AS imbalance_ratio
FROM max_min_prod me
JOIN max_min_prod ch
    ON me.store_id=ch.store_id
    AND me.price>ch.price
    AND me.quantity<ch.quantity
JOIN stores s 
    ON s.store_id=me.store_id
ORDER BY imbalance_ratio DESC, s.store_name ASC