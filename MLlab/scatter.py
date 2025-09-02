import numpy as np
import matplotlib.pyplot as plt
def scatter_plot():
    x = np.random.randn(100)
    y = np.random.randn(100)
    plt.scatter(x, y)
    plt.title("Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()
scatter_plot()
