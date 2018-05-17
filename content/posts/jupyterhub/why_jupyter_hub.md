Title: Why Jupyter Hub?
Date: 2018-05-14 12:40
Modified: 2018-05-14 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: why-jupyter-hub 
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 1
Summary: This is the first part of a multi-part series that shows how to set up **Jupyter Hub** for an engineering programming class. This will be my first time setting up a Jupyter Hub server. I am primarily writing to my future self as I may need to do this again for another class in the future. I hope the lessons learned will help future instructors tackle the same problem if they want to set up Jupyter Hub for their own class or team.

This is the first part of a multi-part series that shows how to set up **Jupyter Hub** for an engineering programming class. This will be my first time setting up a **Jupyter Hub** server. I am primarily writing to my future self as I may need to set up a **Jupyter Hub** server again for a difference class. I hope the lessons learned will also help future instructors tackle the same problem if they want to set up **Jupyter Hub** for their own class or team.

### Why Jupyter Hub?

Why **Jupyter Hub**? I am teaching an intro engineering course this summer. The course has a lab component. Three of the labs are are devoted to computer programming. In previous quarters, I've taught MATLAB for those three labs. But this summer, I would like to try teaching **Python** and cover the same concepts and learning outcomes.

This summer, I would like to spend the three labs in the intro engineering course coding and solving problems. I don't want to spend time during the class downloading Python, creating virtual environments, troubleshooting installs, dealing with system vs. non-system versions of Python, installing packages, dealing with folder structure, explaining the difference between conda and pip, teaching command-line commands, going over Python on Windows compared to Python on MacOSX... 

I would like to see the first programming lab of the quarter run like:

1. There is a .pdf or google doc posted on a shared google drive folder with a link to Jupyter Hub
2. Students click the link and bring up the login page
3. Students log-in with their college usernames and passwords
4. Students type ```import this``` [Shift-Enter] in their first code cell and it just runs.
5. Students can use **Jupyter Hub** from any computer with a web browser and an internet connection.
6. Python code runs the same on all student computers


### This is theoretically possible with Jupyter Hub

**Jupyter Hub** can be installed on a Digital Ocean droplet (a cloud server, like AWS or Google Cloud). The version of **Python** running the notebooks created by **Jupyter Hub** can contain the full **Anaconda** distribution of packages plus some extra packages like **pint** and **pyserial**. All of the notebooks will use the same environment. The installed packages will be the same for each student. One Digital Ocean droplet will be able to run all of the notebooks at the same time (hopefully, there will be about 24 students). Student's work will be saved on the server under their user account. Students can download the .ipynb files and upload them to google drive or save the .ipynb files on a thumb drive. After the students login, folders and notebooks can be in place and used as starting points in lab and as lab exercises. After the course ends, students will still be able to log in and use **Jupyter Hub** and practice writing and running Python code to solve engineering problems.

### What will it take to make Jupyter Hub a reality?

This list will surely change as I go through the process of setting up the **Jupyter Hub** server. Below are the steps I expect to take and software/hardware needed at each step.

1. Sign up for a Digital Ocean Account (already done)
2. Create a new Digital Ocean Droplet (will be called _the server_ from here on out)
3. Connect to the server over SSH and set up SSH keys
4. Create a non-root sudo user on the server
5. Get a public url, hook up the server DNS record to the public URL
6. Install Anaconda on the server
7. Install the other packages on the server like jupyter hub, npm, pyserial, pint
8. Edit permissions of files and directories on the server
9. Create and implement SSL certificates on the server
10. Run Jupyter Hub as non-root sudo user
11. Connect google OAuth to Jupyter Hub
12. Connect to the server as student and celebrate teaching **Python** without worrying about installation and virtual environments.

### Will this work? How much time will it take?

Will this work? I hope so. Other people have done it. There was a JupyterCon talk about it, there are example implementations up on github. A large data science class at UC Berkeley ran **Jupyter Hub**. 

I don't really know how long it will take. The only real step that takes time is the DNS connection. The rest of the steps are in the minute time frame of computing time and probably days if not weeks of troubleshooting time. I'm just going to try and complete a step a day or a step a week and see if I can get the server going by the end of the spring quarter.

### Next Steps:

The next step is really the first step:

Create SSH keys. We'll need a public/private SSH key pair to be able to log into the **Jupyter Hub** server over SSH.