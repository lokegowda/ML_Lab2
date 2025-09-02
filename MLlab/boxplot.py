import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def box_plot():
    x = np.random.randn(100)
    sns.boxplot(x=x)
    plt.title("Box Plot")
    plt.show()
box_plot()
