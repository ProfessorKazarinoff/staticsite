Title: Plotting a gaussian normal curve with Python and matplotlib
Date: 2017-12-24 09:01
Modified: 2017-12-24 09:01
Status: Draft
Category: plotting
Tags: python, engineering, statistics, matplotlib
Slug: plotting-normal-curve-with-python
Authors: Peter D. Kazarinoff
Series: Calculating the probability under a normal curve
series_index: 2

In the previous post, we calculated the area under the standard normal curve using Python and the ```erf()``` function from the ```math``` module in the standard library. In this post, we will construct a plot that illustrates the standard normal curve and the area we calculated. To do this we are going to use Python, matplotlib, and a module called seaborn. 

Calculating the probability under a normal curve is useful for engineers. This type of calculation can be useful to predict the likely hood of a part coming of an assembly line being within a given specification when the statistical properties of all the parts that have come of the assembly line previously are known. 

In this post we will calculate the probability under the normal curve to answer a question like the one below:

Given: In a facility that manufactures electrical resistors, a sample of 35 1-kΩ resistors are randomly pulled from the production line, and their resistances are measured and recorded. A mean resistance of 990 kΩ and a standard deviation of 10 kΩ represents the sample of resistors. The desired resistance tolerance for the resistor is ± 10%, meaning that the acceptable range of resistance is 900Ω to 1100Ω.

Find: Assuming a standard distribution, determine the probability that a resistor coming off the production line will be within spec.

To build our script we need to accomplish a couple of things

Let's take a look at a gaussin curve

![gaussian_curve]({filename}/images/normal_gaussian_curve.png)

```python
# normal_curve.py

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm
%matplotlib inline
mpl.rcParams['savefig.dpi'] = 80
mpl.rcParams['figure.figsize'] = (6,9)
```

Now we need to define our constants

```python
# define constants
mu = 998.8 
sigma = 72.1
x1 = 990
x2 = 1100
```

We can calculate the z-transform of each of the ```x1``` and ```x2```.

```python
# calculate the z-transform
z1 = ( x1 - mu ) / sigma
z2 = ( x2 - mu ) / sigma
```

Next we calculate the probability build the curve with scipy's ```scipy.stats.norm.pdf()``` function.

```python
# change the range to cut off one end or other of the curve
x = np.arange(z1, z2, 0.001)
x_all = np.arange(-10, 10, 0.001)
# Mean = 0, SD = 1.
y = norm.pdf(x,0,1)
y2 = norm.pdf(x_all,0,1)
```

Finally, we'll build the plot

```python
# build the plot
fig, ax = plt.subplots()
ax.plot(x_all,y2)
ax.fill_between(x,y,0, alpha=0.5)
ax.fill_between(x_all,y2,0, alpha=0.2)
plt.xlim([-4,4])
plt.xlabel('# of standard deviations outside the mean')
plt.title('Normal Gaussian Curve')
plt.show()
```

The finished plot is below. Notice how the area corresponding to resistors in given specification are shaded.

![Area Under Normal Curve Plot]({filename}/images/area_under_normal_curve_plot.png)