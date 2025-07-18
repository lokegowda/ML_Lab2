import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv('toyotacorola.csv')

sns.pairplot(df)
plt.suptitle('pair wise scatter plot of dataset',y=10)
plt.show