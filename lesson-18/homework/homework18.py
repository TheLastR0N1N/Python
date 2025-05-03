# %% [markdown]
# Homework 2

# %%
import pandas as pd

# %%
df = pd.read_csv('stackoverflow_qa.csv')
df.head()

# %%
df['creationdate'] = pd.to_datetime(df['creationdate'], errors='coerce')
filt_year = df['creationdate'].dt.year < 2014

df[filt_year]

# %%
filt_score = df.score > 50

df[filt_score]

# %%
filt_score = df.score.between(50, 100)

df[filt_score]

# %%
filt_ans = df.ans_name == 'Scott Boston'

df[filt_ans]

# %%
df.head(6)

# %%
filt_anss = ['Wes McKinney', 'Mike Pennington', 'doug', 'Demitri', 'Scott Boston']

filtered_df = df[df['ans_name'].isin(filt_anss)]
filtered_df

# %%
# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

df['creationdate'] = pd.to_datetime(df['creationdate'], errors='coerce')
filt_year = df['creationdate'].dt.year == 2014
filt_month = df['creationdate'].dt.month.between(3,10)
filt_ans = df.ans_name == 'unutbu'
filt_score = df.score < 5


df[filt_year & filt_month & filt_ans & filt_score]

# %%
# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

filt_score = df.score.between(5,10)
filt_view = df.viewcount > 10000

df[filt_score | filt_view]

# %%
# Find all questions that are not answered by Scott Boston

filt_ans = df['ans_name'] == 'Scott Boston'
df_filtered = df[~filt_ans]
df_filtered


# %% [markdown]
# Homework 3

# %%
titanic_df = pd.read_csv("titanic.csv")
titanic_df.head()

# %%
# Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

f_gen = titanic_df.Sex == 'female'
f_class = titanic_df.Pclass == 1
f_age = titanic_df.Age.between(20,30)

filt = f_gen & f_class & f_age
titanic_df[filt]


# %%
# Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

f_fare = titanic_df.Fare > 100

titanic_df[f_fare]

# %%
# Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
df = pd.read_csv("titanic.csv")

df.columns = df.columns.str.strip()

f_companion = (df.SibSp == 0) & (df.Parch == 0)
f_survived = df.Survived == 1

filt = f_companion & f_survived
df[filt]

# %%
# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

f_embarked = df.Embarked == 'C'
f_fare = df.Fare > 50

df[f_embarked & f_fare]

# %%
# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.

f_companion = (df.SibSp > 0) & (df.Parch > 0)

filt = f_companion 
df[filt]

# %%
# Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

f_age = df.Age <= 15
f_survived = df.Survived == 0

filt = f_age & f_survived
df[filt]

# %%
# Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

f_cabin = df.Cabin.notna()
f_fare = df.Fare > 200

filt = f_fare & f_cabin
df[filt]

# %%
# Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

f_id = df.PassengerId % 2 != 0

df[f_id]

# %%
# Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.

f_unique = df.Ticket.value_counts()
f_unique = f_unique[f_unique == 1].index

unique_passengers = df[df['Ticket'].isin(f_unique)]

unique_passengers

# %%
# Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

f_combined = (df['Name'].str.contains('Miss', na=False)) & (df['Pclass'] == 1)
df[f_combined]

