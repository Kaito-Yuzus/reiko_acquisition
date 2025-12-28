import sqlite3
import pandas as pd
# from tabulate import tabulate

conn = sqlite3.connect('Login Data.db')
table1 = 'logins'

df = pd.read_sql_query(f"SELECT * FROM {table1}", conn)

filtered_columns = []

for col in df.columns:
    first_value = df[col].iloc[0]  # get the first value of the column
    if not isinstance(first_value, bytes):
        filtered_columns.append(col)  # keep the column if it's not bytes

# Create a new DataFrame with only the filtered columns
filtered_df = df[filtered_columns]

# Display results
print("Filtered Columns:")
for col in filtered_columns:
    print(col)

print("\nFiltered DataFrame:")
for index, row in filtered_df.iterrows():
    print(row.tolist())



















