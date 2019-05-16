Title: Calculating the probability under a normal curve with Python
Date: 2019-01-24 09:01
Modified: 2019-01-24 09:01
Status: published
Category: statistics
Tags: python, engineering, statistics
Slug: probability-under-normal-curve-with-python
Authors: Peter D. Kazarinoff

![gaussian_curve]({static}/images/gaussian_curve.png)

Calculating the probability under a normal curve is useful for engineers. This type of calculation can be helpful to predict the likely hood of a part coming off an assembly line being within a given specification. The probability can be calculated when the statistical properties of all the parts that have come of the assembly line are known. 

In this post, we will calculate the probability under the normal curve to answer a question like the one below:

### GIVEN:
At a facility that manufactures electrical resistors, a statistical sample of 1-kΩ resistors is pulled from the production line. The resistor's resistances are measured and recorded. A mean resistance of 979.8 kΩ and a standard deviation of 73.10 kΩ represents the sample of resistors. The desired resistance tolerance for the 1-kΩ resistors is ± 10%. This tolerance range means the acceptable range of resistance is 900 Ω to 1100 Ω.

### FIND:
Assuming a normal distribution, determine the probability that a resistor coming off the production line will be within spec (in the range of 900 Ω to 1100 Ω).

### SOLUTION:
The Python script we are going to build to solve the resistor problem above needs to accomplish a couple of things:

1. Import the necessary functions. We need to use the ```erf()``` and ```sqrt()``` functions in Python's ```math``` module.
2. Define the constants for this problem. The mean, standard deviation, lower bound and upper bound will be defined.
3. Calculate the probability using the ```erf()``` function from Python's ```math()``` module.
4. Print the results to the Python interpreter

Let's take a look at a Gaussian curve.

![gaussian_curve]({static}/images/gaussian_curve.png)

The shape of the curve describes the spread of resistors coming off the production line. We need to find the area under the curve within our upper and lower bounds to solve the problem.

Open up a new Python script called **_stats.py_**. In the first line of code, we import the ```erf``` and ```sqrt()``` functions from the ```math``` module. Because the ```math``` module is part of the Python Standard Library, ```math``` does not need to be installed using ```conda``` or ```pip```.

```python
# stats.py

from math import erf, sqrt
```

Now we need to define the constants. The mean is 978.8 kΩ, and the standard deviation is 73.1 kΩ. The acceptable range of resistance is between 900 kΩ and 1100 kΩ. These two values, 900 kΩ, and 1100 kΩ define our upper and lower bounds.

```python
# define constants

mu = 979.8    # mean = 978.8 kΩ
sigma = 73.1  # standard deviation = 73.1 kΩ
x1 = 900      # lower bound = 900 kΩ
x2 = 1100     # upper bound = 1100 kΩ

```

Next, we calculate the Z-transform of the upper and lower bounds using the mean and standard deviation. Then we use the ```erf()``` function to calculate the probability from Z = 0 to the Z-transform derived from the upper and lower bounds.

```python
# calculate probability

# probability from Z=0 to lower bound
double_prob = erf( (x1-mu) / (sigma*sqrt(2)) )
p_lower = double_prob/2
print(f'\n Lower Bound: {round(p_lower,4)}')

# probability from Z=0 to upper bound
double_prob = erf( (x2-mu) / (sigma*sqrt(2)) )
p_upper = double_prob/2
print(f'\n Upper Bound: {round(p_upper,4)}')

```

From the Z-transform of the upper and lower limits, we calculated two probabilities: ```p_lower``` and ```p_upper```. We can use these probabilities to calculate the likelihood a resistor randomly pulled off the line is within tolerance (inside the range of 900 kΩ to 1100 kΩ) or out of tolerance (outside the range of 900 kΩ to 1100 kΩ).

```python
# print the results

Pin = (p_upper) - (p_lower)
print('\n')
print(f'mean = {mu}    std dev = {sigma} \n')
print(f'Calculating the probability of occurring between {x1} <--> {x2} \n')
print(f'inside interval Pin = {round(Pin*100,1)}%')
print(f'outside interval Pout = {round((1-Pin)*100,1)}% \n')
print('\n')

```

When the entire script is run, the output of our **_stats.py_** script is:

```text
 Lower Bound: -0.3625

 Upper Bound: 0.4499


mean = 979.8    std dev = 73.1 

Calculating the probability of occurring between 900 <--> 1100 

inside interval Pin = 81.2%
outside interval Pout = 18.8% 

```

<br>

So back to the original question: 

<br>

_Determine the probability that a resistor coming off the production line will be within spec._

<br>

The answer is: the probability a resistor coming off the production line is within spec is the probability of the inside interval, **81.2%**

<br>

In the next post, we will use Python and **Matplotlib** to build a curve that describes the problem.
