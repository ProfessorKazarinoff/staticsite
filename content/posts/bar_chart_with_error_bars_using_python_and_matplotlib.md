Title: Creating a bar chart with error bars using Python and matplotlib
Date: 2017-10-11 20:32
Modified: 2017-10-11 20:32
Status: Draft
Category: matplotlib
Tags: python, matplotlib, engineering, materials science, statistics
Slug: python-matplotlib-error-bars
Authors: Peter Kazarinoff
JavaScripts: table.js
Stylesheets: table.css
Series: Statistics
series_index: 1
Summary: Error bars are useful in engineering to show the confidence or precision in a set of measurements or calculated values. Bar charts without error bars give the illusion that a measured or calculated value is known to a high precision. In this post we will build a bar chart for the coefficient of thermal expansion (CTE) for three different materials based on a small data set. We will then add error bar to this chart based on the standard deviation of the data.

Error bars are useful in engineering to show the confidence or precision in a set of measurements or calculated values. Bar charts without error bars give the illusion that a measured or calculated value is known to a high precision. In this post we will build a bar chart using python and matplotlib for the coefficient of thermal expansion (CTE) for three different materials based on a small data set. We will then add error bar to this chart based on the standard deviation of the data.

A bar chart with error bars is shown below. Note the labels on the x-axis and the error bars at the top of each bar.

![plot with error bars]({filename}/images/bar_plot_with_error_bars.png)

In order to build this plot, we need a couple of things

|Asset|Description|
|---|---|
Python| Run the program |
conda prompt	| create the virtual environment and install packages |
numpy	| calculate the mean and standard deviation	|
matplotlib	| build the plot	|



To get going, we'll use the **conda prompt** to create a new virtual environment. Select **Anaconda Prompt** from the windows start menu.

![conda prompt on windows start menu]({filename}/images/conda_in_windows_start_menu.png)


Once you have the conda prompt open, type the following command to create a new virtual environment:

```
conda create -n errorbars
```

Then to activate our new virtual environment, type the following into the **conda prompt**

```
activate errorbars
```

Now that the errorbars virtual environment is active, you shoud see ```(errorbars)``` in parenthesis before the **conda prompt**.
Next install ```matplotlib``` and ```numpy``` using conda. pip will work to install these packages as well. You can write both packages on the same line or use two different ```conda install``` lines.

```
conda install matplotlib numpy
```

Make sure that our ```(errorbars)``` virtual environment has matplotlib and numpy installed:

```
conda list
```



Now create a new Python script called ***errorbars.py***. At the top of the script we need to import ```numpy``` and ```matplotlib```.

```python
#errorbars.py

import numpy as np
import matplotlib.pyplot as plt

```

Next we need to read in our data. The chart below shows the different measurement data for the coefficient of thermal expansion (CTE) of the metals:

### Coefficient of thermal expansion of three metals (units: /  &#176;C) 
 Sample | Aluminum | Copper | Steel 
 ----- | ------------- | ------------- | ------------- 
 1 | 6.4e-5  | 4.5e-5  | 3.3e-5  
 2 | 3.01e-5  | 1.97e-5  | 1.21e-5  
 3 | 2.36e-5  | 1.6e-5  | 0.9e-5  
 4 | 3.0e-5  | 1.97e-5 | 1.2e-5  
 5 | 7.0e-5  | 4.0e-5  | 1.3e-5  
 6 | 4.5e-5  | 2.4e-5  | 1.6e-5  
 7 | 3.8e-5 | 1.9e-5  | 1.4e-5 
 8 | 4.2e-5  | 2.41e-5  | 1.58e-5  
 9 | 2.62e-5  | 1.85e-5  | 1.32e-5  
 10 | 3.6e-5  | 3.3e-5  | 2.1e-5  

We will add these to three different numpy arrays by adding the following to ***errorbars.py***

```
# Enter in the raw data
Aluminum = np.array([6.4e-5 , 3.01e-5 , 2.36e-5, 3.0e-5, 7.0e-5, 4.5e-5, 3.8e-5, 4.2e-5, 2.62e-5, 3.6e-5])
Copper = np.array([4.5e-5 , 1.97e-5 , 1.6e-5, 1.97e-5, 4.0e-5, 2.4e-5, 1.9e-5, 2.41e-5 , 1.85e-5, 3.3e-5 ])
Steel = np.array([3.3e-5 , 1.2e-5 , 0.9e-5, 1.2e-5, 1.3e-5, 1.6e-5, 1.4e-5, 1.58e-5, 1.32e-5 , 2.1e-5])
```


Now we need to calculate the mean (or average) for each of the three materials using numpy's ```np.mean()``` function. The means will be the height of each bar in our chart.

```
# Calculate the average
Aluminum_mean = np.mean(Aluminum)
Copper_mean = np.mean(Copper)
Steel_mean = np.mean(Steel)
```

Next we'll calculate the standard deviation using numpy's ```np.std()``` function. On the plot, we will use the standard deviation as the hight of our error bars. The positive error will be +1 standard deviation and the negative error will be -1 standard deviation. 

```
Aluminum_std = np.std(Aluminum)
Copper_std = np.std(Copper)
Steel_std = np.std(Steel)
```

There are a couple more things needed to build the plot. We need the names to go along for our x-axis. We'll assign these as list of strings in a variable called ```materials```. We also need the means of the coefficients of thermal expansion, the data we are going to plot. We'll put these into a python list called ```CTEs```. Our standard deviations will be used for the height of the error bars. Those will go together in a list called ```error```. Let's code all of these list into our ***errorbars.py*** script.

```
# Create Arrays for the plot
materials = ['Aluminum', 'Copper', 'Steel']
x_pos = np.arange(len(materials))
CTEs = [Aluminum_mean, Copper_mean, Steel_mean]
error = [Aluminum_std, Copper_std, Steel_std]
```


Now it's time to build the plot. We are going to build a bar chart with three different bars, one bar for each material: Aluminum, Copper and Steel. We are going to put labels on the x-axis that shows each material name and a label on the y-axis with the title "Coefficient of thermal expansion (&#176;C<sup>-1</sup>)". We can save the figure to a file called ***bar_plot_with_error_bars.png*** using matplotlib's ```plt.savefig()``` function.

```
# Build the plot
fig, ax = plt.subplots()
ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Coefficient of Thermal Expansion ($\degree C^{-1}$)')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials)
ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
ax.yaxis.grid(True)

plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
plt.show()
```

The final plot looks like this:

![plot with error bars]({filename}/images/bar_plot_with_error_bars.png)