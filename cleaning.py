import pandas as pd

#load data

vendors = pd.read_csv("C:/Users/VICTUS/Desktop/Vendor_performance_analysis/Data/vendors.csv/vendors.csv")
orders = pd.read_csv("C:/Users/VICTUS/Desktop/Vendor_performance_analysis/Data/orders.csv/orders.csv")
quality = pd.read_csv("C:/Users/VICTUS/Desktop/Vendor_performance_analysis/Data/quality.csv/quality.csv")

#convert dates

orders['order_date']=pd.to_datetime(orders['order_date'])
orders['delivery_date']=pd.to_datetime(orders['delivery_date'])

#remove duplicates

orders=orders.drop_duplicates()

#merge column

orders['delivery_delay']=(orders['delivery_date']-orders['order_date']).dt.days
orders['on_time']=orders['delivery_delay'].apply(lambda x:1 if x<=3 else 0)

#merge table

data=orders.merge(quality,on='order_id')
data=data.merge(vendors,on='vendor_id')

#create defect rate

data['defect_rate']=data['defective_quantity']/data['quantity']

#save cleaned data

data.to_csv("C:/Users/VICTUS/Desktop/Vendor_performance_analysis/Data/cleaned_data.csv/cleaned.csv",index=False)

print("CLEANED")