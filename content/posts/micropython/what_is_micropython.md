Title: What is Micropython?
Date: 2018-02-26 09:01
Modified: 2018-02-26 09:01
Status: published
Category: micropython
Tags: python, micropython, esp8266, microcontroller, REPL
Slug: what-is-micropython
Authors: Peter D. Kazarinoff
Series: micropython
series_index: 1

This is the first part of a multipart series on Micropython. In this post we'll review what Micropython is, what it is used for and how it is both similar and different from "regular" Python. We'll also discuss why Micropython is relevant to undergraduate engineers.

### 1. What is Micropython?

[Micropython](http://micropython.org/) is a port, or version of Python designed to run on small, inexpensive, low-power microcontrollers. Examples of microcontrollers that Micropython can run on include the [pyboard](https://store.micropython.org/), the [WiPy](https://pycom.io/development-boards) and ESP8266 boards like the [Adafruit Feather Huzzah](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266).  Normally, Python is run on a desktop or laptop computer (also on big servers at server farms). Compared to a desktop or laptop, microcontrollers are much smaller, cheaper and less powerful.  A "regular" version of Python can't run on small, cheap microcontrollers because Python is too resouce intensive. Regular Python takes up too much hard disk space, runs on too much RAM and requires a more powerful processor than microcontrollers have. 

It is pretty amazing that a version of Python (Micropython) runs on these small, cheap microcontrollers like the ESP8266. To get Micropython to run at all on these small boards, Micropython only contains a subset of all the standard library modules inlcuded with "regular" Python. Some of the libraries that are included with Micropython don't have the full set of functions and classes that come with the full version of Python. This allows Micropython to be compact (around 600 kB for the ESP8266 port) and only use a small amount of RAM (down to 16k according to the [Micropython main page](https://micropython.org/))

You can try using Micropython online with this neat [Micropython online emulator](https://micropython.org/unicorn/). The emulator allows you to run commands at a Micropyton Prompt and see the result on a virtual pyboard. 

### 2. What is Micropyton used for?

Micropython is installed on small, cheap microcontrollers like the [ESP8266](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266). Anthing these small microcontrollers can do, Micropython can do. This includes using the microcontroller as a remote sensor to measure things like temperature, humidity and light level. Micropython can also be used to blink LED's, control arrays of LED's, or run small displays. Micropython can control servo motors, stepper motors and solenoids. Civil Engineers could use Micropython to monitor water levels. Michanical Engineers could use Micropython to drive robots. Electrical Engineers could use micropython to measure voltage levels in embedded systems. In the later posts in this series, we will use Micropython, running on a small cheap ESP8266 board, to create a remote internet-connected weather station. The last posts in the series will use Micropyton, running on a __really cheap__ (around $2) ESP-01 module to turn on and off an LED from any computer connected to the internet anywhere in the world.

### 3. Why should undergraduate Engineers learn Mircopython?

Using Python to solve engineering problems such as calculations, statistics, modeling and visulization is really useful for undergraduate Engineers. But Python on it's own is fairly limited in controlling devices outside the computer it's running on. You don't want to leave a laptop in a remote estuary to meausure water temperature, but you could leave a little microcontroller and low-cost temperature sensor. A small robot can't carry around a heavy laptop, but a small, light, low-power board could run a simple robot. You don't want to use a laptop for every small electrical measurement or embedded system control, but a $2 WiFi module would work. 

In addition, learning how to use Micropython on small, cheap microcontrller can help undergraduates Engineers understand how programming works. It is a different kind of feedback and excitment seeing a motor whirl around compared to seeing a picture of a motor with the speed displayed as text. There is a different kind of wonder seeing an array of LED's light up compared to a 2-D plot on a computer screen. Plus Micropython is just fun! It's as easy to program Micropython as it is to program regular Python. The little projects you can do with Micropython running on a small, low-cost board are almost unlimited. We could send Micropython to space in a micro-satalite, or burry Micropython underground in a small borring machine, or launch Micorpython into the sky on a weather ballon.

### Next steps:
In the next post, we will install Micropython on a small, cheap ESP8266 microcontroller board called the Adafruit Feather Huzzah. Once Micropython is installed on the board, we will run a couple commands at the Micropython REPL running on the board.
