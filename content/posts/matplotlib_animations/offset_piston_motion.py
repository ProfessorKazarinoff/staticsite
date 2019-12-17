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
