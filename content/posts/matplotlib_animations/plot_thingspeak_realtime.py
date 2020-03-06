# plot_thingspeak_realtime.py

"""
A Python script that plots live data from Thingspeak.com using Matplotlib
inspiration from:
https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time
"""
import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation

url = "https://api.thingspeak.com/channels/12397/fields/2.json?results=1"

# function to pull out a float from the requests response object
def pull_float(response, field_num="2"):
    jsonr = response.json()
    field_str = "field" + field_num
    strr = jsonr["feeds"][0][field_str]
    if strr:
        fltr = round(float(strr), 2)
        return fltr
    else:
        return None


# Create figure for plotting
fig, ax = plt.subplots()
xs = []
ys = []


def animate(i, xs: list, ys: list):
    # grab the data from thingspeak.com
    response = requests.get(url)
    flt = pull_float(response, "2")
    print(flt)
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime("%H:%M:%S"))
    ys.append(flt)
    # Limit x and y lists to 10 items
    xs = xs[-10:]
    ys = ys[-10:]
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    # Format plot
    ax.set_ylim([0, 10])
    plt.xticks(rotation=45, ha="right")
    plt.subplots_adjust(bottom=0.30)
    plt.title("Wind Speed from ThingSpeak Channel 948462")
    plt.ylabel("Wind Speed (mph)")


# Set up plot to call animate() function every 1000 milliseconds
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
