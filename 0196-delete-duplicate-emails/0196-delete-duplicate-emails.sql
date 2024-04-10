# Write your MySQL query statement below
DELETE FROM person
WHERE id IN 
(
    SELECT id
    FROM (
        SELECT
            id,
            email,
            ROW_NUMBER() OVER(PARTITION BY email ORDER BY id ASC) AS rn
        FROM person
    ) AS t
    WHERE rn >= 2
);