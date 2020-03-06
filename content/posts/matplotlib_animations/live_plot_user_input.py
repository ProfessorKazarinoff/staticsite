# live_plot_user_input.py

# import necessary packages
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# initial data
data = [3, 6, 2, 1, 8]

# create figure and axes objects
fig, ax = plt.subplots()

# animation function
def animate(i):
    with open("data.txt", "r") as f:
        for line in f:
            data.append(int(line.strip()))
    ax.clear()
    ax.plot(data[-5:])  # plot the last 5 data points


# call the animation
ani = FuncAnimation(fig, animate, interval=1000)
ani.save("images/live_plot_user_input.html", writer="html", fps=1)

# show the plot
plt.show()
