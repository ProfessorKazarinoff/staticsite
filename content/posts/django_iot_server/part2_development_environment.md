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

## What is a Development Environment

What does _development environment_ even mean? Before we started building the IoT server, we needed to make sure the necessary software, packages, and settings were in place. This begins with setting up a development environment. 

 > A development environment is merely the software on a computer that allows me to get work done. 
 
 In this case, the development environment includes the tools necessary to build the server.

## Computer and Operating System

I have a couple different computers that I'm going to use to build the Django IoT server. Below is a list of the machines I'll use to build the Django IoT server. I want to make sure that I have the same Python packages installed on each computer and make sure that the version of the Django IoT server is the same accross all of these machines.

 * Windows 10 Desktop at work

I have a Windows 10 Desktop at work with two monitors. One limitation is that I don't have administrator access on my desktop at work, so I can't install new programs

 * Windows 10 Laptop at home

My main laptop at home is an old Windows 10 machine. The screen suround is comming off, the battery doesn't last very long and the speakers don't always work. But for developing a Django IoT server, this works fine. 

 * MacOS Laptop at home

My wife has a MacBook Air at home. It is pretty old, but still humming along. Compared to the Windows 10 computers I use, the MacOS operating system is a little easier to write code on. MacOS has the _terminal_. This little program is helpful when working with **Git**, remote servers over SSH. On Windows 10, the substitue is the **Anaconda Prompt** instead of the MacOS terminal. 

 * Ubuntu Desktop at home

I have a Desktop computer at home that run the Ubuntu operating system. Ubuntu is a popular Linux distribution. Like MacOS, Ubutu comes with a termial program. 

## Installing Python

I use the **Anconda** distribution of Python on all my computers. You can download **Anaconda** [here].(https://www.anaconda.com/distribution/)

## Visual Studio Code

[![vscode download page]({filename}/posts/django_iot_server/images/vscode_download_page.png)](https://code.visualstudio.com/download)

I have used a couple different code editors. These editors include PyCharm, IDLE, notepad, nano, Sublime Text, and Code Writer. But the one I reach for most often is Visual Studio Code. You can download VS Code [here](https://code.visualstudio.com/download).

## PuTTY and FileZilla

PuTTY and FileZilla are two other programs that will help with this Django IoT project. 

[![putty download page]({filename}/posts/django_iot_server/images/putty_download_page.png)](https://www.putty.org/)

PuTTY is an SSH termial program that will allow us to communicate with our server during development. PuTTY comes with the PuTTY terminal and a utility called PuTTY Gen. PuTTY Gen makes SSH Keys. We'll use an SSH Key to Authenticate with our server. You can download PuTTY [here](https://www.putty.org/)

[![filezilla download page]({filename}/posts/django_iot_server/images/filezilla_download_page.png)](https://filezilla-project.org/download.php?platform=win64)

FileZilla is an FTP program that will allow us to move files over to the server. It is possible to code all of the files that will run on the server right on the server in a PuTTY window. But an easeir way to accomplish the same thing is to write the code on our local compter, then use FileZilla to copy the files over to the server. You can download FileZilla [here](https://filezilla-project.org/download.php?platform=win64)

## Create a Virtual Environment



## Install Django

## Summary

This post explained what we need to don

## Next Steps

In the next post, we will review the development environment, set up a GitHub repo and create a virtual environment.