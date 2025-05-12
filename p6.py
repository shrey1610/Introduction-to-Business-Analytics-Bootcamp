import pandas as pd,matplotlib.pyplot as plt, numpy as np
df=pd.read_csv('updated_spotify_list.csv')
x=df['Genre']
y=df['song']
fig,axs=plt.subplots(2,2,figsize=(10,8))
axs[1,0].bar(x,y,color='g')
plt.show()