# %% [markdown]
# Homework Assignment 1: Analyzing Sales Data
# 
# Task 1:
# 
# Group the data by the Category column and calculate the following aggregate statistics for each category:
#  * Total quantity sold.
#  * Average price per unit.
#  * Maximum quantity sold in a single transaction.
# 

# %%
import pandas as pd
import numpy as np

# %%
sales = pd.read_csv('sales_data.csv')


# %%
sales.head()

# %%
(sales.groupby('Category')
                        .agg({'Quantity':'sum','Price':'mean','Quantity':'max'})
                        .reset_index())

# %% [markdown]
# Task 2:
# 
# Identify the top-selling product in each category based on the total quantity sold.
# 

# %%
grouped = sales.groupby(['Category', 'Product']).agg({'Quantity': 'sum'}).reset_index()

top_selling = (
    grouped
    .sort_values(['Category', 'Quantity'], ascending=False)
    .groupby('Category')
    .first()  
    .reset_index()
)

top_selling

# %% [markdown]
# Task 3:
# 
# Find the date on which the highest total sales (quantity * price) occurred.
# 

# %%
sales['Total'] = sales['Quantity'] * sales['Price']


# %%
date = sales.groupby(['Date']).agg({'Total': 'sum'}).reset_index()


# %%
daily_totals = sales.groupby('Date')['Total'].sum().reset_index()

top_sales = daily_totals.sort_values('Total', ascending=False).head(1)


# %%
top_sales

# %% [markdown]
# Homework Assignment 2: Examining Customer Orders
# 
# Tasks 1:
# 
# Group the data by CustomerID and filter out customers who have made less than 20 orders.
# 

# %%
customer = pd.read_csv('customer_orders.csv')

# %%
customer.head(3)

# %%
order_count = customer.groupby('CustomerID')['OrderID'].count()

# %%
low_order_customers = order_count[order_count < 20].index


# %%
filtered = customer[customer['CustomerID'].isin(low_order_customers)]


# %%
filtered

# %% [markdown]
# Task 2:
# 
# Identify customers who have ordered products with an average price per unit greater than $120.
# 

# %%
customer['AvgPricePerUnit'] = customer['Price'] / customer['Quantity']

customers_above_120 = customer[customer['AvgPricePerUnit'] > 120]

result = customers_above_120[['CustomerID', 'AvgPricePerUnit']].drop_duplicates()
result

# %% [markdown]
# Task 3:
# 
# Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
# 

# %%
customer.head(10)

# %%
totals = customer.groupby('Product').agg({'Price':'sum','Quantity':'sum'}).reset_index()
filt = totals[totals['Quantity'] >= 5]
result = filt[['Product', 'Quantity','Price']]
result

# %% [markdown]
# Homework Assignment 3: Population Salary Analysis
# 
# Task 1:
# 
# * "task\population salary analysis.xlsx" file defines Salary Band categories.
# * Read the data from population table and calculate following measures:
# * Percentage of population for each salary category;
# * Average salary in each salary category;
# * Median salary in each salary category;
# * Number of population in each salary category;
# 

# %%
import pyodbc

connection = pyodbc.connect( 
                               'DRIVER={SQL Server};'
                               'Server=DESKTOP-L4RJI31;'
                               'Database=F19_SQL;'
                               'trusted_Connection=yes;'
                               )
print('Connected Successfully')

cursor = connection.cursor()



# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%



