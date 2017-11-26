import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read in the data
df = pd.read_csv('data.csv')

#plot the data
ax = sns.barplot(data=df, palette="pastel", errwidth=1, capsize=0.1)

#customize the plot
ax.set_ylabel('Density ($g/cm^3$)')
ax.set_title('Density of IKEA wood blocks organized by shape')

#show the plot
plt.show()