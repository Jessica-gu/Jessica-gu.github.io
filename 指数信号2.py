import numpy as np
import matplotlib.pyplot as plt
import math 
a=-0.6
def zhishu(t):
    r=math.exp(a*t)
    return r
x=np.linspace(0,10,1000)
y=np.array([zhishu(t)for t in x])
plt.plot(x,y)
plt.title('Index signal')
plt.show()