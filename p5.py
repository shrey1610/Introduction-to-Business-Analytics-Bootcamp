import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)
y4=1/(np.tan(x))
y5=1/(np.sin(x))
y6=1/(np.cos(x))
fig,axs=plt.subplots(2,3, figsize=(10,8))
axs[0,0].plot(x,y,label='sin(x)')
axs[0,1].plot(x,y2,label='cos(x)')
axs[0,2].plot(x,y3,label='tan(x)')
axs[1,0].plot(x,y5,label='cosec(x)')
axs[1,1].plot(x,y4,label='sec(x)')
axs[1,2].plot(x,y6,label='cot(x)')
plt.legend()
plt.show()

# .hist