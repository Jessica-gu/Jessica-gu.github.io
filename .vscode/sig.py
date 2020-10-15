import numpy as np
import matplotlib.pyplot as plt
def rect_wave(t,c0,c):
    if t>=c+c0:
        r=0.0
    elif t<c0:
        r=0.0
    else:
        r=1.0
    return r
x=np.linspace(0,4,1000)#创建等差数列
y=np.array([rect_wave(t,1.0,2.0)for t in x])
plt.ylim(0,2)#设置纵轴的上下限
plt.plot(x,y)
plt.title("aaa")
plt.show()