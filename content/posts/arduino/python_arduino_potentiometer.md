Title: Using Python to read a potentiometer connected to an Arduino
Date: 2018-03-13 20:20
Modified: 2018-03-13 20:20
Status: draft
Category: python and arduino
Tags: python, arduino, serial, hardware, sensor, matplotlib
Slug: python-arduino-potentiometer
Authors: Peter D. Kazarinoff

Python is used in many applications including data science, machine learning and web development. Another area where we can use Python is external hardware control. What do I mean by external hardware? A piece of external hardware could be a light or a sensor. External hardware includes multimeters or spectral analyzers. I consider anything connected to a computer that isn't typically connected to a computer as external hardware. So not a keyboard, mouse, headphones, webcams, USB drives, but things like motors, light arrays, solenoids, linear actuators, pressure sensors etc.  In this post we see how to use Python to read the value comming off a potentiometer conneted to an Arduino. Python running on our computer will read data from an external sensor, then we will use numpy and matplotlib to plot the data.

To complete this Python project, it is best practice to use a virtual environment. I have the **Anaconda** distribution of Python installed on my Windows 10 machine. In the last post, we reviewed how to create a new virtual enviromment called ```(arduino)```. Before we start this project, we will activate the ```(arduino)``` virtual environment and ensure that the ```pyserial``` package is installed.

![anaconda in start menu](images/anaconda_from_start_menu.png)

```terminal
conda activate arduino
```

You know you are in the ```arduino``` virtual environment when ```(arduino)``` is in parenthesis at the start of the prompt:

```terminal
(arduino) >
```

To communicate with the Arudino using Python over a serial line, we need to have the **pyserial** package installed. We can install **pyserial** from the **Anaconda Prompt** using the ```conda install``` command.

```terminal
(arduino) > conda install pyserial
```


1. Virtual environment and pyserial
2. Download Arduino IDE
3. "Blink" the Arduino, make sure it is working
4. Wire the potentiometer to the Arduino 
5. Copy the potentiometer.ino sketch and upload to the Arduino
6. Use the Arduino Serial Monitor and Serial Plotter
7. Construct and run the Python script to read the potentiometer value
