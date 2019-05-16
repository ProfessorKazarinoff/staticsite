Title: Violin Plot using Python, matplotlib and seaborn
Date: 2017-10-21 16:00
Status: Draft
Author: Peter D. Kazarinoff

### Import the necessary packages
Pandas is used to read in the .csv data. Seaborn to build the plot and Matplotlib for displaying the plot.


```python
# seaborn violin plot

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```


```python
%matplotlib inline
```

### Read in the .csv data file
Use pandas ```pd.read_csv()``` function to read in the .csv file


```python
df = pd.read_csv('data.csv')
```

### Build the violin plot
Use seaborns built-in violin plot function to make the plot. The two fuction arguments are ```data=df``` and ```pallette="pastel"```.


```python
ax = sns.violinplot(data=df, palette="pastel")
plt.show()
```


![png]({static}/images/output_7_0.png)


### Save the figure
Save the figure using matplotlib's ax.get_figure() method and ```fig.savefig()``` method. Since seaborn produces a matplotlib axis object, we can use matplotlib methods on our ```ax``` object. 


```python
fig = ax.get_figure()
fig.savefig('sns_violin_plot.png', dpi=300)
```


```python
#seaborn violin plot

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

ax = sns.violinplot(data=df, palette="pastel")

fig = ax.get_figure()
fig.savefig('sns_violin_plot.png', dpi=300)
```


![png]({static}/images/output_10_0.png)