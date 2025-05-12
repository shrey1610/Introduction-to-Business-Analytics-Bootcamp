import pandas as pd, matplotlib.pyplot as plt, numpy as ny
df=pd.read_csv('order_sales.csv')
x=df['product']
y=df['price']
fig,axs=plt.subplots(2,2, figsize=(10,8))
axs[0,0].plot(x,y,label='product x price')
axs[0,1].bar(x,y,label='product x price')
# histogram
# scatterplots
plt.legend()
plt.show()