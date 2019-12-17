Title: Piston Motion with Python and Matplotlib
Date: 2019-12-17 20:40
Modified: 2019-12-17 20:40
Status: Draft
Category: Python
Tags: python, matplotlib, animation, dynamics
Slug: piston-motion
Authors: Peter D. Kazarinoff
Summary: An animation of piston motion created with Python and Matplotlib

Piston motion is one of the classic dynamic types of motion that belong to a category of 4-bar motion. Piston motion is the type of motion that the piston in a cylinder of a car engine goes through as the crankshaft rotates. 

## Set up a python virtual environment

To start this process, we will set up a virtual environment in Python.

Real Python has a good [introduction to virtual environments](https://realpython.com/blog/python/python-virtual-environments-a-primer/) and why to use them.

I recommend undergraduate engineers use the Anaconda distribution of Python which comes with the **Anaconda Prompt**. A new virtual environment can be set up by opening the **Anaconda Prompt** and typing:

Using the Anaconda Prompt:

```text
> mkdir piston_motion
> cd piston_motion
> conda create -n piston_motion python=3.7
```

Alternatively, a virtual environment can be set up with a terminal prompt and **pip**

Using a terminal on MacOS or Linux:

```text
$ mkdir piston_motion
$ cd piston_motion
$ python3 -m venv venv
```

Now that we have a new clean virtual environment with Python 3 installed, we need to install the necessary packages:

Using the Anaconda Prompt, activate the ```piston_motion``` virtual environment and use conda to install the Python Packages:

```text
> conda activate piston_motion
(piston_motion) > conda install numpy
(piston_motion) > conda install matplotlib
```

Alternatively, if you are using MacOS or Linux, the packages can be installed with a terminal **pip**:

```text
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

Next, open a text editor (I like to use VS Code) and start a new python file called ```piston_motion.py```

We will start our ```piston_motion.py``` script by importing the necessary modules. NumPy is imported as the comman alias ```np```. Besides importing Matplotlib's ```pyplot``` module, we'll also import Matplotlib's ```animation``` module. 

```python
# import necessary packages
import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```

To model piston motion, we need to animate two moving parts: a crankshaft and a connecting rod.

The crankshaft rotates around a central axis with a constant radius. We'll model the crankshaft as a line of constant length, one end fixed at the origin and the other rotating in a circle like the hand on a clock. To model this line, we just need two points, the origin at ```x=0``` and ```y=0```  and the end of the line at the point ```x1``` and ```x2```.

We also need to define a crank radius and a connecting rode length. We will define these constants at the top of our code.

We'll set a fixed number of rotations so that the animation does not run around indefininelty. The rotation increment defines how fine the 'ticks' are as our crankshaft arm rotates. A rotation increment of ```0.1``` will make our animation smooth enough.

```python
# input parameters
r = 1.0  # crank radius
l = 4.0  # connecting rod length
rot_num = 4 # number of crank rotations
increment = 0.1 # angle increment
```

## Arrays of angles

Next we'll create an array of angles starting from zero radians up to the number of rotations (times 2 pi radians), stepping by our increment amount. NumPy's ```np.arange()``` function accepts the arguments ```(start,stop,step)```. Python starts counting at ```0``` and ends counting at ```n-1```. NumPy follow the same counting convention, so if we want the final value in our angle array to be ```rot_num*2*pi``` we need to add the increment amount to it and set the stop argument as ```rot_num*2*pi+increment```.

```python
# create the angle array, where the last angle is the number of rotations*2*pi
angles = np.arange(0,rot_num*2*pi+increment,increment)
```

Once we have all the rotation angles in an array, we can set up empty arrays for the points in our animation. These point arrays need to have the same number of entries as the angle array:

```python
X1=np.zeros(len(angle)) # array of crank x-positions: Point 1
Y1=np.zeros(len(angle)) # array of crank y-positions: Point 1
X2=np.zeros(len(angle)) # array of rod x-positions: Point 2
Y2=np.zeros(len(angle)) # array of rod y-positions: Point 2
```

# Fill the point arrays

Now we will populate the point arrays with values according to the geometry of piston motion:

```python
# find the crank and connecting rod positions for each angle
for index, theta in enumerate(angles):

        x1 = r*cos(theta) # x-coordinate of the crank: Point 1
        y1 = r*sin(theta) # y-coordinate of the crank: Point 1
        x2 = 0 # x-coordinate of the rod: Point 2
        # y-coordinate of the rod: Point 2
        y2 = ((r*cos(theta-pi/2)) + (sqrt((l**2)-(r**2)*((sin(theta-pi/2))**2))))

        X1[index]=x1 #grab the crank x-position
        Y1[index]=y1 #grab the crank y-position
        X2[index]=x2 #grab the rod x-position
        Y2[index]=y2 #grab the rod y-position
```

## Set up the Matplotlib figure

Now that the point arrays are full, we have the values necessary to build the animation. We can start building the animation using these arrays of points. In this plotting section of the script, it is important to set ```aspect='equal'``` and ```autoscale_on=False```; otherwise the x and y axies will not have the same scale the animation will look ovoid instead of circular.

```python
# set up the figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-2,6))
ax.grid()
line, = ax.plot([], [], 'o-', lw=5, color='g')
```

## Initialization Function

The animation requires an initialization function:

```python
# initialization function
def init():
        line.set_data([], [])
        return line,

```

## Animation Function

Finally on to building the animation function and showing it.

```python
# animation function
def animate(i):
        thisx = [0, X1[i], X2[i]]
        thisy = [0, Y1[i], Y2[i]]

        line.set_data(thisx, thisy)
        return line,

# call the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(X1), interval=20, blit=True, repeat=False)
## to save animation, uncomment the line below:
## ani.save('piston_motion.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#show the animation
plt.show()
```

## Running the annimation

The animation can be run by running the ```piston_motion.py``` script. This can be accomplished using the Anaconda prompt or a terminal. Make sure the virtual environment we created above is active when the command is run.

```text
python piston_motion.py
```

## The complete script

The complete ```piston_motion.py``` script is below:

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
        #print piston_height
        #axis ([-r-l r+l -3*r 3*r+l]); %set the plot size
        #pause (speed); %wait before next iteration

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
        return line,

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


