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

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns

```

Now we need to define our constants

```python

# define constants

# define constants

mu = 979.8    # mean = 978.8 kΩ
sigma = 73.1  # standard deviation = 73.1 kΩ
x1 = 900      # lower bound = 900 kΩ
x2 = 1100     # upper bound = 1100 kΩ

```

Next we calculate the probability build the curve with scipy's ```scipy.stats.norm.pdf()``` function

```
# plot the data

plt.plot(data)
plt.show()
```
