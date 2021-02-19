import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


plt.style.use('seaborn')
# change the range to cut off one end or other of the curve
x = np.arange(-10, 10, 0.001)
# Mean = 0, SD = 2.
y = norm.pdf(x,0,2)
fig, ax = plt.subplots()
ax.fill_between(x,y,0, alpha=0.5)
plt.xlim([-10,10])
plt.title('Normal Gaussian Curve')
plt.show()