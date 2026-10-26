# Write your MySQL query statement below
SELECT product_name,year,price
FROM Sales Join Product
on sales.product_id = Product.product_id;
-- Group by sale_id;