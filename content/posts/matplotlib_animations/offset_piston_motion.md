Title: Offset Piston Motion with Python and matplotlib
Date: 2019-12-17 20:40
Modified: 2017-12-17 20:40
Status: Draft
Category: matplotlib
Tags: python, matplotlib, animation, engineering
Slug: offset-piston-motion
Authors: Peter D. Kazarinoff

Offset piston motion is one of the classic types of engineering dynamics motion that belong to a category of 4-bar motion. Piston motion is the type of motion that the piston in a cylinder of a car engine goes through as the crankshaft rotates. Offset pistion motion has the same type of motion, but the center line of the piston is not inline with the center of the crankshaft. This type of offset piston/crankshaft geometry is sometimes used in automobile engines. For example some Toyota engines have an offset piston geometry.

[TOC]

## Set up a python virtual environment

To start this process, we will set up a Python virtual environment. 

Real Python has a good [introduciton to virtual environments](https://realpython.com/blog/python/python-virtual-environments-a-primer/) and why to use them.

Using the terminal:

```text
$ mkdir piston_motion
$ cd piston_motion
$ python3 -m venv venv
```

## Install Python packages

Now that we have the a new clean virtual environment with Python 3 installed, we need to install the necessary packages
```none
$ source venv/bin/activate
(venv) $ pip install numpy
(venv) $ pip install matplotlib
(venv) $ pip freeze
cycler==0.10.0
matplotlib==2.0.2
numpy==1.13.1
pyparsing==2.2.0
python-dateutil==2.6.1
pytz==2017.2
six==1.10.0
```

## Start the script with imports

Open a text editor (like VS Code or PyCharm) and start a new python file called ```offset_piston_motion.py```
We will start our script by importing the necessary modules

```python
#import necessary packages
import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```

## Initial Paramters

To model offset piston motion we need to have two moving parts: the crankshaft and the connecting rod.

The crankshaft rotates around a central axis with a constant radius. We will model this with a line of constant length, one end fixed at the origin and the other rotating in a circle like the hand on a clock. To model this crankshaft line, we just need two points, the origin at x=0 and y=0  and the end of the line at the point ```x1``` and ```x2```. We also need to have a crank radius and a connecting rode length. We will define these constants at the top of our code. So that the animation does not run around indefininelty we will set a fixed number of rotations.  The rotation increment defines how fine the 'ticks' are as our crankshaft arm rotates. 0.1 will work to make the animation smooth enough.

For offset piston motion, one last parameter we need is the offset distance. This is the distance between the center of the crankshaft and the line that goes through the end of the connecting rod. In regular piston motion, this length is zero. In offset pistion motion this non-negative

```python
#input parameters
r = 1.0  # crank radius
l = 4.0  # connecting rod length
d = 0.5; # offset distance
rot_num = 6 # number of crank rotations
increment = 0.1 # angle incremement
```

## Create arrays of angles and points

Next, we will create a couple of arrays of angles and points

```python
#create the angle array, where the last angle is the number of rotations*2*pi
angle_minus_last = np.arange(0,rot_num*2*pi,increment)
angles = np.append(angle_minus_last, rot_num*2*pi)


X1=np.zeros(len(angles)) # array of crank x-positions: Point 1
Y1=np.zeros(len(angles)) # array of crank y-positions: Point 1
X2=np.zeros(len(angles)) # array of rod x-positions: Point 2
Y2=np.zeros(len(angles)) # array of rod y-positions: Point 2
```

## Loop through angles

After the ```angles``` array is defined, we can loop through the angles and define points for the end of the crankshaft and the end of the connecting rod. To keep track of the number of times though the loop, we'll use Python's ```enumerate()``` function.

```python
#find the crank and connecting rod positions for each angle
for index,theta in enumerate(angles, start=0):
    x1 = r*cos(theta) # x-cooridnate of the crank: Point 1
    y1 = r*sin(theta) # y-cooridnate of the crank: Point 1
    x2 = d # x-coordinate of the rod: Point 2
    # y-coordinate of the rod: Point 2
    y2 = r*sin(theta) + sqrt(  l**2 - (r*cos(theta)-d)**2  )
    X1[index]=x1 #grab the crankshaft x-position
    Y1[index]=y1 #grab the crankshaft y-position
    X2[index]=x2 #grab the connecting rod x-position
    Y2[index]=y2 #grab the connecting rod y-position
```

## Create the Matplotlib figure and plot

Now that the point arrays are all defined, we can set up the Matplotlib figure window and add a subplot to it.

```python
# set up the figure and subplot
fig = plt.figure()
fig.canvas.set_window_title('Matplotlib Animation')
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-2,6))
ax.grid()
ax.set_title('Offset Piston Motion Animation')
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
line, = ax.plot([], [], 'o-', lw=5, color='#de2d26')
```

## Initialization function

An initialization function is need to make the animation work. 

```python
# initialization function
def init():
    line.set_data([], [])
    eturn line,
```

## Animation function

Defining the animation function is next.

```python
# animation function
def animate(i):
    x_points = [0, X1[i], X2[i]]
    y_points = [0, Y1[i], Y2[i]]
    line.set_data(x_points, y_points)
    return line,
```

## Call the animation and show the plot

The script is almost finished. All have left to do is call our animation and show the plot.

```python

# call the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(X1), interval=40, blit=True, repeat=False)
## to save animation, uncomment the line below:
## ani.save('offset_piston_motion_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#show the animation
plt.show()
```

## Run the script

The completed ```offset_piston_motion.py``` script can be run from the command line.

```
$ python offset_piston_motion.py
```

## The resulting animation

A video of the resulting animation is shown below:

{% youtube 4KbbOZh7Zzk %}

## The complete code

The complete ```offset_piston_motion.py``` script is shown below. You can also find the code on GitHub [here](https://github.com/ProfessorKazarinoff/offset_piston_motion)

```python
"""
Offset Piston Motion Animation using Matplotlib.
Animation designed to run on Raspberry Pi 3
Author: Peter D. Kazarinoff, 2019
"""

#import necessary packages
import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#input parameters
r = 1.0  # crank radius
l = 4.0  # connecting rod length
d = 0.5; # offset distance
rot_num = 6 # number of crank rotations
increment = 0.1 # angle incremement

#create the angle array, where the last angle is the number of rotations*2*pi
angle_minus_last = np.arange(0,rot_num*2*pi,increment)
angles = np.append(angle_minus_last, rot_num*2*pi)


X1=np.zeros(len(angles)) # array of crank x-positions: Point 1
Y1=np.zeros(len(angles)) # array of crank y-positions: Point 1
X2=np.zeros(len(angles)) # array of rod x-positions: Point 2
Y2=np.zeros(len(angles)) # array of rod y-positions: Point 2

#find the crank and connecting rod positions for each angle
for index,theta in enumerate(angles, start=0):
    x1 = r*cos(theta) # x-cooridnate of the crank: Point 1
    y1 = r*sin(theta) # y-cooridnate of the crank: Point 1
    x2 = d # x-coordinate of the rod: Point 2
    # y-coordinate of the rod: Point 2
    y2 = r*sin(theta) + sqrt(  l**2 - (r*cos(theta)-d)**2  )
    X1[index]=x1 #grab the crankshaft x-position
    Y1[index]=y1 #grab the crankshaft y-position
    X2[index]=x2 #grab the connecting rod x-position
    Y2[index]=y2 #grab the connecting rod y-position

# set up the figure and subplot
fig = plt.figure()
fig.canvas.set_window_title('Matplotlib Animation')
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-2,6))
ax.grid()
ax.set_title('Offset Piston Motion Animation')
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
line, = ax.plot([], [], 'o-', lw=5, color='#de2d26')


# initialization function
def init():
    line.set_data([], [])
    eturn line,

# animation function
def animate(i):
    x_points = [0, X1[i], X2[i]]
    y_points = [0, Y1[i], Y2[i]]
    line.set_data(x_points, y_points)
    return line,

# call the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(X1), interval=40, blit=True, repeat=False)
## to save animation, uncomment the line below:
## ani.save('offset_piston_motion_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#show the animation
plt.show()
```