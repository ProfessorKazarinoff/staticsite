Title: Plotting a gaussian normal curve with Python and Matplotlib
Date: 2019-01-27 09:01
Modified: 2019-01-27 09:01
Status: Draft
Category: plotting
Tags: python, engineering, statistics, matplotlib
Slug: plotting-normal-curve-with-python
Authors: Peter D. Kazarinoff

![Area Under Normal Curve Plot]({filename}/images/area_under_normal_curve_plot.png)

In the [previous post]({filename}/posts/statistics/probability_under_a_normal_curve_with_python.md), we calculated the area under the standard normal curve using Python and the ```erf()``` function from the ```math``` module in Python's Standard Library. In this post, we will construct a plot that illustrates the standard normal curve and the area we calculated. To build the gaussian normal curve, we are going to use Python, Matplotlib, and a module called SciPy.

Calculating the probability under a normal curve is useful for engineers. This type of calculation can be helpful to predict the likely hood of a part coming off an assembly line being within a given specification when the statistical properties of all the parts that have come of the assembly line previously are known.

In this post, we will calculate the probability under the normal curve to answer a question like the one below:

#### Given:
In a facility that manufactures electrical resistors, a sample of 35 1-kΩ resistors are randomly pulled from the production line, and their resistances are measured and recorded. A mean resistance of 990 kΩ and a standard deviation of 10 kΩ represents the sample of resistors. The desired resistance tolerance for the resistor is ± 10%, meaning that the acceptable range of resistance is 900Ω to 1100Ω.

#### Find:
Assuming a normal distribution, determine the probability that a resistor coming off the production line will be within spec.

#### Solution:
To build the plot, we will use Python and a plotting package called Matplotlib. We will also use ```norm()``` function from the SciPy package. Both Matplotlib and SciPy come including when you install [Anaconda](https://anaconda.com/downloads). If you do not have Anaconda installed, Matplotlib and SciPy can be installed from the command line with **pip**.

```text
$ pip install matplotlib
$ pip install scipy
```

Before we build the plot, let's take a look at a gaussin curve. The shape of a gaussin curve is sometimes referred to as a "bell curve." This is the type of curve we are going to plot with Matplotlib.

![gaussian_curve]({filename}/images/normal_gaussian_curve.png)

Create a new Python script called ```normal_curve_.py```. At the top of the script, import NumPy, Matplotlib, and SciPy.

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

Now we need to define the constants given in the problem. The mean is ```998.8```, the standard deviation is ```72.1```. The lower bound is ```990``` and the upper bound is ```1100```. 

```python
# define constants
mu = 998.8 
sigma = 72.1
x1 = 990
x2 = 1100
```

Next, we calculate the Z-transform of the lower and upper bound ```x1``` and ```x2```.

```python
# calculate the z-transform
z1 = ( x1 - mu ) / sigma
z2 = ( x2 - mu ) / sigma
```

After the Z-transform of the lower and upper bound are calculated, we calculate the probability with SciPy's ```scipy.stats.norm.pdf()``` function.

```python
# change the range to cut off one end or other of the curve
x = np.arange(z1, z2, 0.001)
x_all = np.arange(-10, 10, 0.001)
# Mean = 0, SD = 1.
y = norm.pdf(x,0,1)
y2 = norm.pdf(x_all,0,1)
```

Finally, we'll build the plot. Note how Matplotlib's ```ax.fill_between()``` function is used to highlight the area of interest.

```python
# build the plot
fig, ax = plt.subplots()
ax.plot(x_all,y2)

ax.fill_between(x,y,0, alpha=0.5)
ax.fill_between(x_all,y2,0, alpha=0.2)
ax.set_xlim([-4,4])
ax.set_xlabel('# of Standard Deviations Outside the Mean')
ax.set_title('Normal Gaussian Curve')

plt.show()
```

The finished plot is below. Notice how the area corresponding to resistors in the given specification (between the upper and lower bounds) is shaded.

![Area Under Normal Curve Plot]({filename}/images/area_under_normal_curve_plot.png)