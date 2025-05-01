# %% [markdown]
# Homework 1

# %%
import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
    'Age': [25, 30, 35, 40], 
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
} 

df = pd.DataFrame(data)

df.columns = ['first_name', 'age', 'city']

df

# %%
df.head(3)

# %%
mean = df['age']

mean.mean()

# %%
df[['first_name','city']]

# %%
df['salary'] = '4000','2999','1343','1233'

# %%
df

# %%
df.describe()


# %% [markdown]
# Homework 2

# %%
sales_and_expenses = {
    'Month': ['Jan','Feb','March','Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

df2 = pd.DataFrame(sales_and_expenses)


# %%
sne = df2[['Sales','Expenses']]
sne.max()

# %%
sne.min()

# %%
sne.mean()

# %% [markdown]
# Homework 3

# %%
expenses = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'], 
    'January': [1200, 200, 300, 150], 
    'February': [1300, 220, 320, 160], 
    'March': [1400, 240, 330, 170], 
    'April': [1500, 250, 350, 180]
}

df3 = pd.DataFrame(expenses)

# %%
summary = df3.groupby('Category').mean().round(1)
summary = summary.reset_index().set_index('Category')

summary

# %%
df3

# %%
summary = df3.groupby('Category').max().round(1)
summary = summary.reset_index().set_index('Category')

summary

# %%
summary = df3.groupby('Category').min().round(1)
summary = summary.reset_index().set_index('Category')

summary


