-- Write your query below
SELECT name, SUM(distance) as travelled_distance
FROM (
    SELECT user_id, name, COALESCE(distance, 0) AS distance
    FROM users u LEFT JOIN rides r ON (u.id = r.user_id)
    )
GROUP BY name
ORDER BY travelled_distance DESC, name;