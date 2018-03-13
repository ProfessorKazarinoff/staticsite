Title: Using Python to control an Arduino LED
Date: 2018-03-13 20:20
Modified: 2018-03-13 20:20
Status: draft
Category: python and arduino
Tags: python, arduino, serial, hardware, anaconda prompt
Slug: python-arduino-LED
Authors: Peter D. Kazarinoff

Python is used in many applications including data science, machine learning and web development. Another area where we can use Python is external hardware control. What do I mean by external hardware? A piece of external hardware could be a light or a sensor. External hardware includes multimeters or spectral analyzers. I consider anything connected to a computer that isn't typically connected to a computer as external hardware. So not a keyboard, mouse, headphones, webcams, USB drives, but things like motors, light arrays, solenoids, linear actuators, pressure sensors etc.  In this post we review over how to use Python to control an LED that is conneted to an Arduino. Python running on our computer will turn the Arduino LED on and off.

To start a new Python project, it is best practice to create a new virtual environment. I have the **Anaconda** distribution of Python installed on my Windows 10 machine. When you [install **Anaconda**]({filename}installing_anaconda_on_windows.md), it comes with the very useful **Anaconda Prompt**. Using the **Anaconda Prompt** is a bit like using the terminal on a Mac OSX or Linux. To start the **Anaconda Prompt** on Windows 10, go to the Windows start button on the lower left and select **Anaconda Prompt**.

![anaconda in start menu](images/anaconda_from_start_menu.png)

Let's create a new virtual environment for our Arduino LED project using the Anaconda Prompt:

```terminal
conda create --name arduino python=3.6
```

The ```conda create``` command builds the new virtual environment. The ```--name arduino``` flag gives our new virtual environment the name ```arduino```.  I like to name my virtual environments the same name as the project that I will use that environment for, or after the name of the package that will be used the most.  Including ```python=3.6``` ensures that your virtual environment has an up to date version of python.

Type ```y``` to confirm that you want to create the new virtual environment. To use the new virtual environment ```arduino``` you need to _activate_ it by typing:

```terminal
conda activate arduino
```

You know you are in the ```arduino``` virtual environment when ```(arduino)``` is in parenthesis at the start of the prompt:

```terminal
(arduino) >
```

To communicate with the Arudino using Python we need to install the **pyserial** package. We can do this at the **Anaconda Prompt** using the ```conda install``` command.

```terminal
(arduino) > conda install pyserial
```

