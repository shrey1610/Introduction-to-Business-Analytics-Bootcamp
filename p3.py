import pandas as pd
df=pd.read_csv('light_spotify_dataset.csv')
# print(df)
df1=df.head(2000)
# print(df1)
df1.isnull()
df1.drop_duplicates()
df1.dropna()
# df1.to_csv('updated_spotify_list.csv',index=False)