Title: Using the Micropython RERL on an Adadfruit Feather Huzzah ESP8266
Date: 2018-02-26 09:01
Modified: 2018-02-26 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller, LED, REPL
Slug: micropython-REPL
Authors: Peter D. Kazarinoff
Series: micropython
series_index: 3

This is the third part of a multipart series on Micropython. In last post of the series, we installed micropython on an Adafruit Feather Huzzah ESP8266 board using Python and a package called esptool. In this post, we are going to write commands to the Python REPL (the Micropython prompt) running on the feather board to turn on and off an LED.

Before we can use the Micropython REPL (the Microython prompt) running on the Adafruit Feather Huzzah ESP8266, Micropython needs to be installed on the board and Putty needs to be installed to communicate with the board over serial. See the [previous post]({filename}micropython_install.md) on how to install Micropython on the board and install Putty on a Windows 10 machine.

Summary of Steps:

1. Connect the Adafruit Feather Huzzah ESP8266 using a USB cable
2. Determine which COM port the board is connected to using the Windows Device Manager 
3. Open Putty and connect to the board at 115200 baud
4. Run commands at the prompt to turn the builtin LED on the Adafruit Feather Huzzah ESP8266 on and off

### 1. Connect the Adafruit Feather Huzzah ESP8266 board to the laptop

Use a microUSB cable to connect the Feather Huzzah to the computer. Make sure that the microUSB cable is a full USB data cable and not just a simple power cable. The first cable I tried was just for charging mobile phones and I couldn't figure out why Putty wasn't working. Switching out the cable was all it took to get it to work. 

### 2. Determine which serial port the Feather Huzzah is connected to

Use Windows device manager to determine which serial port the Feather Huzzah is connected to. On my Windows 10 laptop, it usually comes up as ```COM4```. You can find the serial port by looking in the Ports(COM and LPT) category. The Feather Huzzah board will be listed under "Silicon Labs CP201x  USB to UART bridge (COM#)" It is the **COM#** that you are looking for.

![Find Device Manager]({filename}/posts/micropython/find_device_manager.png)

![Device Manager Menu]({filename}/posts/micropython/device_manager_menu.png)

### 3. Use Putty to connect to the Feather Huzzah

Ensure the Feather is connected with a USB cable, and connect to it with Putty using the proper serial port (COM#) and 115200 baud. Remember to use the **Serial** radio button under **Connection Type:**

![Putty in start menu]({filename}/posts/micropython/putty_in_start_menu.png)

![Putty config]({filename}/posts/micropython/putty_config.PNG)

This should bring up the Micropython REPL prompt ```>>>```. If you can't see the ```>>>``` prompt, try typing [Enter], Ctrl-D, pushing the RESET button on the Feather Huzzah or unplugging then replugging the USB cable.

![REPL prompt]({filename}/posts/micropython/REPL_prompt.PNG)


### 4. Run commands at the prompt to turn the built-in LED on the Adafruit Feather Huzzah ESP8266 on and off

At the micropython REPL (the Micropython command promt ```>>>```) try the following commands:

```
>>> print('Micropython for Engineers!')
Micropython for Engineers
```

```
>>> import sys
>>> sys.implementation
(name='micropython', version=(1, 9, 3))
>>> sys.platform
'esp8266'
```

![REPL prompt]({filename}/posts/micropython/sys_dot_implementation_and_platform.PNG)

If you see similar output, that means Micropython is working.

Now let's turn the built-in LED that's on the Adafruit Feather Huzzah board on and off. We do this with Micropython's ```machine``` module. First we use the ```machine``` module to create a ```Pin``` object. The first argument is the pin number on the board. Pin zero on the Feather Huzzah is connected to the built-in LED. The second argument is the pin type. We want Pin 0 to act as an ouput pin. We are going to assin it the attribute ```.on()``` or ```.off()```. This will cause the Feather board to output a positive voltage or no voltage at Pin 0 to turn the built-in LED on and off. You can also connect Pin 0 to an LED through a resistor (then to ground) and have this LED turn on and off.

```
>>> import machine
>>> pin = machine.Pin(0, machine.Pin.OUT)
```

Note that Pin 0 on the Adafruit Feather Huzzah is kind of wired "backwards". We call ```pin.off()``` and the built-in LED turns **on** and call ```pin.on()``` and the built-in LED turns **off**.  

```
>>> pin.on()
>>> pin.off()
>>> pin.on()
>>> pin.off()
```

Now let's see if we can make the LED blink. We'll do this with a simple ```for``` loop. At the micropython REPL, initiating a loop will automatically indent the next line, so a tab is not needed before the ```print``` statement. To run the loop, we type backspace on an empty line (to backspace from an indented line) and hit return.

```
>>> import time
>>> for i in range(10):
...     pin.on()
...     time.sleep(1)
...     pin.off()
...     time.sleep(1)
...
```

This will blink the LED on and off for a total of 20 seconds.

## Next steps:
Next we'll connect to a I2C temperature sensor to the Adafruit Feather Huzzah and use Micropython to read out the temperature.