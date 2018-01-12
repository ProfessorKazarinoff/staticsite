Title: Python Data Types
Date: 2018-01-11 10:15
Modified: 2018-01-11 10:15
Status: draft
Category: python
Tags: python, data
Slug: python-data-types
Authors: Peter D. Kazarinoff
JavaScripts: table.js
Stylesheets: table.css
Summary: Python has many useful built in data types. Python variables can store different types of data and can be created dynamically, without first defining a data type. It's useful for engineers to understand a couple of Python's core data types in order to write well constructed code. Below we will discuss a few different data types.

Python has many useful built in data types. Python variables can store different types of data and can be created dynamically, without first defining a data type. It's useful for engineers to understand a couple of Python's core data types in order to write well constructed code. Below we will discuss a few different data types.

#### Integers

Integers are one of the python data types. An integer is a whole number, negative, positive or zero. In Python integer variables can be defined by simply assigning a whole number to a variable name. We can determine data type of a variable using the ```type()``` function.

```python
>>> a = 5
>>> type(a)
<class 'int'>
>>> b = -2
>>> type(b)
<class 'int'>
>>> z = 0
>>> type(z)
<class 'int'>
```

#### Floating Point Numbers

Floating point numbers or _floats_ are another Python data type. Floats are decimals, positive, negative and zero. Floats can also be numbers in scientific notation which contain exponents. In Python, a float can be defined using a decimal point ```.``` when a variable is assigned.

```python
>>> c = 6.2
>>> type(c)
<class 'float'>
>>> d = -0.03
>>> type(d)
<class 'float'>
>>> e = 6.02e23
>>> e
6.02e+23
>>> type(e)
<class 'float'>
```

To make sure a variable is a float instead of an integer even if it is a whole number, a trailing decimal point used. Note the difference when a decimal point is used.

```python
>>> g = 5     # no decimal point
>>> type(g)
<class 'int'>
>>> g = 5.    # decimal point
>>> type(g)
<class 'float'>
```

#### Boolean

A boolean value is either True or False. In Python, boolean variables are defined by the True and False key words. Note that True and False must have an upper case first letter.

```python
a = True
type(a)
<class 'bool'>
b = False
type(b)
<class 'bool'>
c = true
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'true' is not defined
d = false
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'false' is not defined
```

#### String

Strings are sequences of letters, numbers, spaces and symbols. In Python, strings can be almost any length. String variables are assigned using quotation marks.

```python
str = 'z'
type(str)
<class 'str'>
str = 'Engineers'
type(str)
<class 'str'>
```

A numbers and decimals can be defined as strings too. If a decimal number is defined using quotes, it will be saved as a string rather than a float. This is true of whole numbers as well.

```python
num = '5.2'
type(num)
<class 'str'>
num = '2'
type(num)
<class 'str'>
```

### Converting between different data types

A whole number can be either an integer, float or string depending on how it is assigned. Python has built in functions to convert from one to another. The ```int()``` ```float()``` and ```str()``` methods will convert one Python data type to another. 

```python
int_num = 5
type(int_num)
<class 'int'>
float_num = float(int_num)
type(float_num)
<class 'float'>
str_num = str(int_num)
type(str_num)
<class 'str'>
str_num
'5'
```

### Summary

|Data Type| Python Class | Description |Examples|
|---|---|---|---|
| integer | int | whole numbers: negative positive and zero | 5 -2 0 |
| floating point number	| float | decimal number: negative positive and zero. Can contain an exponent | 2.3 -0.05 4.5e8 | 
| boolean	| bool	| True or False | True False |
| string	| str	| sequence of letters, numbers, spaces and symbols | Peter Engineering! 5 |
