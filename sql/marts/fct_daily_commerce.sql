-- BigQuery Standard SQL
-- Assumes raw_olist orders, order_items, order_payments, and customers tables.
-- Replace project and dataset names before execution.

WITH order_items AS (
  SELECT
    order_id,
    SUM(price) AS product_revenue,
    SUM(freight_value) AS freight_revenue,
    COUNT(*) AS units
  FROM raw_olist.order_items
  GROUP BY order_id
),
payments AS (
  SELECT
    order_id,
    SUM(payment_value) AS payment_value
  FROM raw_olist.order_payments
  GROUP BY order_id
),
orders AS (
  SELECT
    o.order_id,
    c.customer_unique_id,
    DATE(o.order_purchase_timestamp) AS order_date,
    o.order_status,
    o.order_delivered_customer_date,
    o.order_estimated_delivery_date
  FROM raw_olist.orders AS o
  JOIN raw_olist.customers AS c
    ON o.customer_id = c.customer_id
  WHERE o.order_status = 'delivered'
)
SELECT
  order_date,
  COUNT(DISTINCT order_id) AS orders,
  COUNT(DISTINCT customer_unique_id) AS customers,
  SUM(units) AS units,
  ROUND(SUM(product_revenue), 2) AS product_revenue,
  ROUND(SUM(freight_revenue), 2) AS freight_revenue,
  ROUND(SUM(payment_value), 2) AS gross_revenue,
  ROUND(SAFE_DIVIDE(SUM(payment_value), COUNT(DISTINCT order_id)), 2) AS average_order_value,
  ROUND(AVG(DATE_DIFF(DATE(order_delivered_customer_date), order_date, DAY)), 1) AS avg_delivery_days,
  COUNTIF(DATE(order_delivered_customer_date) <= DATE(order_estimated_delivery_date)) AS on_time_deliveries
FROM orders
JOIN order_items USING (order_id)
JOIN payments USING (order_id)
GROUP BY order_date
ORDER BY order_date;
