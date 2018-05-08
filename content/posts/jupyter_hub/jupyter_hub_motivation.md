Title: Why Jupyter Hub?
Date: 2018-05-07 12:40
Modified: 2018-05-07 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: why-jupyter-hub
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 1
Summary: This is the first part of a multi-part series that show how to set up Jupyter Hub for a class. This will be the first time setting up a Jupyter Hub server for me, I am primarily writing to my future self as I may need to do this again in the future. I hope the lessons learned will help future instructors tackle the same problem.

This is the first part of a multi-part series that show how to set up Jupyter Hub for a class. This will be the first time setting up a Jupyter Hub server for me, I am primarily writing to my future self as I may need to do this again in the future. I hope the lessons learned will help future instructors tackle the same problem.

### Why Jupyter Hub?

Why Jupyter Hub? I am teaching an intro engineering course this summer. The course has a lab component and three of the labs are are devoted to computer programming. I have taught MATLAB during those three labs, but I would like to try Python and cover the same content.

I would like to spend the lab time coding and solving problems. I don't want to spend time in lab downloading Python, creating virtual environments, troubleshooting installs, dealing with system vs. non-system versions of Python, installing packages, dealing with folder structure, teaching command-line commands...

As a goal, I would like to see the first programming lab of the quarter to
1. There is a pdf or google doc posted on a shared google drive folder with a link to Jupyter Hub
2. Students click the link and bring up the login page
3. Students log-in with their college usernames and passwords (or maybe Github usernames and passwords)
4. Students type ```import this``` [Shift-Enter] and their first code cell runs.


### This is theoretically possible with Jupyter Hub

Jupyter Hub can be installed on a Digital Ocean droplet. The version of Python running the notebooks can be the full Anaconda distribution plus some extras like **Pint** and **pyserial**. One Digital Ocean droplet will be able to run all of the notebooks at the same time. Student's work will be saved on the server under their user account. Students can download the .ipynb files and upload them to google drive. There can be folders and notebooks already in place that can be used as starting points in lab and as lab exersizes.

### What will it take to make Jupyter Hub a reality

This list will surely change as I go through the process of setting the server up. Below are the steps I expect to take and software/hardware needed at each step.

1. Sign up for a Digital Ocean Account (already done)
2. Create a new Digital Ocean Droplet (will be called _the server_ from here on out)
3. Connect to the server over SSH and set up SSH keys
4. Create a non-root sudo user
5. Get a public url, hook up the server DNS record to the public URL
6. Install Anaconda on the server
7. Install the other packages on the server like jupyter hub, npm, pyserial, pint
8. Symlinks and permissions of files on the server
9. Create and implement SSL certificates on server
10. Run Jupyter Hub as non-root sudo user
11. Connect OAuth to Jupyter Hub
12. Connect to Server as student

### Will this work? How much time will it take?

Will this work? I hope so. Other people have done it. There was a jupytercon talk about it. They did it at UCBerlkey. I don't really know how long it will take. The only real step that takes time is the DNS connection. The rest of the steps are in the minute time frame. I'm just going to try and do a step a day or a step a week and see if I can get the server going by the end of the quarter.

### Next Steps:

The next steps are really the first steps:

1. Sign up for a digital Ocean account

2. Create a new Digital Ocean Droplet

3. Create a non-root sudo user