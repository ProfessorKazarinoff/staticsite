Title: Why I use Conda
Date: 2022-05-22 8:20
Modified: 2022-05-22 8:21
Status: Draft
Category: Python
Tags: python, virtualenvs, anaconda, conda
Slug: why-i-use-conda
Authors: Peter D. Kazarnoff
Summary: This post is a love letter of sorts to the Anaconda Prompt and Conda. The reasons I love to use Conda and why I think Conda is often a better tool for Engineers to use than pip.

### The conda works on Windows

Conda, how I love thee. Conda, you work on windows. My machine at work is a Windows 10 Desktop. From the windows start menu it always available:

![conda prompt on windows start menu]({static}/images/conda_in_windows_start_menu.png)

### Conda works in Windows Locked down by your IT Department or school

Conda, how I love thee. Pip installing python packages on Windows can be a kind of a nightmare or at least full of surprises. pip isn't automatically available from the windows command window. It takes some configuration and messing around with settings deep inside the bowels of windows settings to get it to work. If you finally are able to get pip to work from the windows command line, you still may not be able to install packages because windows won't let you install them. Installing packages is easy with wonderful conda.
 
### Conda handles virtual environments
 
 Conda, how I love thee. Using ```virlenv``` and ```virtualenv wrapper``` works pretty great actually, but in windows you have to be in the right directory in order to fire them off. When you open the conda prompt you just type ```activate```.  Doesn't matter which directory you are in.
 
### The conda prompt behaves like a regular linux or mac terminal
 
 In the conda prompt, you can type regular commands like ```ls```. At the windows prompt you have to type ```dir```. At the conda prompt you can ```cd``` into directories with "regular" file paths. ```cd code/python/plotting``` in Windows the slashes go the other way. It makes me feel like I'm typing LaTeX commands. cd ```code\python\plotting```.
 
 ### You can install non-python packages with conda

 Conda, how I love thee. You can install non-python packages which can be tough to set up especially on windows. This includes packages like ffmpeg and tessearct that aren't python packages, but do have python wrapper packages.
