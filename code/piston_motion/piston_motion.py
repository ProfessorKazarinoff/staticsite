"""
Piston Motion Animation using Matplotlib.
Animation designed to run on Raspberry Pi 2
Author: Peter D. Kazarinoff, 2016
Tribilium Engineering Solutions   www.tribilium.com
"""

#import necessary packages
import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#input parameters
r = 1.0  # crank radius
l = 4.0  # connecting rod length
rot_num = 4 # number of crank rotations
increment = 0.1 # angle incremement

#create the angle array, where the last angle is the number of rotations*2*pi
angles = np.arange(0,rot_num*2*pi+increment,increment)


X1=np.zeros(len(angles)) # array of crank x-positions: Point 1
Y1=np.zeros(len(angles)) # array of crank y-positions: Point 1
X2=np.zeros(len(angles)) # array of rod x-positions: Point 2
Y2=np.zeros(len(angles)) # array of rod y-positions: Point 2

#find the crank and connecting rod positions for each angle
for index, theta in enumerate(angles, start=0):

        x1 = r*cos(theta) # x-cooridnate of the crank: Point 1
        y1 = r*sin(theta) # y-cooridnate of the crank: Point 1
        x2 = 0 # x-coordinate of the rod: Point 2
        # y-coordinate of the rod: Point 2
        y2 = ((r*cos(theta-pi/2)) + (sqrt((l**2)-(r**2)*((sin(theta-pi/2))**2))))
        
        X1[index]=x1 #grab the crank x-position
        Y1[index]=y1 #grab the crank y-position
        X2[index]=x2 #grab the rod x-position
        Y2[index]=y2 #grab the rod y-position
        

# set up the figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-4,4), ylim=(-2,6))
ax.grid()
line, = ax.plot([], [], 'o-', lw=5, color='g')


# initialization function
def init():
        line.set_data([], [])
        return line,

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