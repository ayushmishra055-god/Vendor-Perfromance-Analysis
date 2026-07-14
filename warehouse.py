import sqlite3

# 1. Connect to SQLite database (creates a local file vendor_data_warehouse.db)
conn = sqlite3.connect('vendor_data_warehouse.db')
cursor = conn.cursor()

print("Creating relational table schemas...")

# Enable Foreign Key enforcement in SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Create Categories Dimension Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS dim_categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT,
    department_id INTEGER,
    department_name TEXT
);
''')

# Create Customers Dimension Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id INTEGER PRIMARY KEY,
    customer_fname TEXT,
    customer_lname TEXT,
    customer_city TEXT,
    customer_state TEXT
);
''')

# Create Logistics Fact Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS fact_logistics (
    order_id INTEGER,
    customer_id INTEGER,
    category_id INTEGER,
    order_date TEXT,
    days_shipping_real INTEGER,
    days_shipping_scheduled INTEGER,
    shipping_days_variance INTEGER,
    is_late_delivery INTEGER,
    is_anomalous_delay INTEGER,
    gross_sales REAL,
    net_revenue REAL,
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (category_id) REFERENCES dim_categories(category_id)
);
''')

conn.commit()
print("Success: Relational Data Warehouse structure initialized!")

#//
import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect('vendor_data_warehouse.db')

print("1. Loading clean CSV files into memory...")
dim_categories = pd.read_csv('dim_categories_clean.csv')
dim_customers = pd.read_csv('dim_customers_clean.csv')
fact_logistics = pd.read_csv('fact_logistics_clean.csv')

print("2. Mapping DataFrame columns to match SQL schemas...")
# Rename Category Dimension to match your SQL columns
dim_categories.columns = ['category_id', 'category_name', 'department_id', 'department_name']

# Rename Customer Dimension to match your SQL columns
dim_customers.columns = ['customer_id', 'customer_fname', 'customer_lname', 'customer_city', 'customer_state']

# (Note: fact_logistics columns were already renamed in our previous step, so they should be good!)

print("3. Migrating data into SQL tables...")
# Push data to SQL matching our exact DDL schemas
dim_categories.to_sql('dim_categories', conn, if_exists='append', index=False)
dim_customers.to_sql('dim_customers', conn, if_exists='append', index=False)
fact_logistics.to_sql('fact_logistics', conn, if_exists='append', index=False)

print("4. Running SQL validation check...")
# Query the database to prove the data actually made it inside
sample_check = pd.read_sql_query("SELECT COUNT(*) as total_rows FROM fact_logistics;", conn)

print(f"\n[SUCCESS] Data Warehouse is fully loaded! You have {sample_check['total_rows'][0]} rows securely stored in your fact table.")