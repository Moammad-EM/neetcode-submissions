-- Write your query below
SELECT DISTINCT name
FROM customers
WHERE id NOT IN (SELECT customer_id from orders);