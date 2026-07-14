import sqlite3
import pandas as pd

# Connect to your fresh data warehouse
conn = sqlite3.connect('vendor_data_warehouse.db')

print("Executing Advanced Supply Chain Window Query...")

# The complex analytical query
sql_kpi_query = """
WITH Monthly_Vendor_Performance AS (
    SELECT 
        c.category_name AS vendor_category,
        c.department_name,
        SUBSTR(f.order_date, 1, 7) AS reporting_month,
        COUNT(f.order_id) AS total_shipments,
        ROUND(SUM(f.gross_sales), 2) AS total_gross_sales,
        ROUND(AVG(f.shipping_days_variance), 2) AS avg_delay_days,
        SUM(f.is_late_delivery) AS late_deliveries
    FROM fact_logistics f
    JOIN dim_categories c ON f.category_id = c.category_id
    GROUP BY c.category_name, SUBSTR(f.order_date, 1, 7)
),
Calculated_Metrics AS (
    SELECT 
        vendor_category,
        department_name,
        reporting_month,
        total_shipments,
        total_gross_sales,
        avg_delay_days,
        ROUND((CAST(late_deliveries AS REAL) / total_shipments) * 100, 2) AS late_delivery_rate,
        
        -- WINDOW FUNCTION 1: 3-Month Moving Average of Gross Sales to map category volume growth
        ROUND(AVG(total_gross_sales) OVER (
            PARTITION BY vendor_category 
            ORDER BY reporting_month
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ), 2) AS rolling_3_month_sales_avg,
        
        -- WINDOW FUNCTION 2: Rank product lines by failure rates within their master departments
        DENSE_RANK() OVER (
            PARTITION BY department_name 
            ORDER BY avg_delay_days DESC
        ) AS risk_rank_within_department
    FROM Monthly_Vendor_Performance
)
SELECT * 
FROM Calculated_Metrics
WHERE total_shipments > 10
ORDER BY department_name, risk_rank_within_department ASC;
"""

# Extract the calculations directly into a pandas DataFrame
kpi_summary_df = pd.read_sql_query(sql_kpi_query, conn)

# Export this calculated layer to a CSV so Power BI can ingest it as a pre-calculated aggregate table
kpi_summary_df.to_csv('sql_vendor_kpis.csv', index=False)

print("\n--- SAMPLE SQL OUTPUT (Top 10 High-Risk Areas) ---")
print(kpi_summary_df.head(10).to_string())
print("\n[SUCCESS] Complex SQL KPI Layer generated and exported to 'sql_vendor_kpis.csv'!")