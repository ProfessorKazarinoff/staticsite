Title: Calculating the probability under a normal curve with Python
Date: 2017-10-10 09:01
Modified: 2017-10-10 09:01
Status: Draft
Category: python
Tags: python, engineering, statistics
Slug: probability-under-normal-curve-with-python
Authors: Peter Kazarinoff
Series: Calculating the probability under a normal curve
series_index: 1

Calculating the probability under a normal curve is useful for engineers. This type of calculation can be useful to predict the likly hood of a part comming of an assembly line being within a given specification when the statistical properties of all the parts that have come of the assembly line previously are known. 

In this post we will calculate the probabiliy under the normal curve to answer a question like the one below:

Given: In a facility that manufactures electrical resistors, a sample of 35 1-kΩ resistors are randomly pulled from the production line, and their resistances are measured and recorded. A mean resitance of 990 kΩ standard deviation of 10 kΩ represents the sample of resistors. The desired resistance tolerance for the resistor is ± 10%, meaning that the acceptable range of resistance is 900Ω to 1100Ω.

Find: Assuming a standard distribution determine the probability that a resistor coming off the production line will be within spec.

To build our script we need to accomplish a couple of things

1. Import the necessary modules. We need to use the ```erf()``` function in the ```math``` module
2. Define the contants for this problem. The mean, standard deviation, lower bound and upper bound
3. Calculate the probability using the ```erf()``` function
4. Print the results to the Python interperater
5. Build a plot to show our results (this will be done in the second post of this series)

Let's take a look at a gaussin curve

![gaussian_curve]({filename}/images/gaussian_curve.png)



```python
from math import erf
```

Now we need to define our constants

```python

# define constants

```

Next we calculate the probability using the ```erf()``` function


```

# sample parameters
d = 1.778     # diameter of sample in mm
A0 = np.pi*(d/2)**2 # original cross-sectional area of sample in mm^2
L0 = 18.002   # original gauge length of sample (lenth of narrowest section)

# calcuate stress and strain
stress = (force/A0)
strain = delta_L/L0

# plot the stress strain curve
plt.plot(strain,stress)
plt.xlabel('Strain (mm/mm)')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curve of Al6061 - T6')
plt.axis([0, 1.4, 0, 60])
plt.grid(True)
plt.show()
```
