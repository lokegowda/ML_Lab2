import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  


df = pd.read_csv('toyotacorola.csv')


x = df['KM']
y = df['Doors']
z = df['Price']

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')


surf = ax.plot_trisurf(x, y, z, cmap='jet', edgecolor='none')


ax.set_xlabel('KM Driven')
ax.set_ylabel('Number of Doors')
ax.set_zlabel('Price')


fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)


plt.title('3D Price Visualization (KM vs Doors vs Price)')
plt.show()
