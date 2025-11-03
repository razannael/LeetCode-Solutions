WITH Reviews AS (
    SELECT employee_id, review_date, rating,
    LAG(rating) OVER( PARTITION BY employee_id ORDER BY review_date DESC ) AS next_rating,
    LAG(rating, 2) OVER( PARTITION BY employee_id ORDER BY review_date DESC ) AS next_next_rating,
    ROW_NUMBER() OVER( PARTITION BY employee_id ORDER BY review_date DESC ) AS rnks
    FROM performance_reviews 
),
Scores AS (
    SELECT employee_id, (next_next_rating - rating) AS improvement_score
    FROM Reviews
    WHERE rating < next_rating AND next_rating < next_next_rating AND rnks = 3
)
SELECT e.employee_id, name, improvement_score
FROM Scores AS s
LEFT JOIN employees AS e
USING(employee_id)
ORDER BY improvement_score DESC, name 