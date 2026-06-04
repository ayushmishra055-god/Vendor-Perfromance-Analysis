CREATE DATABASE vendor_analysis;
USE vendor_analysis;
CREATE TABLE vendors (
    vendor_id VARCHAR(10),
    vendor_name VARCHAR(50)
);

CREATE TABLE orders (
    order_id VARCHAR(10),
    vendor_id VARCHAR(10),
    order_date DATE,
    delivery_date DATE,
    quantity INT,
    cost INT,
    delivery_delay INT,
    on_time INT,
    defective_quantity INT,
    defect_rate FLOAT
);

SELECT 
    vendor_id,
    ROUND(SUM(on_time)*100.0 / COUNT(*), 2) AS on_time_percentage,
    ROUND(AVG(delivery_delay), 2) AS avg_delay,
    ROUND(AVG(defect_rate)*100, 2) AS defect_rate,
    ROUND(AVG(cost), 2) AS avg_cost
FROM orders
GROUP BY vendor_id;