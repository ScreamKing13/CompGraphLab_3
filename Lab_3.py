import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')
a = 1
b = 1
x = np.arange(-50, 50)
y = np.arange(-50, 50)
x, y = np.meshgrid(x, y)
z = (x-a)**2/a - (y-b)**2/b
surf = ax.plot_surface(x, y, z, linewidth=0, antialiased=True)
plt.show()
