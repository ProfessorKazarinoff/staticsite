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

## Pre-requisits

To follow along with this tutorial, a couple pre-requisits need to be in place:

 * Python needs to be installed on your computer. I recommend installing the Anaconda Distribution of Python
 * You are running a version of Python 3.6 or above. Python version 3.7 or 3.8 are more up to date.
 * You know how to open the Anaconda Prompt on Windows10 or know how to open a terminal on MacOS or Linux
 * You have a general idea of what Python packages are and have installed a Python package before using **conda** or **pip**.
 * You know how to create a text file in an editor or an IDE such as Visual Studio Code, PyCharm, Sublime Text, vim, emacs, etc.
 * You know how to run a Python program using a terminal prompt, like the Anaconda Prompt or know how to run a Python program from your IDE.
 * You have general understanding of how files are organized on your computer into directories and sub-directories.
 * You have some familiarity with navigating through directories and files using a terminal using commands like ```cd```, ```cd ..```, ```dir``` or ```ls```, and ```mdkir```.

Now that those pre-requisites are out of the way, let's start coding! 

## Set up a Python virtual environment

To start the coding process, we will set up a virtual environment in Python.

Real Python has a good [introduction to virtual environments](https://realpython.com/blog/python/python-virtual-environments-a-primer/) and why to use them.

I recommend undergraduate engineers use the [Anaconda distribution of Python](https://anaconda.com/distribution) which comes with the **Anaconda Prompt**. You can create a new virtual environment by opening the **Anaconda Prompt** and typing:

Using the Anaconda Prompt:

```text
> mkdir live_plot
> cd live_plot
> conda create -y -n live_plot python=3.7
```

![still of piston motion]({static}/posts/matplotlib_animations/images/create_env_conda.PNG) 

Alternatively, on MacOS or Linux, a virtual environment can be set up with a terminal prompt and **pip**.

Using a terminal on MacOS or Linux:

```text
$ mkdir live_plot
$ cd live_plot
$ python3 -m venv venv
```

## Install Python packages

Now that we have a new clean virtual environment with Python 3 installed, we need to install the necessary packages that we'll use to create our plots.

Using the Anaconda Prompt, activate the ```live_plot``` virtual environment and use **conda** to install the following Python packages. Ensure the virtual environment you created above is activate when the packages are installed.

```text
> conda activate live_plot
(live_plot) > conda install -y numpy matplotlib requests
```

![still of piston motion]({static}/posts/matplotlib_animations/images/conda_install_numpy_matplotlib.PNG) 

Alternatively, if you are using MacOS or Linux, the packages can be installed with a terminal **pip**:

```text
$ source venv/bin/activate
(venv) $ pip install numpy
(venv) $ pip install matplotlib
(venv) $ pip install requests
```

## Create a static line plot

Before we create a live auto-updating plot, let's first create a static line plot. Our live plots will look a lot like this first static plot. Building a simpler plot first gives us some practice and a structure to build upon when we create the more complex live plots.

Open a text editor or IDE (I like to use [VS Code](https://code.visualstudio.com/)) and create a new Python file called ```static_plot.py```

![still of piston motion]({static}/posts/matplotlib_animations/images/create_static_plot_dot_py.PNG) 

### Import packages

Let's start our ```static_plot.py``` script by importing the packages we'll use later in the script. NumPy is imported as the common alias ```np```. We will also import Matplotlib's ```pyplot``` module using the standard ```plt``` alias.

```python
# static_plot.py

# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
```

We need some data to plot. For this static plot, we'll plot the temperature in Portland, OR in degree ferenheit over seven day. We'll save the temperature values in a Python list.

```python
# data
temps = [60, 59, 49, 51, 49, 52, 53]
```

Next, we'll create a figure object ```fig``` and an axis object ```ax``` using Matplotlib's ```plt.subplots()``` method. 

```python
# create the figure and axis objects
fig, ax = plt.subplots()
```

Now we can plot the temperature data on the axis object ```ax``` and customize the plot. Let's include plot title, axis labels.

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

That's it for this first script. Pretty simple right?

Run the ```static_plot.py``` script using the Anaconda Prompt of a terminal. Ensure the virtual environment ```(live_plot)``` is active when the script is run.

```text
(live_plot)> python static_plot.py
```
![still of piston motion]({static}/posts/matplotlib_animations/images/run_static_plot_dot_py.PNG) 

The plot should look something like image below:

![still of piston motion]({static}/posts/matplotlib_animations/images/static_plot.png) 

The complete script is below:

```python
# static_plot.py

# import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# data
temps = [60, 59, 49, 51, 49, 52, 53]

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

Next, we'll build a live plot based on user input.

## Build a live plot based on user input

Create a new Python file called ```live_plot_user_input.py```

![still of piston motion]({static}/posts/matplotlib_animations/images/create_live_plot_user_input_dot_py.PNG)

In the file ```live_plot_user_input.py```, add the same imports we used in our first plot. Then add an import line to bring in Matplotlib's ```FuncAnimation``` class from the ```matplotlib.animation``` library. We'll use the ```FuncAnimation``` class to build our live auto-updating plot.

```python
# live_plot_user_input.py

# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
```

Next we'll pre-populate a list called ```data``` with a couple of data points. This will gives our plot a couple of points to start off with. When our script runs, we'll include functionality to add more points.

```python
# initial data
data = [3, 6, 2, 1, 8]
```

Now we'll build an ```animate()``` function that will read in values from a text file and plot them with Matplotlib. Note the line ```plt.cla()```. This line of code clears the current axis so that the plot can be redrawn. The line ```plt.plot(data[-5:])``` pulls the last 5 data points out of the list ```data``` and plots them.

```python
# animation function
def animate(i):
    with open('data.txt','r') as f:
        for line in f:
            data.append(int(line.strip()))
    plt.cla()

    plt.plot(data[-5:])
```

The last section of code in the ```live_plot_user_input.py``` script will call the ```FuncAnimation``` class. When we intantiate an instance of this class, we pass in a couple arguments:

 * ```plt.gcf()``` - grabs the current Matplotlib figure. This is the figure we animate
 * ```animate``` - this is the function we wrote above that pulls lines out of a ```data.txt``` file and plots 5 points at a time.
 * ```interval=1000``` - this is the time interval in milliseconds (1000 miliseconds = 1 second) for our plot to update.

 ```python
# call the animation
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

# show the plot
plt.tight_layout
plt.show()
 ```

Before you run the script, create a new file in the ```live_plot``` directory along side our ```live_plot_user_input.py``` script called ```data.txt```. Inside the file add a couple numbers, each number on it's own line.

```text
5
9
3
10
12
```

Save ```data.txt``` and leave the file open. This is the file that we will add number to and watch our live plot update.

Save ```live_plot_user_input.py``` and run it. You should see a plot pop up. 

![still of piston motion]({static}/posts/matplotlib_animations/images/run_live_plot_user_input_py.PNG)

Now add a number to ```data.txt``` at the bottom of the file on it's own line. Save ```data.txt```. The plot should update with a new data point. I added the number ```16``` to ```data.txt``` and saw the line on the plot go upwards. Add another number at the end of ```data.txt``` (I added ```18``` on the last line). Save ```data.txt``` and watch the plot update.

![still of piston motion]({static}/posts/matplotlib_animations/images/user_input_live_plot.PNG)

Great! We built a live updating plot based on user input. Next, let's build a live auto-updating plot using data pulled from the web.

## Build a live plot using data from the web

The third plot we are going to build is a plot that pulls data from the web.

```python
# plot_thingspeak_realtime.py

"""
A Python script that plots live data from Thingspeak.com using Matplotlib
inspiration from:
https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time
"""
import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation

url = "https://api.thingspeak.com/channels/9/fields/1.json?results=1"

# function to pull out a float from the requests response object
def pull_float(response, field_num='1'):
    jsonr = response.json()
    field_str = 'field'+field_num
    strr = jsonr['feeds'][0][field_str]
    fltr = round(float(strr),2)
    return fltr

# Create figure for plotting
fig, ax = plt.subplots()
xs = []
ys = []

def animate(i, xs:list, ys:list):
    # grab the data from thingspeak.com
    response = requests.get(url)
    flt = pull_float(response,'1')
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(flt)
    # Limit x and y lists to 10 items
    xs = xs[-10:]
    ys = ys[-10:]
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    # Format plot
    ax.set_ylim([175,225])
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Light from ThingSpeak Channel 9')
    plt.ylabel('Light Reading')

# Set up plot to call animate() function every 1000 milliseconds
ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval=1000)
plt.show()
```

## Build a live plot using data from a sensor

## Summary
