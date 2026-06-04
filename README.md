# Vendor Performance Analysis

## Project Overview

This project analyzes vendor performance using MySQL, Python, and Power BI. The objective is to evaluate suppliers based on key operational and quality metrics, helping organizations identify reliable vendors and improve procurement decisions.

The project follows a complete data analytics workflow including data storage, cleaning, KPI calculation, and dashboard visualization.

---

## Tools & Technologies

* MySQL
* Python (Pandas)
* Power BI
* CSV Data Sources

---

## Project Workflow

### 1. Data Collection

Vendor and order data were collected and stored in CSV files.

### 2. Database Creation

A MySQL database was created to store vendor and order information.

### 3. Data Cleaning

Python was used to:

* Handle missing values
* Validate records
* Clean inconsistent data
* Prepare datasets for analysis

### 4. KPI Calculation

SQL queries were used to calculate vendor performance metrics.

### 5. Dashboard Development

Power BI was used to create an interactive dashboard for vendor performance monitoring.

---

## Key Performance Indicators (KPIs)

### On-Time Delivery Percentage (%)

Measures the percentage of orders delivered on or before the expected delivery date.

Formula:

On-Time Delivery % = (On-Time Orders / Total Orders) × 100

---

### Average Delivery Delay (Days)

Measures the average delay in deliveries across all orders.

Formula:

Average Delay = Total Delay Days / Total Orders

---

### Defect Rate (%)

Measures the percentage of defective items supplied by a vendor.

Formula:

Defect Rate % = (Defective Quantity / Total Quantity) × 100

---

### Average Cost per Order

Measures the average procurement cost associated with each vendor.

Formula:

Average Cost = Total Cost / Number of Orders

---

## SQL KPIs Generated

```sql
SELECT
    vendor_id,
    ROUND(SUM(on_time)*100.0 / COUNT(*), 2) AS on_time_percentage,
    ROUND(AVG(delivery_delay), 2) AS avg_delay,
    ROUND(AVG(defect_rate)*100, 2) AS defect_rate,
    ROUND(AVG(cost), 2) AS avg_cost
FROM orders
GROUP BY vendor_id;
```

---

## Dashboard Features

* Vendor-wise KPI comparison
* On-Time Delivery Analysis
* Average Delivery Delay Tracking
* Defect Rate Monitoring
* Cost Analysis
* Interactive filtering and reporting

---

## Repository Structure

```text
Vendor-Performance-Analysis/
│
├── maincode.sql
├── cleaning.py
├── vendors.csv
├── orders.csv
├── quality.csv
├── cleaned.csv
├── Vendor_analysis_final.pbix
└── README.md
```

---

## Business Impact

This analysis helps organizations:

* Identify top-performing vendors
* Monitor delivery efficiency
* Reduce procurement risks
* Track product quality issues
* Optimize supplier selection processes

---

## Author

Ayush Mishra

Data Analytics Project using MySQL, Python, and Power BI.
