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

Next, we'll build a plot that shows an animated line.

## Create an animated line plot

The last plot we built was a simple line plot. We are going to build on that simple static line plot and trun it into an animated line plot. To create the data for the plot we are going to use Python's ```random.randint()``` function. The ```randint()``` function accepts a lower limit and upper limit, for our temperature data, we will set a lover limit of 25 degrees and an uper limit of 99 degrees. The script to build the animated line plot starts almost the same way as our simple line plot, the difference is that we need to import Matplotlib's ```FuncAnimation``` class from the `````matplotlib.animation``` library. The next part of the script is the same.

```python
# animated_line_plot.py

from random import randint

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# create empty lists for the x and y data
x = []
y = []

# create the figure and axes objects
fig, ax = plt.subplots()
```

In our first static line plot, we started the plot at this point, but for the animated line plot, we need to build the plot in a function. At a minimum the fuction needs to accept one argument that corresponds to frames in the animation. This argument can be given a simple parameter like ```i```. That parameter does not have to be used in the function that draws the plot. It just has to be included in the function definition.

```python
# function that draws each frame of the animation
def animate(i):
    pt = randint(1,9) # grab a random integer to be the next y-value in the animation
    x.append(i)
    y.append(pt)

    ax.clear()
    ax.plot(x, y)
    ax.set_xlim([0,20])
    ax.set_ylim([0,10])
```

Now we need to call the animation. Matplotlib's FuncAnimation class can accept a number of arguments. At a minum, we need to pass in the figure object ```fig```, our animation function that draws the plot ```animate```. We'll also add a ```frames=``` keyword aregument that describes how many times the plot is re-drawn or how many times the animation function is called. ```interval=500``` specifies the time between frames in miliseconds. ```interval=500``` means 500 milliseconds between each frame which is half a second. ```repeat=False``` means that once the live plot is drawn, it will not repeat.

```python
# run the animation
ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=False)

plt.show()
```

You can run the animated plot from the command line.

```text
(live_plot)> animated_line_plot.py
```

An example of the plot produced is below.

![still of animated line plot]({static}/posts/matplotlib_animations/images/animated_line_plot.gif)

Next, we'll build a live auto-updating plot based on user input.

## Build a live plot based on user input

Create a new Python file called ```live_plot_user_input.py```

![still of piston motion]({static}/posts/matplotlib_animations/images/create_live_plot_user_input_dot_py.PNG)

In the file ```live_plot_user_input.py```, add the same imports we used in our first plot. Then add an import line to bring in Matplotlib's ```FuncAnimation``` class from the ```matplotlib.animation``` library. We'll use the ```FuncAnimation``` class to build our live auto-updating plot.

```python
# live_plot_user_input.py

# import necessary packages
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
```

Next we'll pre-populate a list called ```data``` with a couple of data points. This will gives our plot a couple of points to start off with. When our script runs, we'll include functionality to add more points.

```python
# initial data
data = [3, 6, 2, 1, 8]

# create figure and axes objects
fig, ax = plt.subplots()
```

Now we'll build an ```animate()``` function that will read in values from a text file and plot them with Matplotlib. Note the line ```plt.cla()```. This line of code clears the current axis so that the plot can be redrawn. The line ```plt.plot(data[-5:])``` pulls the last 5 data points out of the list ```data``` and plots them.

```python
# animation function
def animate(i):
    with open('data.txt','r') as f:
        for line in f:
            data.append(int(line.strip()))
    ax.clear()
    ax.plot(data[-5:]) # plot the last 5 data points
```

The last section of code in the ```live_plot_user_input.py``` script will call the ```FuncAnimation``` class. When we intantiate an instance of this class, we pass in a couple arguments:

 * ```fig``` - the figure object we created with the ```plt.subplots()``` method
 * ```animate``` - this is the function we wrote above that pulls lines out of a ```data.txt``` file and plots 5 points at a time.
 * ```interval=1000``` - this is the time interval in milliseconds (1000 miliseconds = 1 second) for our plot to update.

```python
# call the animation
ani = FuncAnimation(fig, animate, interval=1000)

# show the plot
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

![still of plot]({static}/posts/matplotlib_animations/images/run_live_plot_user_input_py.PNG)

Now add a number to ```data.txt``` at the bottom of the file on it's own line. Save ```data.txt```. The plot should update with a new data point. I added the number ```16``` to ```data.txt``` and saw the line on the plot go upwards. Add another number at the end of ```data.txt``` (I added ```18``` on the last line). Save ```data.txt``` and watch the plot update.

![animated gif]({static}/posts/matplotlib_animations/images/user_input_live_plot.gif)

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

url = "https://api.thingspeak.com/channels/948462/fields/2.json?results=1"

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
    ax.set_ylim([0,10])
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Wind Speed from ThingSpeak Channel 948462')
    plt.ylabel('Wind Speed (mph)')

# Set up plot to call animate() function every 1000 milliseconds
ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval=1000)
plt.show()
```

Next, we will build a live-plot from sensor data

## Build a live plot using data from a sensor

The final live auto-updating plot we are going to build will show sensor data streaming in from an Arduino. Since this post is about live plots, I will not go into great detail about how to connect the sensor to the Arduino or how the Arduino works. Very briefly, the sensor we are using in this example is a potentiometer. A potentiometer is a dial that you can turn back and forth. When the dial of a potentiometer is turned, the resistance of the poteniomter changes. 

### Hardware Hookup

We can hook up a potentiometer up to an Arduino based on the diagram below.

![still of piston motion]({static}/posts/matplotlib_animations/images/redboard_pot_led_fritzing.png)

### Arduino Code

After the little blue potentiometer is hooked up, Upload the following code on the Arduino. 

```text
// potentiometer.ino
// reads a potentiometer and sends value over serial

int sensorPin = A0; // The potentiometer is connected to analog pin 0
int ledPin = 13; // The LED is connected to digital pin 13
int sensorValue; // an integer variable to store the potentiometer reading

void setup() // this function runs once when the sketch starts
{
// make the LED pin (pin 13) an output pin
pinMode(ledPin, OUTPUT);
// initialize serial communication at 9600 baud
Serial.begin(9600);
}

void loop() // this function runs repeatedly after setup() finishes
{
sensorValue = analogRead(sensorPin); // read the voltage at pin A0
Serial.println(sensorValue); // Output voltage value to Serial Monitor
if (sensorValue < 500) { // if sensor output is less than 500,
    digitalWrite(ledPin, LOW); } // Turn the LED off
else {                   // if sensor output is greater than 500
    digitalWrite(ledPin, HIGH); } // Keep the LED on
delay(100); // Pause 100 milliseconds before next reading
}
```

### Python Code

We need to install the PySerial library before we can use PySerial to read the sensor data the Arduino spits out over the serial line. Install PySerial with the command below. Make sure you have activated the ```(live_plot)``` virtual environment when the install commmand is entered.

```text
(live_plot)> conda install -y pyserial
```

or

```
(venv)$ pip install pyserial

```

At the top of the Python script, we need to import the necessary libraries:

```python
import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```

Next, we need to build an ```animate()``` function like we did above when we build our live plot from a data file and our live plot from a web api. 

```python
# animation function
def animate(i, data_lst, ser):  # ser is the serial object
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    flt = float(string)
    data_lst.append(flt)

    # Add x and y to lists
    data_lst.append(flt)
    # Limit the data list to 100 values
    data_lst = data_lst[-100:]
    # clear the last frame and draw the next frame
    ax.clear()
    ax.plot(data_lst)
    # Format plot
    ax.set_ylim([0,1050])
    ax.set_title('Potentiometer Reading Live Plot')
    ax.set_ylabel('Potentiometer Reading')
```

Now we need to create our ```data_lst``` list as well as intantiate the serial object.

```python
# create empty list to store data
# create figure and axes objects
data_lst = []
fig, ax = plt.subplots()

# set up the serial line
ser = serial.Serial('COM7', 9600) # change COM# if necessary
time.sleep(2)
print(ser.name)

```

Then we need to call our animation using Matplotlib's FuncAnimate class. After the animation is finished, we should close the serial line


```python
# run the animation and show the figure
ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(data_lst, ser), interval=200)
plt.show()

# after the window is closed, close the serial line
ser.close()
print("Serial line closed")
```

The entire Python script is below:

```python
# live_sensor.py

import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# animation function
def animate(i, data_lst, ser):  # ser is the serial object
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    flt = float(string)
    data_lst.append(flt)

    # Add x and y to lists
    data_lst.append(flt)
    # Limit the data list to 100 values
    data_lst = data_lst[-100:]
    # clear the last frame and draw the next frame
    ax.clear()
    ax.plot(data_lst)
    # Format plot
    ax.set_ylim([0,1050])
    ax.set_title('Potentiometer Reading Live Plot')
    ax.set_ylabel('Potentiometer Reading')

# create empty list to store data
# create figure and axes objects
data_lst = []
fig, ax = plt.subplots()

# set up the serial line
ser = serial.Serial('COM7', 9600) # change COM# if necessary
time.sleep(2)
print(ser.name)

# run the animation and show the figure
ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(data_lst, ser), interval=200)
plt.show()

# after the window is closed, close the serial line
ser.close()
print("Serial line closed")

```

## Summary

In this post, we...
