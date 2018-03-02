import matplotlib.pyplot as plt
import numpy as np

#import sys
#print (sys.executable)
#print (sys.path)
#import tkinter
#tkinter._test()
x = np.linspace(-np.pi, np.pi, 100)
y = 2*np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Free Body Diagram')
ax.plot(x, y)
ax.spines['left'].set_position('zero')
ax.spines['left'].set_color('gray')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['bottom'].set_color('gray')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
#ax.xaxis.
ax.yaxis.set_ticks_position('left')

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.show()