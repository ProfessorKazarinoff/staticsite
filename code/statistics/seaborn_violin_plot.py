import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv', header=0)

ax = sns.violinplot(data=df, palette="pastel")
ax.set_ylabel('Density ($g/cm^3$)')
ax.set_title('Density of IKEA wood blocks organized by shape')
plt.show()