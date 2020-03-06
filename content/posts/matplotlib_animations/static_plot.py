# static_plot.py
"""A simple Python script to build a line plot using Matplotlib"""

# import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# data
temps = [60, 59, 49, 51, 49, 52, 53, 54]

# create the figure and axis objects
fig, ax = plt.subplots()

# plot the data and customize
ax.plot(temps)
ax.set_xlabel("Day Number")
ax.set_ylabel("Temperature (*F)")
ax.set_title("Temperature in Portland, OR over 7 days")

# save and show the plot
fig.savefig("images/static_plot.png")
plt.show()
