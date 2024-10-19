import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
df = pd.read_csv(r'e:\New folder\DOTPY\cleaned_pizza_sales.csv')

# Convert columns to datetime with the specified format
df['order_time'] = pd.to_datetime(df['order_time'], format='%d-%m-%Y', errors='coerce')
df['order_date'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y', errors='coerce')

# A. KPI’s
# 1. Total Revenue
total_revenue = df['total_price'].sum()
print(f'Total Revenue: {total_revenue}')

# 2. Average Order Value
avg_order_value = df['total_price'].sum() / df['order_id'].nunique()
print(f'Average Order Value: {avg_order_value}')

# 3. Total Pizzas Sold
total_pizzas_sold = df['quantity'].sum()
print(f'Total Pizzas Sold: {total_pizzas_sold}')

# 5. Average Pizzas Per Order
avg_pizzas_per_order = df['quantity'].sum() / df['order_id'].nunique()
print(f'Average Pizzas Per Order: {avg_pizzas_per_order:.2f}')

# B. Hourly Trend for Total Pizzas Sold
hourly_trend = df.groupby(df['order_time'].dt.hour)['quantity'].sum()

if not hourly_trend.empty:
    plt.figure(figsize=(10, 5))
    hourly_trend.plot(kind='bar')
    plt.title('Hourly Trend for Total Pizzas Sold')
    plt.xlabel('Hour of Day')
    plt.ylabel('Total Pizzas Sold')
    plt.show()
else:
    print("No data available for hourly trend.")

# C. Weekly Trend for Total Orders
weekly_trend = df.groupby([df['order_date'].dt.isocalendar().week, df['order_date'].dt.year]).size()

plt.figure(figsize=(10, 5))
weekly_trend.plot()
plt.title('Weekly Trend for Orders')
plt.xlabel('Week Number')
plt.ylabel('Total Orders')
plt.show()

# D. % of Sales by Pizza Category
sales_by_category = df.groupby('pizza_category')['total_price'].sum()
percentage_sales_by_category = (sales_by_category / sales_by_category.sum()) * 100

plt.figure(figsize=(8, 8))
percentage_sales_by_category.plot(kind='pie', autopct='%1.1f%%')
plt.title('% of Sales by Pizza Category')
plt.ylabel('')
plt.show()

# E. % of Sales by Pizza Size
sales_by_size = df.groupby('pizza_size')['total_price'].sum()
percentage_sales_by_size = (sales_by_size / sales_by_size.sum()) * 100

plt.figure(figsize=(10, 5))
percentage_sales_by_size.plot(kind='bar')
plt.title('% of Sales by Pizza Size')
plt.ylabel('Percentage of Total Sales')
plt.show()

# F. Total Pizzas Sold by Pizza Category (for February)
february_data = df[df['order_date'].dt.month == 2]
total_pizzas_by_category = february_data.groupby('pizza_category')['quantity'].sum()

plt.figure(figsize=(10, 5))
total_pizzas_by_category.plot(kind='bar')
plt.title('Total Pizzas Sold by Pizza Category in February')
plt.xlabel('Pizza Category')
plt.ylabel('Total Quantity Sold')
plt.show()

# G. Top 5 Pizzas by Revenue
top_5_revenue = df.groupby('pizza_name')['total_price'].sum().nlargest(5)

plt.figure(figsize=(10, 5))
top_5_revenue.plot(kind='bar')
plt.title('Top 5 Pizzas by Revenue')
plt.xlabel('Pizza Name')
plt.ylabel('Total Revenue')
plt.show()

# H. Bottom 5 Pizzas by Revenue
bottom_5_revenue = df.groupby('pizza_name')['total_price'].sum().nsmallest(5)

plt.figure(figsize=(10, 5))
bottom_5_revenue.plot(kind='bar')
plt.title('Bottom 5 Pizzas by Revenue')
plt.xlabel('Pizza Name')
plt.ylabel('Total Revenue')
plt.show()

# I. Top 5 Pizzas by Quantity
top_5_quantity = df.groupby('pizza_name')['quantity'].sum().nlargest(5)

plt.figure(figsize=(10, 5))
top_5_quantity.plot(kind='bar')
plt.title('Top 5 Pizzas by Quantity Sold')
plt.xlabel('Pizza Name')
plt.ylabel('Total Quantity Sold')
plt.show()

# J. Bottom 5 Pizzas by Quantity
bottom_5_quantity = df.groupby('pizza_name')['quantity'].sum().nsmallest(5)

plt.figure(figsize=(10, 5))
bottom_5_quantity.plot(kind='bar')
plt.title('Bottom 5 Pizzas by Quantity Sold')
plt.xlabel('Pizza Name')
plt.ylabel('Total Quantity Sold')
plt.show()

# K. Top 5 Pizzas by Total Orders
top_5_orders = df.groupby('pizza_name')['order_id'].nunique().nlargest(5)

plt.figure(figsize=(10, 5))
top_5_orders.plot(kind='bar')
plt.title('Top 5 Pizzas by Total Orders')
plt.xlabel('Pizza Name')
plt.ylabel('Total Orders')
plt.show()

# L. Bottom 5 Pizzas by Total Orders
bottom_5_orders = df.groupby('pizza_name')['order_id'].nunique().nsmallest(5)

plt.figure(figsize=(10, 5))
bottom_5_orders.plot(kind='bar')
plt.title('Bottom 5 Pizzas by Total Orders')
plt.xlabel('Pizza Name')
plt.ylabel('Total Orders')
plt.show()