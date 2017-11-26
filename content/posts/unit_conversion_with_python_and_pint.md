Title: Using Python and Pint to do Unit Conversions
Date: 2017-09-27 12:03
Modified: 2017-09-27 12:03
Status: Draft
Category: Python
Tags: python, pint, unit conversion
Slug: python-and-pint-unit-conversion
Authors: Peter Kazarinoff
Series: Python and Pint
series_index:
Summary:

Units and unit conversions are **BIG** in engineering. Engineers solve the worlds problems in teams. Any problem that is solved has to have a context that it is solved in. How heavy can a rocket be and still make it off the ground, what thickness bodypannels should be used to keep occupants save during a crash. In engineering a number without a unit is like a fish without water. It just flops around hopelessly without context and is useless. 

How can we get help using unit? Programming is one way. We are going to use Python and Pint, a python package used for unit conversions to do a couple of sample unit conversions and some simple density problems. These could be problems on engineering homework problems sets. Below are is the first problem:


Convert the following measurements into the units provided

1. 13.2 in to cm
2. 1100 W to Btu / hr
3. 63.2 lb ft to N m
4. 1150 J s/m2 to kcal min/in2

First we should fire up a new virtual environment, let's call it ```units```

```
$ mkvirtualenv units
```

Next we need to activate our new ```units``` environment and install the pint package using pip. Pint is a python package used to work with units(like meter, gram, pound, inch, foot) and convert between different units (like converting 12 inches = 30.48 cm).

```
$ workon units
(units)$ pip install pint
(units)$ pip freeze
Pint==0.8.1
```

OK. Now on to our first problem. We can do these first four problems directly in the python interpreter. To open up the interpreter, just type ```python``` on the command line.

```
(units)$ python
Python 3.5.1 (default, Apr 18 2016, 03:49:24) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

First we need to import the UnitRegistry from pint and create a UnitRegistry object

```
>>> from pint import UnitRegistry
>>> ureg = UnitRegistry()
```

Now let's create our measurement value, 13.2 inches

```
>>> measurement = 13.2 * ureg.inch
>>> print(measurement)
13. 2 inch
>>>
```

Our ```measurement``` now has a couple defined attributes, ```magnitude``` , ```units``` , and ```dimensionality```

```
>>> >>> print(measurement.magnitude)
13.2
>>> print(measurement.units)
inch
>>> print(measurement.dimensionality)
[length]
```

There are two ways we can convert our measurement 13.2 inches into centimeters. One is by creating a new object ```measurement_in_cm``` using the ```.to()``` method on our ```measurement``` object.

```
>>> measurement_in_cm = measurement.to(ureg.cm)
>>> print(measurement_in_cm)
33.528 centimeter
>>> 
```

The other way is to convert the measurement in place using the ```.ito()``` method

```
>>> measurement.ito(ureg.cm)
>>> print(measurement)
33.528 centimeter
>>> 
```

OK, let's try a problem which is a little bit harder. This time we will convert between to units of power, watts and Btu / hr

```
>>> power = 1100 * ureg.W
>>> print(power)
1100 watt
>>> 
```

The units we are going to convert to are Btu / hr. Compound units in pint are done with simple multiplication ```*``` or division ```/``` symbols

```
>>> power_in_Btu_per_hour = power.to(ureg.Btu / ureg.hr)
>>> print(power_in_Btu_per_hour)
3753.355796440737 btu / hour
>>> print(power_in_Btu_per_hour.units)
btu / hour
```

Or run the method in place with:

```
>>> power.ito(ureg.Btu / ureg.hr)
>>> print(power)
3753.355796440737 btu / hour
>>> 
```

Our next problem is: 63.2 lb ft to N m. Note here that pounds(lb) is a unit of *force* that will be converted to Newtons (N) also a unit of *force*. We need to make sure that we tell pint that we want pounds as a unit of *force*, not a unit of *mass*.

```
>>> torque = 63.2 * ureg.lb * ureg.ft
>>> print(torque)
63.2 foot * pound
>>> print(torque.dimensionality)
[length] * [mass]
```

This shows that our ```torque``` is in units of *length* x *mass*, but we want lbs as a unit of *force*, not a unit of *mass*. To do this we need to use the pint attribute ```ureg.lbf```

```
>>> torque = 63.2 * ureg.lbf * ureg.ft
>>> print(torque)
63.2 foot * force_pound
>>> 
```

To convert our torque into Newtons x meters, we enter the following:

```
>>> torque_in_N_m = torque.to(ureg.N * ureg.m)
>>> print(torque_in_N_m)
85.68769433454449 meter * newton
>>> 
```

We can then check and make sure the dimensionality of both ```torque``` and ```torque_in_N_m``` are the same

```
>>> print(torque.dimensionality)
[length] ** 2 * [mass] / [time] ** 2
>>> print(torque_in_N_m.dimensionality)
[length] ** 2 * [mass] / [time] ** 2
>>> torque_in_N_m.dimensionality == torque.dimensionality
True
>>> 
```

Now on to the last one. It is a doozy. 

11150 J s/m2 to kcal min/in2


```
>>> value3 = 1150 * ureg.J * ureg.s / ureg.m**2
>>> print(value3)
1150.0 joule * second / meter ** 2
>>> print(value3.dimensionality)
[mass] / [time]
```

Let's try this this conversion one unit at a time. First let's go from Js/m2 to kcals/m2

``` 
value3.ito(ureg.kcal * ureg.s / ureg.m**2)>>> value3.ito(ureg.kcal * ureg.s / ureg.m**2)
>>> print(value3)
0.2748565965583174 kilocalorie * second / meter ** 2
>>>
```

Now we will convert from kcals/m2 to kcalmin/in2

```
>>> value3.ito(ureg.kcal * ureg.min / ureg.m**2)
>>> print(value3)
0.004580943275971957 kilocalorie * minute / meter ** 2
>>> 
```

And finally convert from kcalmin/m2 to kcalmin/in2

```
>>> value3.ito(ureg.kcal * ureg.min / ureg.inch**2)
>>> print(value3)
2.9554413639260674e-06 kilocalorie * minute / inch ** 2
>>> 
```

Great! Now you know how to use python and pint to do unit conversions. Next we will use python and pint to convert numbers into scientific notion and engineering notation.

