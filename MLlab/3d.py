import numpy as np
import matplotlib.pyplot as plt
def plot_3d():
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    ax = plt.figure().add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title("3D Surface Plot")
    plt.show()
plot_3d()
