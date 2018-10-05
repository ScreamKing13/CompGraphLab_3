import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Наилучшие значения
#a = -0.4
#b = -0.25


fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.set_zlim()
a = -0.4
b = -0.25
x = np.arange(-20, 20)
y = np.arange(-15, 15)
x2 = 0
y2 = y
x2, y2 = np.meshgrid(x2, y2)
x, y = np.meshgrid(x, y)
z = (x-a)**2/a - (y-b)**2/b
surf = ax.plot_surface(x, y, z, linewidth=0, antialiased=True)
for i in range(-750, 1000, 25):
    ax.plot3D(xs=x2, ys=y2, zs=i, antialiased=True, color="r")
plt.show()
