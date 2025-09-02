import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def heat_map():
    data = np.random.rand(10, 10)
    sns.heatmap(data, cmap='viridis')
    plt.title("Heatmap")
    plt.show()
heat_map()
