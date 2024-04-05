# Write your MySQL query statement below
(SELECT
    u.name AS results
FROM
    Users u LEFT JOIN MovieRating mr
ON
    u.user_id = mr.user_id
GROUP BY
    mr.user_id
ORDER BY
    COUNT(mr.rating) DESC, u.name ASC
LIMIT 1)
UNION ALL
(SELECT
    m.title AS results
FROM
    Movies m LEFT JOIN MovieRating mr
ON
    m.movie_id = mr.movie_id
WHERE
    mr.created_at > '2020-01-31' AND mr.created_at < '2020-03-01'
GROUP BY
    mr.movie_id
ORDER BY
    AVG(mr.rating) DESC, m.title ASC
LIMIT 1)