import pandas as pd

# Sample data: Revenue and Tax Rate
data = {
    'Order_ID': [1, 2, 3, 4],
    'Revenue': [100, 150, 200, 130],
    'Tax_Rate': [0.18, 0.18, 0.20, 0.18]
}
df = pd.DataFrame(data)

# Use a lambda function with apply to calculate revenue after tax
df['Revenue_After_Tax'] = df.apply(lambda row: row['Revenue'] * (1 + row['Tax_Rate']), axis=1)

# Use a lambda function to categorize orders as 'High' or 'Low' value
df['Value_Category'] = df['Revenue'].apply(lambda x: 'High' if x >= 150 else 'Low')

print(df)