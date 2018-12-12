Title: Calculating the probability under a normal curve with Python
Date: 2017-10-10 09:01
Modified: 2017-10-10 09:01
Status: Draft
Category: statistics
Tags: python, engineering, statistics
Slug: probability-under-normal-curve-with-python
Authors: Peter D. Kazarinoff
Series: Calculating the probability under a normal curve
series_index: 1

Calculating the probability under a normal curve is useful for engineers. This type of calculation can be useful to predict the likely hood of a part coming of an assembly line being within a given specification when the statistical properties of all the parts that have come of the assembly line previously are known. 

In this post, we will calculate the probability under the normal curve to answer a question like the one below:

### GIVEN:
a facility that manufactures electrical resistors, a sample of 35 1-kΩ resistors are randomly pulled from the production line, and their resistances are measured and recorded. A mean resistance of 979.8 kΩ and a standard deviation of 73.10 kΩ represents the sample of resistors. The desired resistance tolerance for the resistors is ± 10%, meaning that the acceptable range of resistance is 900 Ω to 1100 Ω.

### FIND:
Assuming a normal distribution, determine the probability that a resistor coming off the production line will be within spec.

### SOLUTION:

The script we are going to build to solve the problem above needs to accomplish a couple of things:

1. Import the necessary functions. We need to use the ```erf()``` and ```sqrt()``` functions in the ```math``` module.
2. Define the constants for this problem. The mean, standard deviation, lower bound and upper bound will be defined.
3. Calculate the probability using the ```erf()``` function from the ```math()``` module.
4. Print the results to the Python interpreter

Let's take a look at a gaussian curve

![gaussian_curve]({filename}/images/gaussian_curve.png)

This shape of curve describes the spread of resistors coming off the production line. We need to find the area under the curve within our upper and lower bounds.

Open up a new Python script called **_stats.py_**. In the first line of code we import the ```erf``` and ```sqrt()``` functions from the ```math``` module. Because the ```math``` module is part of the standard library, it does not need to be installed using ```conda``` or ```pip```.

```python
# stats.py

from math import erf, sqrt
```

Now we need to define the constants

```python

# define constants

mu = 979.8    # mean = 978.8 kΩ
sigma = 73.1  # standard deviation = 73.1 kΩ
x1 = 900      # lower bound = 900 kΩ
x2 = 1100     # upper bound = 1100 kΩ

```

Next we calculate the probability using the ```erf()``` function


```python

# calculate probability

# Probability from 0 to lower bound
double_prob = erf( (x1-mu) / (sigma*sqrt(2)) )
p_lower = double_prob/2
print(f'\n Lower Bound: {round(p_lower,4)}')

# Probability from 0 to upper bound
double_prob = erf( (x2-mu) / (sigma*sqrt(2)) )
p_upper = double_prob/2
print(f'\n Upper Bound: {round(p_upper,4)}')

```

From the upper and lower limits, we calculated two probabilities: ```p_lower``` and ```p_upper```. We can use these probabilities to calculate the probability a resistor randomly pulled off the line is within tolerance (inside the range of 900 kΩ to 1100 kΩ) or out of tolerance (outside the range of 900 kΩ to 1100 kΩ).

```python

# print the results

Pin= (p_upper) - (p_lower)
print('\n')
print(f'mean = {mu}    std dev = {sigma} \n')
print(f'Calculating probability of occuring between {x1} <--> {x2} \n')
print(f'inside interval Pin = {round(Pin*100,1)}%')
print(f'outside interval Pout = {round((1-Pin)*100,1)}% \n')
print('\n')

```

When it is run, the output of our **_stats.py_** script is:

```
 Lower Bound: -0.3625

 Upper Bound: 0.4499


mean = 979.8    std dev = 73.1 

Calculating probability of occuring between 900 <--> 1100 

inside interval Pin = 81.2%
outside interval Pout = 18.8% 


```

<br>

So back to our original question: 

<br>

_Determine the probability that a resistor coming off the production line will be within spec._
<br>
This is the probability of a resistor being inside the interval, **81.25 %**

<br>
In the next post, we will use Python and **matplotlib** to build a curve that describes this problem. 