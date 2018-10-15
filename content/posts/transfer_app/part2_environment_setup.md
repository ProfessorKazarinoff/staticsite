Title: Oregon Engineering College Transfer App - Part 2: Development Environment
Date: 2018-10-15 12:40
Modified: 2018-10-15 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-2-development-environment
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 2
Summary: This is the second part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this second post, I'll review the development environment I used to set up and build the web app. This includes installing the Anaconda distribution of Python, creating a GitHub repo, synching a local directory to the GitHub repo, installing packages, starting the project and running the project for the first time.

This is the second part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this second post, I'll review the development environment I used to set up and build the web app. This includes installing the Anaconda distribution of Python, creating a GitHub repo, synching a local directory to the GitHub repo, installing packages, starting the project and running the project for the first time.

#Setting up the development environment

What does that even mean? Before I started building the Oregon College Transfer web app, I needed to make sure the necessary software, packages and settings were in place. This starts with setting up a _development environment_. To me, a development environment is simply the software on a computer that allows me to get work done. In this case the development environment means the tools necessary to build this site. A list of the tools and technologies are below:

1. An operating system: This website was built on machines running Windows 10, Mac OSX and Linux (Ubuntu 16.04 LTS).
2. Python: Python 3.7 (legacy Python is version 2.7)
3. Anaconda: The Anaconda Prompt and the Anaconda Python distribution
4. GitHub.com and git: Four different computers were used build the site. Github is the central place where the most up-to-date version of the site is kept.
5. A virtual environment: A separate Python virtual environment that the web app will run in.
6. Django: a Python web framework
7. Pycharm IDE: a Python Integrated Development that I will use to build and test the web app.
8. Deployment Target: A place for the web app to run. Initially this will be on the Huroku free tier.



## An operating system

I am building the web app on at least four different computers depending on where I am. These computers include:

* Windows 10 Desktop at work

* Mac OSX laptop at home

* Windows 10 laptop at home

* Linux (Ubuntu 16.04 LTS) Desktop at home. 

Regardless of which computer I am using for development, the files that make up the web app will be the same because I'm using Git and GitHub.com to keep everything synced. I will also keep my virtual environments the same on each computer.

An advantage of using the Anaconda distribution of Python is that each of these four computers will have the same stable version of Python. 

Download the latest release at:

[https://www.anaconda.com/download](https://www.anaconda.com/download/)

The Anaconda distribution of Python comes with an up-to-date and stable version of Python (Python 3.6) and the **Anaconda Prompt**. The **Anaconda Prompt** is useful because it allows me to run shell commands on my Windows 10 machine at work. These are the same commands I would run in the terminal on my Mac OSX or Linux boxes. The **Anaconda Prompt** makes creating and logging into virtual environments easy and allows me to use git on Windows 10. Follow this post to [install the Anaconda on Windows 10.]({filename}/posts/installation/installing_anaconda_on_windows.md)

 
### Create a new virtual environment

Before downloading Pelican, we should create a new virtual environment. The same virtual environment on each of the computers I use means the same packages are installed on each computer. To create a new virtual environment, open up the Anaconda Prompt (on Windows) or a terminal (on Linux or Mac OSX). Let's call our new virtual environment **_staticsite_**. The ```conda create``` command creates the environment and the ```-n staticsite``` flag adds the name.

```
$ conda create -n staticsite
```

This creates a new virtual environment called **_staticsite_**. Becuase I use four different computers to work on the site, I need to make sure the same Python packages are installed on each computer. Using a virtual environment ensures this consistency. Once the virtual environment **_staticsite_** is created, we need to activate it and start using it with the command:

On Mac OSX or Linux
```
$ source activate staticsite
```

or on Windows 10
```
activate staticsite
```

We should now see ```(staticsite)``` before the terminal prompt. This means we are using the ```(staticsite)``` virtual environment.

### Install Pelican

Time for some fun! Installing Pelican. Pelican is a Python package that creates static websites. Static sites are websites that only have html, css and javascript. A static site is not connected to a database and there is no code run on the server side. The server just serves static files (html, css, javascript) to the client when the client requests them. In order to install Pelican, we need to install ```pip``` first. On my Linux and Mac OSX machines, the command line tool **git** is already installed. If using Windows 10, **git** may not be available. To keep the development environments the same when using Windows 10, you will also need ```conda``` to ```install git```.


```
(staticsite)$ conda install pip
(staticsite)$ conda install git
```

Once ```pip``` is installed, we can install ```pelican``` and ```markdown```. These are two of the core pieces we need to build the website. ```fabric3``` is also installed because we'll use it to build and demo the site on Windows. ```bs4``` is the beautiful soup package. Some of the pelican plugins to be installed later will depend on ```bs4``` to function properly.

```
(staticsite)$ pip install pelican
(staticsite)$ pip install markdown
(staticsite)$ pip install fabric3
(staticsite)$ pip install bs4
(staticsite)$ pip install ghp-import
```

### Create a github account and create a new repository

While I was making the site, it became clear that I had to keep track of **_version control_**. I would make some changes to the site on my computer at work, then come home and make more changes to the site. Bringing a USB thumb drive back and forth was hard. I would forget the thumb drive at work or home and then could not edit the site. Or worse, I'd edit the site in both places and try to remember which changes were made where and which was the best version. Ah!
 
 The solution is to use **git** and **github**. Git is a command line utility that assists with version control. Using git means changes made to files on one computer can be synced with the same files on another computer. Github.com is the where the site content and settings are remotely stored and integrates easily with git. 

To sign up for a github.com account go here:

[https://github.com/join](https://github.com/join)

The account activation screen looks something like:

![Github.com Join](../images/join_github.png)

Once the account is set up, log in and create a new repository. Use the + button on the upper right-hand menu:

![new github repo](../images/new_github_repo.png)

I named the new repository: **staticsite** and included both a **README.md** and a **GNU General Public License v3.0**. 

![new github repo details](../images/create_a_new_repo_details.png)

### Make a directory for the site and link it to github

Once the github repo (short for repository, basically a folder with files on github.com) is set up, the last step to complete the development environment is to link the remote repo on github to the local version of the site on my computer. 

The local version is in a folder call ```staticsite``` in the ```Documents``` folder. The ```staticsite``` folder will contain all the files used to build the site and the output files created by Pelican that _are_ the site.

```
(staticsite)$ cd ~
(staticsite)$ cd Documents
(staticsite)$ mkdir staticsite
(staticsite)$ cd staticsite
```

We can set up git to keep the contents of the local staticsite folder in sync with the contents of the staticsite repo on github.com. The command ```git init``` will initiate or create the local repository. The command ```git remote add origin``` followed by the url of our github repo links local folder to the remote repo on github. Note the web address ends in ```.git```. If you are following along and want to build your own static site, make sure to change ```username``` to your github username and ```reponame``` to your github repo name.

```
git init
git remote add origin https://github.com/username/reponame.git
```

Now for the git magic. On github.com we have a README.md file and a licence. But the local staticsite folder on the computer is empty. So the two folders aren't in sync. To make the contents of each folder identical, we **_pull_** the files from github onto the local computer. A **_pull_** "pulls" or gets the files from github and copies them to the local staticsite folder.

```
(staticsite)$ git pull origin master
```

If you look in the local staticsite folder you should now see the following two files:

```
staticsite
├── LICENSE
├── README.md
```

The development environment is set! On to building the site!

Now each time I work on the site, I navigate to the **staticsite** folder on whatever computer I am using. Before any editing, I key in the command:

```
git pull origin master
```

After the _pull_, the staticsite folder is up-to-date with the newest version of all the files on github. Then I go about editing files, writing posts, changing settings, etc. After the edits, the last thing I do before shutting down the computer for the day is add all the changes to git with ```git add .``` (note there is a space between the ```add``` and the period ```.```). Then commit those changes locally with the line ```git commit -m "commit message"``` (note there are double quotes ```"commit message"``` used around the commit message), and finally push the changes up to github.com with ```git push origin master```. Now the version of the site up on github.com is the same as the version of the site on my local machine.

```
git add .
git commit -m "commit message"
git push origin master
```

This ensures all of my computers and the github repo contain the same version of the site.


In the [next post]({filename}how_I_built_this_site2.md) we will use the ```pelican-quickstart``` command to get the blog off the ground, write our first post and view a demo version of the site.