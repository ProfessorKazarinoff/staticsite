Title: Piston Motion with Python and matplotlib
Date: 2017-09-15 20:40
Modified: 2017-09-15 20:40
Status: Draft
Category: Python
Tags: python, matplotlib, animation
Slug: piston-motion
Authors: Peter D. Kazarinoff
Summary: An animation of piston motion created with Python and matplotlib

Piston motion is one of the classic dynamic types of motion that belong to a category of 4-bar motion. Piston motion is the type of motion that the piston in a cylinder of a car engine goes through as the crankshaft rotates. 

## Set up a python virtual environment

To start this process, we will set up a virtual environment in Python.

Real Python has a good [introduction to virtual environments](https://realpython.com/blog/python/python-virtual-environments-a-primer/) and why to use them.

I recommend undergraduate engineers use the Anaconda distribution of Python which comes with the **Anaconda Prompt**. A new virtual environment can be set up by opening the **Anaconda Prompt** and typing:


Using the Anaconda Prompt:

```text
> mkdir piston_motion
> cd piston_motion
> conda create -n piston_motion python=3.6
```

Alternatively, a virtual environment can be set up with a terminal prompt and **pip**

Using a terminal:

```text
$ mkdir piston_motion
$ cd piston_motion
$ mkvirtualenv piston_motion -p python3
```

Now that we have a new clean virtual environment with Python 3 installed, we need to install the necessary packages:

Using the Anaconda Prompt, activate the ```piston_motion``` virtual environment and use conda to install the Python Packages:

```text
> conda activate piston_motion
(piston_motion) > conda install numpy
(piston_motion) > conda install matplotlib
```

Alternatively, the packages can be installed with **pip**:

```text
$ workon piston_motion
(piston_motion) $ pip install numpy
(piston_motion) $ pip install matplotlib
(piston_motion) $ pip freeze
cycler==0.10.0
matplotlib==2.0.2
numpy==1.13.1
pyparsing==2.2.0
python-dateutil==2.6.1
pytz==2017.2
six==1.10.0
```

Next, open a text editor or IDLE and start a new python file called ```piston_motion.py```
We will start our script by importing the necessary modules

```python
# import necessary packages
import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```

To model piston motion we need to have two moving parts. One is the crankshaft. The crankshaft rotates around a central axis with a constant radius. We will model this with a line of constant length, one end fixed at the origin and the other rotating in a circle like the hand on a clock. To model this line, we just need two points, the origin at x=0 and y=0  and the end of the line at the point ```x1``` and ```x2```. We also need to have a crank radius and a connecting rode length. We will define these constants at the top of our code. So that the animation does not run around indefininelty we will set a fixed number of rotations.  The rotation increment defines how fine the 'ticks' are as our crankshaft arm rotates. 0.1 will work to make the animation smooth enough.

```
# input parameters
r = 1.0  # crank radius
l = 4.0  # connecting rod length
rot_num = 4 # number of crank rotations
increment = 0.1 # angle increment
```

Next we'll create an array of angles starting from zero radians up to the number of rotations (times 2 pi radians), stepping by our increment amount. Numpy's ```np.arange()``` function accepts the arguments ```(start,stop,step)```. Python starts counting at zero and ends counting at n-1. Numpy follows this counting convention, so if we want the final value in angle array to be ```rot_num*2*pi``` we need to add the increment amount to it and set the stop argument as ```rot_num*2*pi+increment```.

```
# create the angle array, where the last angle is the number of rotations*2*pi
angles = np.arange(0,rot_num*2*pi+increment,increment)
```

Once we have all the rotation angles in an array, we can set up empty arrays for the points in our animation. These point arrays need to have the same number of entries as the angle array:

```
X1=np.zeros(len(angle)) # array of crank x-positions: Point 1
Y1=np.zeros(len(angle)) # array of crank y-positions: Point 1
X2=np.zeros(len(angle)) # array of rod x-positions: Point 2
Y2=np.zeros(len(angle)) # array of rod y-positions: Point 2
```

Now we will populate the point arrays with values according to the geometry of piston motion:

```
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

With the point arrays full, we have the values necessary to build the animation, and we can start building the animation using these points. It is important to set ```aspect='equal'``` and ```autoscale_on=False``` otherwise the x and y axies will not have the same scale the animation will look ovoid instead of circular.

```
# set up the figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-2,6))
ax.grid()
line, = ax.plot([], [], 'o-', lw=5, color='g')
```

The animation requires an initialization function:

```
# initialization function
def init():
        line.set_data([], [])
        return line,

```

Finally on to building the animation function and showing it.

```
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