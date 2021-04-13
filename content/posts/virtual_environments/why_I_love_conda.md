Title: Why I love conda
Date: 2017-10-20 8:20
Modified: 2017-10-10 8:21
Status: Draft
Category: Python
Tags: python, virtualenvs, anaconda, conda
Slug: why-i-love-conda
Authors: Peter D. Kazarinoff
Summary: This post is a love letter of sorts to the conda prompt. All the reasons I love to use conda and why I think conda is often a better way to go than using pip.

### The conda prompt works in Windows

Conda prompt, how I love thee. Conda prompt, you work on windows. My machine at work is a Windows 10 Desktop. From the windows start menu it always available:

![conda prompt on windows start menu]({static}/images/conda_in_windows_start_menu.png)

### The conda prompt works in Windows Locked down by your IT Department

Conda prompt, how I love thee. Pip installing python packages on Windows can be a kind of a nightmare or at least full of surprises. pip isn't automatically available from the windows command window. It takes some configuration and messing around with settings deep inside the bowels of windows settings to get it to work. If you finally are able to get pip to work from the windows command line, you still may not be able to install packages because windows won't let you install them. Installing packages is easy with wonderful conda.
 
### The conda prompt handles virtual environments
 
 Conda prompt, how I love thee. Using ```virlenv``` and ```virtualenv wrapper``` works pretty great actually, but in windows you have to be in the right directory in order to fire them off. When you open the conda prompt you just type ```activate```.  Doesn't matter which directory you are in.
 
### The conda prompt behaves like a regular linux or mac terminal
 
 In the conda prompt, you can type regular commands like ```ls```. At the windows prompt you have to type ```dir```. At the conda prompt you can ```cd``` into directors with "regular" file paths. ```cd code/python/plotting``` in windows the slashes go the other way. It makes me feel like I'm typing LaTeX commands. cd ```code\python\plotting```.
 