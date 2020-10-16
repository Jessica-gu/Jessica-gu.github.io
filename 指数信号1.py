import math 
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig=plt.figure (figsize=(6,4))
ax=axisartist.Subplot(fig,111)
fig.add_axes(ax)

def exponential_func(x, a=2):
    y=math.pow(a, x)
    return y
x=np.linspace(-4, 4, 40)
y=[exponential_func(x) for x in x]
ax.plot(x,y)
plt.show()
print(max(x), max(y))
ax.axis[:].set_visibel(False)
ax.axis["x"]=ax.new_floating_axis(0, 0, axis_direction="bottom")
ax.axis["y"]=ax.new_floating_axis(1, 0, axis_direction="bottom")