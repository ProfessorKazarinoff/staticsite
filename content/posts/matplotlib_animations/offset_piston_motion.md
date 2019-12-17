Title: Offset Piston Motion with Python and matplotlib
Date: 2017-10-15 20:40
Modified: 2017-10-15 20:40
Status: Draft
Category: matplotlib
Tags: python, matplotlib, animation
Slug: offset-piston-motion
Authors: Peter D. Kazarinoff
Summary: An animation of offset piston motion created with Python and matplotlib

Offset piston motion is one of the classic dynamic types of motion that belong to a category of 4-bar motion. Piston motion is the type of motion that the piston in a cylinder of a car engine goes through as the crankshaft rotates. 

## Set up a python virtual environment

To start this process, we will set up a virtual environment on python. 

Real Python has a good [introduciton to virtual environments](https://realpython.com/blog/python/python-virtual-environments-a-primer/) and why to use them.

Using the terminal:
```bash
$ mkdir piston_motion
$ cd piston_motion
$ mkvirtualenv piston_motion -p python3
```

Now that we have the a new clean virtual environment with Python 3 installed, we need to install the necessary packages
```none
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

Open a text editor or IDLE and start a new python file called ```piston_motion.py```
We will start our script by importing the necessary modules

```python
#import necessary packages
import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```

To model piston motion we need to have two moving parts. One is the crankshaft. The crankshaft rotates around a central axis with a constant radius. We will model this with a line of constant length, one end fixed at the origin and the other rotating in a circle like the hand on a clock. To model this line, we just need two points, the origin at x=0 and y=0  and the end of the line at the point ```x1``` and ```x2```. We also need to have a crank radius and a connecting rode length. We will define these constants at the top of our code. So that the animation does not run around indefininelty we will set a fixed number of rotations.  The rotation increment defines how fine the 'ticks' are as our crankshaft arm rotates. 0.1 will work to make the animation smooth enough.

```
#input parameters
r = 1.0  # crank radius
l = 4.0  # connecting rod length
rot_num = 4 # number of crank rotations
increment = 0.1 # angle incremement
```
