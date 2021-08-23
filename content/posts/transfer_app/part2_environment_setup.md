Title: Oregon Engineering College Transfer App - Part 2: Development Environment
Date: 2020-08-23 12:40
Modified: 2020-08-23 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-2-development-environment
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 2
Summary: This is the second part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this second post, we'll review the development environment used to set up and build the web app. This includes installing the Anaconda distribution of Python, creating a GitHub.com repo, synching a local directory to the repo on GitHub, creating a virtual environment, installing packages, starting the project and running the project for the first time.

This is the second part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this second post, we'll review the development environment used to set up and build the web app. This includes installing the Anaconda distribution of Python, creating a GitHub.com repo, synching a local directory to the repo on GitHub, creating a virtual environment, installing packages, starting the project and running the project for the first time.

# Setting up the development environment

What does that even mean? Before we start building the Oregon College Transfer web app, we needed to make sure the necessary software, packages and settings were in place. This starts with setting up a _development environment_. To me, a development environment is the software on a computer that allows me to get work done. In this case the development environment means the tools necessary to build the website. A list of the tools and technologies are below:

1. An operating system: This website is going to be built on machines running Windows 10
2. Python: Python 3.9.6 is the most recent version of Python at the time of writing
3. Anaconda: The Anaconda Prompt and the Anaconda Python distribution
4. GitHub.com and git: We are going to save the code we write on GitHub.com and push the code up to Github using the command-line tool **git**.
5. A virtual environment: A separate Python virtual environment that the web app will run in.
6. Django: a Python web framework
7. VS Code: a Python code editor to build and test the web app.
8. Deployment Target: A place for the web app to run. Initially this will be on the Huroku free tier. Eventually we may run the website on a Digital Ocean droplet or on an AWS EC2 instance. 

## An operating system

I am building the web app on at least three different computers depending on where I am. These computers include:

* Windows 10 Work Laptop

* Windows 10 Personal Laptop

* Linux (Ubuntu 20.04 LTS) Desktop at home. 

Regardless of which computer I am using for development, the files that make up the web app will be the same because I'm using git and GitHub.com to keep everything synced. I will also keep my virtual environments the same on each computer.

## Python and Anaconda

Python is a programming language. The Anaconda distribution of Python is a software download that includes the Python programing language and a couple other software tools. For this project, the Anaconda Prompt that comes with Anaconda is going to be used to set up the virtual environment.

Download the latest release of Anaconda at:

[https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)

The Anaconda distribution of Python comes with an up-to-date and stable version of Python and the **Anaconda Prompt**. The **Anaconda Prompt** is useful because it allows me to run shell commands on Windows 10 machines. These are the same commands I would run in the terminal on my Linux desktop. The **Anaconda Prompt** makes creating and activating virtual environments easy and allows me to use git on Windows 10. Follow this post to [install the Anaconda on Windows 10.]({static}/posts/installation/installing_anaconda_on_windows.md)

 
## Create a new virtual environment

It is best practice to create and use a seperate virtual environment for each Python project. To create a new virtual environment, open up the Anaconda Prompt (on Windows) or a terminal (on Linux or MacOS). Let's call our new virtual environment **_transfer-app_**. The ```conda create``` command creates the environment and the ```-n staticsite``` flag adds the name.

```text
> conda create -n transfer-app python=3.9
```

Note that the ```>``` character should not be typed into the Anaconda Prompt. The ```>``` character is used to show the Anaconda Prompt, not a character for you to type.

The command above creates a new virtual environment called **transfer-app**. Once the virtual environment **_transfer-app_** is created, we need to activate it and start using it with the command below:

```text
conda activate transfer-app
```

We should now see ```(transfer-app)``` before the terminal prompt. This means we are using the ```(trasfer-app)``` virtual environment.

### Install Django

Time for some fun! Installing Django. Django is a Python package that builds websites. Django is called a _web framework_. A web framework is a software package that scaffolds a website. Django is one of the most popular web frameworks for Python. Another popular webframework for Python is called **Flask**. Django is considered more opinionated that Flask and comes with more things included than Flask does.

```
(transfer-app)$ conda install django
```

We can make sure that Django is installed by opening up the python REPL from the Anaconda Prompt and seeing if we can import Django and invoke the ```.__version__``` atribute that is often defined for popular Python packages.

```
(transfer-app)$ python
>>> import django
>>> django.__version__

```

### Create a GitHub.com account and create a new repository

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


In the [next post]({static}/posts/how_i_built_this_site/how_I_built_this_site2.md) we will use the ```pelican-quickstart``` command to get the blog off the ground, write our first post and view a demo version of the site.