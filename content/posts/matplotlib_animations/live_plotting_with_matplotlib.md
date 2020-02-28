Title: Plotting Live Data with Matplotlib and Python
Date: 2020-02-27 08:40
Modified: 2020-02-27 08:40
Status: draft
Category: Plotting
Tags: python, matplotlib, animation, arduino, api
Slug: live-plotting-with-matplotlib
Authors: Peter D. Kazarinoff

![still of piston motion]({static}/posts/matplotlib_animations/images/piston_motion_still.png) 

Matplotlib can be used to create static 2D plots, but it Matplotlib can also be used to create dynamic auto-updating live plots. In this post, you see how to create a live running plot using Matplotlib and Python.

[TOC]

## Set up a Python virtual environment

To start this process, we will set up a virtual environment in Python.

Real Python has a good [introduction to virtual environments](https://realpython.com/blog/python/python-virtual-environments-a-primer/) and why to use them.

I recommend undergraduate engineers use the [Anaconda distribution of Python](https://anaconda.com/distribution) which comes with the **Anaconda Prompt**. You can create a new virtual environment by opening the **Anaconda Prompt** and typing:

Using the Anaconda Prompt:

```text
> mkdir live_plot
> cd live_plot
> conda create -y -n live_plot python=3.7
```

Alternatively, on MacOS or Linux, a virtual environment can be set up with a terminal prompt and **pip**.

Using a terminal on MacOS or Linux:

```text
$ mkdir live_plot
$ cd live_plot
$ python3 -m venv venv
```

## Install Python packages

Now that we have a new clean virtual environment with Python 3 installed, we need to install the necessary packages:

Using the Anaconda Prompt, activate the ```live_plot``` virtual environment and use **conda** to install the following Python packages. Ensure the virtual environment you created above is activate when the packages are installed.

```text
> conda activate live_plot
(live_plot) > conda install numpy
(live_plot) > conda install matplotlib
```

Alternatively, if you are using MacOS or Linux, the packages can be installed with a terminal **pip**:

```text
$ source venv/bin/activate
(venv) $ pip install numpy
(venv) $ pip install matplotlib
```

## Create a static line plot

Before we create a live auto-updating plot, let's first create a static line plot. Our live plots will look a lot like this first static plot. Building a simpler plot first gives us some practice and a structure to build upon when we create the more complex live plots.

Open a text editor (I like to use [VS Code](https://code.visualstudio.com/)) and create a new Python file called ```static_plot.py```

### Import packages

We will start our ```static_plot.py``` script by importing the necessary modules. NumPy is imported as the common alias ```np```. We will also import Matplotlib's ```pyplot``` module using the standar ```plt``` alias

```python
#import necessary packages
import numpy as np
import matplotlib.pyplot as plt
```

We need some data to plot. For this static plot, we'll plot the temperature in Portland, OR from the last week. We can save the temperature values in a Python list.

```python
# create data
temps = [60, 59, 49, 51, 49, 52,53,54]
```

Next, we'll create a figure object ```fig``` and an axis object ```ax``` using Matplotlib's ```plt.subplots()``` method. 

```python
# create the figure and axis objects
fig, ax = plt.subplots()
```

Now we plot the data on the axis object ```ax``` and customize the plot. We'll include a title,  axis labels and a legend.

```python
# plot the data and customize
ax.plot(temps)
ax.set_xlabel('Day Number')
ax.set_ylabel('Temperature (*F)')
ax.set_title('Temperature in Portland, OR over 7 days')
```

Finally we can show and save the plot. Make sure that the ```fig.savefig()``` line is before the ```plt.show()``` line. 

```python
# save and show the plot
fig.savefig('static_plot.png')
plt.show()
```

Run the ```static_plot.py``` script using the Anaconda Prompt of a terminal. Ensure the virtual environment with Matplotlib installed into is active when the script is run.

```
(live_plot)> python static_plot.py
```

The plot should look something like below:

![still of piston motion]({static}/posts/matplotlib_animations/images/static_plot.png) 

The complete script is below:

```python
#import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# data
temps = [60, 59, 49, 51, 49, 52,53,54]

# create the figure and axis objects
fig, ax = plt.subplots()

# plot the data and customize
ax.plot(temps)
ax.set_xlabel('Day Number')
ax.set_ylabel('Temperature (*F)')
ax.set_title('Temperature in Portland, OR over 7 days')

# save and show the plot
fig.savefig('static_plot.png')
plt.show()
```

## Build a live plot based on user input

## Build a live plot using data from the web

## Build a live plot using data from a sensor

## Summary
