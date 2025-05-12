import pandas as pd
df=pd.read_csv('top-1000-trending-youtube-videos.csv')
# # print(df['Likes'].describe())
# print(df.info())
# print(df.describe())

df1=pd.read_csv('updated_spotify_list.csv')
print(df1.describe())
# print(df1.info())