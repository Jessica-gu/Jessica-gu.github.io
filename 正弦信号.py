import numpy as np
import matplotlib.pyplot as plt 
import math
#math.sin(wt)
def domo(t):
    r=math.sin(t)
    return r
x=np.linspace(0,8.0,1000)
y=np.array([domo(t)for t in x])
plt.plot(x,y)
plt.title('sin function')
plt.show()