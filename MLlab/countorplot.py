import numpy as np
import matplotlib.pyplot as plt
def counter_plot():
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X**2 + Y**2)
    plt.figure(figsize=(6, 5))
    contour = plt.contourf(X, Y, Z, cmap='coolwarm')
    plt.colorbar(contour)
    plt.title("Contour Plot")
    plt.show()
counter_plot()

