Title: What is Micropython?
Date: 2018-26-17 09:01
Modified: 2018-02-26 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller, REPL
Slug: what-is-micropython
Authors: Peter D. Kazarinoff
Series: micropython
series_index:1

This is the first part of a multipart series on Micropython. In this post we'll review what Micropython is, what it is used for and how it is both similar and different from "regular" Python. We'll also discuss why Micropython is relevant to undergraduate engineers.

### 1. What is Micropython?

[Micropython](http://micropython.org/) is a port, or version of Python designed to run on small, inexpensive, low power microcontrollers. Normally, Python is run on a desktop or laptop computer. Compared to a desktop or laptop, microcontrollers are much smaller, cheaper and less powerful. A "full"version of Python can not run on microcontrollers because Python is too resouce intensive. Regular Python takes up too much hard disk space, runs on too much RAM and requires a more powerful processor than microcontrollers have. Examples of microcontrollers that Micropython can run on include the [pyboard](https://store.micropython.org/), the [WiPy](https://pycom.io/development-boards) and ESP8266 boards like the [Adafruit Feather Huzzah](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266).

It is pretty amazing that a version of Python (Micropython) runs on these small cheap microcontrollers. To get Micropython to run at all on these cheap small boards, Micropython only contains a subset of all the standard library modules inlcuded with "regular" Python. Some of the libraries that are included with Micropython don't have the full set of functions and classes in the "regular" version of Python. This allows Micropython to be compact (around 600 kB for the esp8266 port) and use a small amount of RAM (down to 16k according to the [Micropython main page](https://micropython.org/))

You can try using Micropython online with this neat [Micropython online emulator](https://micropython.org/unicorn/). The emulator will allow you to run commands at a Micropyton Prompt and see the result on a virtual pyboard. 

### 2. What is Micropyton used for?

Micropython is installed on small cheap microcontrollers like the esp8266. Anthing these microcontrollers can do, Micropython can do. This includes using the microcontroller as a remote sensor to things like monitor temperature, humidity and light level. Micropython could also be used to blink LED's, control arrays of LED's, and run small displays. Micropython can also control servo motors, stepper motors and solenoids. Civil engineers could use micropython to monitor water levels. Michanical engineers could use micropython to drive robot motors. Electrical engineers could use micropython to measure voltage levels. In the later posts in this series, we will use micropython running on a small cheap ESP8266 board to create a remote weather station. The last posts in the series will use micropyton running on a really cheap (around $2) ESP-01 module to turn on an off an LED from any computer connected to the internet anywhere in the world.

### 3. Why should Undergraduate Engineers learn Mircopython?

Using Python to solve engineering problems such as calculations, statistics, modeling and visulization is really useful. But Python on it's own is fairly limited in controlling devices outside the computer that it's running on. You would not want to leave a laptop in a remote estuary to meausure temperature. You would not want a small robot to have to carry around a heavy laptop that has to be plugged into the wall periodically in order for it to move. You don't want to use a laptop for every small electrical measurement or control. In addition, learning how to use Micropython on a small cheap microcontrller can help undergraduates understand how programming works. There is a different kind of feedback and excitment seeing a motor whirl around compared to seeing a picture of a motor with the speed displayed as text. There is a different kind of wonder seeing an array of LED's light up compared to a 2-D plot on a computer screen. Plus Micropython is just fun! It's as easy to program as regular Python and there are all sorts of little projects to do with a microcontroller. 

## Next steps:
In the next post, we will install Micropython on a small cheap ESP8266 board called the Adafruit Feather Huzzah. Once micropython is installed on the board, we will run a couple commands at the Micropython REPL running on the board. 