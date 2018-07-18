Title: Picoweb and Pico-Notes
Date: 2018-07-18 10:15
Modified: 2018-07-18 10:15
Status: draft
Category: micopython
Tags: python, micropython, ESP8266
Slug: the-fair-talk-problem
Authors: Peter D. Kazarinoff
Summary: This post entails my investigation of a micropython project called picoweb. Picoweb is a micropython micro web framework (cute- a pico web framework). In this post, I will run through installing pico web on an ESP8266. 

## What is picoweb

Picoweb is micro web framework that is sort of like flask or bottle. Picoweb runs on smaller microcontrollers with micropython.


## Microcontroller vs. Unix distribution of picoweb

Picoweb can run on a microcontroller, but there is also a version of micropython that runs on Unix systems. First we'll try to get the picoweb running on Unix. Then we will get it picoweb going on an ESP8266 Board

## Picoweb on Unix

To get picoweb going on Unix, in particular by desktop running Ubuntu 16.04, I first cloned pfalcon's micropython github repository. I already cloned the micropython repo, so I used a different directory name for pfalcon's branch. In the pico-notes README, it mentions that running pfalcon's micropython fork is needed to get the application running

 > NOTE: Recent versions of uasyncio async framework and Picoweb web framework, and thus Notes Pico, require "advanced" fork of MicroPython at https://github.com/pfalcon/micropython .

```bash
$ cd ~
$ git clone git@github.com:pfalcon/micropython.git micropython-pfalcon
$ cd micropython-pfalcon
$ git submodule update --init
```

To get the micropython REPL on Ubuntu, you need to ```cd``` into the micropython unix port and run the micropython executable

```bash
$ cd ~/micropython-pfalcon
$ cd ports/unix
$ make axtls
$ make
$ ./micropython
```

When the Micropython REPL comes up, you test out typical python commands, and then try some commands that only work in micropython.

```
MicroPython v1.9.3-902-gd880d5b on 2018-07-18; linux version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>> a = [x**2 for x in range(5)]
>>> print(a)
>>> sys.implementation
(name='micropython', version=(1, 9, 3))
>>> sys.version
'3.4.0'
>>> sys.platform
'linux'
# [ctrl-d] to ext it the REPL
```

Next, I installed pico-notes into the unix version of micropython with ```upip```

```bash
$ pwd
~/micropython-pfalcon/ports/unix
$ ./micropython -m upip install -p app notes-pico
```

pfalcon notes that that the ```-p app``` flag and argument install notes-pico in the app directory

> app (argument of -p option) is a subdirectory into which to install the application.

Starting pico-notes intails being in the same directory that houses the ```app``` directory assigned above and running micropython with an environmental variable set

```
$ MICROPYPATH=app ./micropython -m notes_pico
mem: total=268751, current=62135, peak=76674
stack: 5712 out of 80000
GC: total: 2072832, used: 55712, free: 2017120
 No. of 1-blocks: 551, 2-blocks: 118, max blk sz: 81, max free sz: 62498
* Running on http://127.0.0.1:8081/

# [ctrl-c] to quit
```

Then we can browse on over to [http://127.0.0.1:8081/](http://127.0.0.1:8081/) and see pico-notes in action.

![pico-notes on unix](/posts/fairtalk/pico-notes-on-unix.png)

The app is pretty neat. Type in the text field and click add note. It puts the note below.

![pico-notes on unix](/posts/fairtalk/pico-note-added.png)

After playing around with the notes application, I tried out what it would look like on a phone:

![pico-notes on unix](/posts/fairtalk/pico-note-on-phone.png)

I pulled up a different web browser (chrome) and connected to the same IP address [http://127.0.0.1:8081/](http://127.0.0.1:8081/) with pico-note running. 

![pico-notes on unix](/posts/fairtalk/pico-note-on-chrome.png)

The notes added on chrome were reflected in the notes shown in firefox. Pretty neat!

![pico-notes on unix](/posts/fairtalk/pico-note-back-on-firefox.png)

## picoweb on an ESP8266

Now it is time to build some custom firmware for the ESP8266 because the pico-notes app is too big just to dump as regular .py files. This got a little tricky.