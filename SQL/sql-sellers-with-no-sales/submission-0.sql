-- Write your query below
SELECT DISTINCT seller_name
FROM seller
WHERE seller_id NOT IN (SELECT seller_id FROM orders NATURAL JOIN seller WHERE TO_CHAR(sale_date,'YYYY') = '2020')
ORDER BY seller_name;