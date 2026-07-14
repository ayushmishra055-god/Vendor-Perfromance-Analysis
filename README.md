# 📦 Vendor Performance Analysis — Supply Chain Analytics

An end-to-end supply chain analytics project that evaluates **vendor/category-level delivery performance** using **Python, SQL (SQLite), and Power BI**, built on the **DataCo Global Supply Chain dataset**. The project models a proper dimensional data warehouse, runs advanced SQL window-function analytics, and visualizes the results in an interactive Power BI dashboard.

---

## 🧾 Overview

Using real-world supply chain transaction data, this project answers:

- Which product **categories/departments** have the highest late-delivery risk?
- How do **gross sales trends** move month over month per category (rolling averages)?
- Which departments have categories that are consistently **high-risk for delivery delays**?
- What's the overall **late delivery rate** across the shipping network?

The pipeline takes raw DataCo transaction data → cleans and models it into a star-schema warehouse → runs advanced SQL analytics with window functions → outputs a pre-aggregated KPI table for Power BI.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python (Pandas)** | Data loading and ETL into the warehouse |
| **SQLite (`sqlite3`)** | Relational data warehouse — dimension & fact tables |
| **SQL (Window Functions, CTEs)** | Advanced KPI aggregation and ranking |
| **Jupyter Notebook** | Exploratory Data Analysis (EDA) |
| **Power BI** | Interactive dashboard |

---

## 📁 Repository Structure
