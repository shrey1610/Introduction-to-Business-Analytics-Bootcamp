import pandas as pd

# Sample data: create a DataFrame with date and time strings
data = {
    'Order_ID': [1, 2, 3, 4],
    'Order_DateTime': [
        '2024-01-15 09:30:00',
        '2024-02-20 15:45:00',
        '2024-02-28 11:20:00',
        '2024-03-05 18:05:00'
    ],
    'Revenue': [100, 150, 200, 130]
}
df = pd.DataFrame(data)

# Convert 'Order_DateTime' to datetime format
df['Order_DateTime'] = pd.to_datetime(df['Order_DateTime'])

# Extract year, month, day, hour, minute, and second for further analysis
df['Year'] = df['Order_DateTime'].dt.year
df['Month'] = df['Order_DateTime'].dt.month
df['Day'] = df['Order_DateTime'].dt.day
df['Hour'] = df['Order_DateTime'].dt.hour
df['Minute'] = df['Order_DateTime'].dt.minute
df['Second'] = df['Order_DateTime'].dt.second
print(df)