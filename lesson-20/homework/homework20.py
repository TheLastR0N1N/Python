# %% [markdown]
# 1. Customer Purchases Analysis:
#     * Find the total amount spent by each customer on purchases (considering invoices).
#     * Identify the top 5 customers with the highest total purchase amounts.
#     * Display the customer ID, name, and the total amount spent for the top 5 customers.
# 

# %% [markdown]
# * Find the total amount spent by each customer on purchases (considering invoices).
# 

# %%
import pandas as pd
import sqlite3

# %%
conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()


# %%
cursor.execute("SELECT * FROM Customer;")
tables = cursor.fetchall()
print(tables)


# %%
import pandas as pd

customers = pd.read_sql_query("SELECT * FROM Customer;", conn)
customers.head()

# %%
invoices = pd.read_sql_query("select * from Invoice",conn)
invoices.head()

# %%
invoice_line = pd.read_sql_query("select * from InvoiceLine",conn)
invoice_line.head()

# %%
merged = customers.merge(invoices,on='CustomerId',how='right')
merged.head()

# %%
merged2 = merged.merge(invoice_line,on='InvoiceId')
merged2.head()

# %%
merged2['spent'] = merged2['UnitPrice'] * merged2['Quantity']
merged2.head()

# %%
total = merged2.groupby('CustomerId').agg({'spent':'sum'}).reset_index()
total2 = total.merge(customers[['CustomerId', 'FirstName', 'LastName']], on='CustomerId')
total2['FullName'] = customers['FirstName'] + ' ' + customers['LastName']

total2[['CustomerId','FullName','spent']].head()

# %% [markdown]
# * Identify the top 5 customers with the highest total purchase amounts.
# 

# %%
total2[['CustomerId','FullName','spent']].sort_values('spent',ascending=False).head(5)

# %% [markdown]
# 2. Album vs. Individual Track Purchases:
#     * Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
#     * A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
#     * Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).
# 

# %%
album = pd.read_sql_query("SELECT * FROM Album;", conn)
album.head()

# %%
track = pd.read_sql_query("select * from track",conn)
track.head()

# %%
al_tr_mer = track.merge(album,on='AlbumId')
al_tr_mer.head()

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



