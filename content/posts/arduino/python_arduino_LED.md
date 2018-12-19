Title: Using Python to control an Arduino LED
Date: 2018-03-13 20:20
Modified: 2018-03-13 20:20
Status: draft
Category: python and arduino
Tags: python, arduino, serial, hardware, anaconda prompt
Slug: python-arduino-LED
Authors: Peter D. Kazarinoff

Python is used in many applications including data science, machine learning and web development. Another area where we can use Python is external hardware control. What do I mean by external hardware? A piece of external hardware could be a light or a sensor. External hardware includes multimeters or spectral analyzers. I consider anything connected to a computer that isn't typically connected to a computer as external hardware. So not a keyboard, mouse, headphones, webcams, USB drives, but things like motors, light arrays, solenoids, linear actuators, pressure sensors etc.  In this post, we review over how to use Python to control an LED that is conneted to an Arduino. Python running on a computer will turn the Arduino LED on and off.

## Install pyserial

To start a new Python project, it is best practice to create a new virtual environment. I have the **Anaconda** distribution of Python installed on my Windows 10 machine. When you [install **Anaconda**]({filename}/posts/installation/installing_anaconda_on_windows.md), it comes with the very useful **Anaconda Prompt**. Using the **Anaconda Prompt** is a bit like using the terminal on a MacOS or Linux. To start the **Anaconda Prompt** on Windows 10, go to the Windows start button on the lower left and select **Anaconda Prompt**.

![anaconda in start menu](images/anaconda_from_start_menu.png)

Let's create a new virtual environment for our Arduino LED project using the Anaconda Prompt:

```terminal
> conda create --name arduino python=3.7
```

The ```conda create``` command builds the new virtual environment. The ```--name arduino``` flag gives our new virtual environment the name ```arduino```.  I like to name my virtual environments the same name as the project that uses the virtual environment.  Including ```python=3.7``` ensures that the new virtual environment has an up to date version of Python.

Type ```y``` to confirm and create the new virtual environment. To use the new virtual environment ```arduino``` you need to _activate_ it by typing:

```terminal
> conda activate arduino
```

You know you are in the ```arduino``` virtual environment when ```(arduino)``` is in parenthesis at the start of the **Anaconda Prompt**:

```terminal
(arduino) >
```

To communicate with the Arudino using Python, you need to install the **pyserial** package. You can do this at the **Anaconda Prompt** using the command ```conda install pyserial```. Note the ```(arduino)``` virtual environment needs to be active when you run the ```conda install``` command.

```terminal
(arduino) > conda install pyserial
```

To confirm that **pyserial** is installed, open the Python REPL while the ```(arduio)``` virtual environment is activate. At the ```>>>``` REPL prompt, import **pyserial** with the command ```import serial```. Note that although we installed **pyserial** with the command ```conda install pyserial```, we import **pyserial** using the line ```import serial```. 

```terminal
(arduino) > python
>>> import serial
>>> serial.__version__
'3.4'
>>>
```

## Download the Arduino IDE

Download the Arduino IDE using the following link: 
[https://www.arduino.cc/en/Main/Software](https://www.arduino.cc/en/Main/Software) 
Scroll down the page to the Download the Arduino IDE section. Be sure to select: **Windows ZIP file for non-admin install** as new software can not be installed on lab computers without administrator privileges. You can select **JUST DOWNLOAD** from the donation screen. Extract the downloaded .zip folder to your thumb drive or the desktop.

![Arduino Download Page]({filename}/posts/arduino/images/arduino_download_page.png)

## Wire an LED and a resistor to the Arduino

Take out an LED (any color), a 330 Ohm resistor, two jumper wires, the Arduino and a white breadboard. Connect the LED, resistor and wires as shown below. Note the LED has two different sized ``legs" Ensure the LED is wired in the correct orientation. LED short leg --> resistor, LED long leg --> Pin 13. Also see the SIK GUIDE page 19 and the SparkFun Inventor’s kit online guide: 

> [https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino—v33/experiment-1-blinking-an-led](https://learn.sparkfun.com/tutorials/sik-experiment-guide-for-arduino—v33/experiment-1-blinking-an-led)

![Redboard LED Fritzing]({filename}/posts/arduino/images/redboard_LED_bb.png)


## Load the Arduino example sketch **Blink.ino** onto the Arduino. Confirm the Arduino and LED blinks

Open the extracted Arduino IDE folder and double-click the **Arduino.exe** program. Open the Arduino **Blink.ino** sketch by going to: File --> Examples --> 01.Basics --> Blink. 

![blink.ino in examples menu]({filename}/posts/arduino/images/blink_in_examples_menu.png)

Connect the Arduino to the computer using the red USB cable. Note that USB ports connected to monitors sometimes do not work correctly. Connect to a computer USB port, not a monitor USB port. In the Arduino IDE Window that contains the **Blink.ino** sketch, click the check mark to Verify then click the arrow to Upload. 

![check to verify]{filename}/posts/arduino/images/Check_to_Verify.png)

![arrow to upload]{filename}/posts/arduino/images/Arrow_to_Upload.png)

Once the upload is complete, the Arduino and LED should blink on and off. If you don't see the Arduino and LED blinking, you need to do some trouble shooting. Check the **COM Port** or try unplugging and re-plugging in the Arduino. 

## Load the Arduino example sketch **PhysicalPixel.ino**

Open the Arduino sketch **PhysicalPixel.ino** by going to File --> Examples --> 04.Communication --> PhysicalPixel. 

   ![image name]({filname}/posts/arduino/images/physicalpixel_in_examples_menu.png)

Once again, click the check mark to Verify then click the arrow to Upload. 


   ![image name]({filname}/posts/arduino/images/Check_to_Verify.png)

   ![image name]({filname}/posts/arduino/images/Arrow_to_Upload.png)


## Use the Arduino Serial Monitor to turn the Arduino LED on and off

In the Arduino IDE Window that contains th **PhysicalPixel.ino** sketch, open the Arduino Serial Monitor by going to Tools --> Serial Monitor.

![image name]({filname}/posts/arduino/images/Tools_SerialMonitor.png)


In the Arduino Serial Monitor type: **H** and click Send (or press ENTER). Then type: **L** and click Send (or press ENTER). You should see the Arduino LED switch on and off. If you are have trouble, make sure the **Port** is set correctly in Tools --> Port and make sure the Serial Monitor is set to 9600 baud. 

![image name]({filname}/posts/arduino/images/SerialMonitor_H.png}
