Title: Django IoT Server - Part 2 Development Environment
Date: 2019-03-21 09:21
Modified: 2019-03-21 09:21
Status: draft
Category: Django
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part2-development-environment
Authors: Peter D. Kazarinoff

In this post, we are going to review the development environment we'll use to build the Django IoT Server. 

[TOC]

## What is a Development Environment?

What does _development environment_ even mean? Before we started building the IoT server, we needed to make sure the necessary software, packages, and settings were in place. This begins with setting up a development environment. 

 > A development environment is merely the software on a computer that allows me to get work done. 
 
 In this case, the development environment includes the tools necessary to build the server.

## Computer and Operating System

I have a couple different computers that I'm going to use to build the Django IoT server. Below is a list of the machines I'll use. I want to make sure that I have the same Python packages installed on each computer and make sure that the version of the Django IoT server is shared accross all of these machines.

 * Windows 10 Desktop at work

I have a Windows 10 Desktop at work with two monitors. One limitation is that I don't have administrator access on my work desktop, so I can't install new programs.

 * Windows 10 Laptop at home

My main computer at home is an old Windows 10 laptop. The screen suround is comming off, the battery doesn't last very long, and the speakers don't always work. But for developing a Django IoT server, it will work just fine. 

 * MacOS Laptop at home

My wife has a MacBook Air at home. It is pretty old, but still humming along. Compared to the Windows 10 computers I use, the MacOS operating system is a little easier to write code on. MacOS has _the terminal_. The MacOS terminal is helpful when working with **Git** and remote servers over SSH. On Windows 10, the substitue for the MacOS terminal is the **Anaconda Prompt**. 

 * Ubuntu Desktop at home

I have a Desktop computer at home that runs the Ubuntu operating system. Ubuntu is a popular Linux distribution. Like MacOS, Ubutu comes with a termial program, called the Bash terminal. 

## Installing Python

I use the **Anconda** distribution of Python on all my computers. You can download **Anaconda** [here].(https://www.anaconda.com/distribution/)

## Visual Studio Code

[![vscode download page]({static}/posts/django_iot_server/images/vscode_download_page.png)](https://code.visualstudio.com/download)

I have used a couple different code editors including PyCharm, IDLE, notepad, nano, Sublime Text, and Code Writer. But the code editor I reach for most often now is Visual Studio Code. You can download VS Code [here](https://code.visualstudio.com/download).

## PuTTY and FileZilla

PuTTY and FileZilla are two other programs that are useful to have when we develope this Django IoT project. 

[![putty download page]({static}/posts/django_iot_server/images/putty_download_page.png)](https://www.putty.org/)

PuTTY is an SSH termial program that allows you to communicate with a server. PuTTY comes with the PuTTY terminal and a utility called PuTTY Gen. PuTTY Gen makes SSH Keys. We'll use an SSH Key to authenticate (log in) to our server. You can download PuTTY [here](https://www.putty.org/)

[![filezilla download page]({static}/posts/django_iot_server/images/filezilla_download_page.png)](https://filezilla-project.org/download.php?platform=win64)

FileZilla is an FTP program that allows you to move files over to the server. It is possible to code all of the files that will run on the server right in a PuTTY terminal window, but boy would that be slow and painful. An easeir way to accomplish the same thing is to write the code on our local compter, then use FileZilla to copy the files over to the server. You can download FileZilla [here](https://filezilla-project.org/download.php?platform=win64)

## Git and GitHub

We are going to use the verson control tool **Git** and the website GitHub.com to save and store our code. Because I'm using at least four different computers to build this project, it is helpful to have all the code stored in one central place. GitHub also makes it easy to share the code with others.

Next, we are going to actually start the project! The first step is to create a virtual environment.

## Create a Virtual Environment

After the Anaconda distribution of Python is installed, open the Anaconda Prompt and create a virtual environemnt. We'll call our virtual environemnt ```djangoiot```. Note that when the ```djangoiot``` environment is active, you see ```(djangoiot)``` in parenthesis before the prompt.

```text
> conda create -n djangoiot python=3.7
> conda activate djangoiot
(djangoiot)>
```

## Install Django

Next, we'll install Django into our virtual environment. I like to use conda for Python package installation, but you could use pip, pipenv or pipx as well. 

```text
(djangoiot)> conda install django
(djangoiot)> python

>>> import django
>>> django.__version__
'2.1.7'
>>> exit()
```

## Summary

In this post we set up our development environment. This included installing the Anaconda Distribution of Python, installing Visual Studio Code, PuTTY and FileZilla. We also created a virtual environment for the project and installed Django into that environment.

## Next Steps

In the next post, we will set up a GitHub repo and link a folder on our local computer to the repo. In the future each time we edit code for this project. We'll save the changes locally then push the most recent version of the project up to GitHub.
