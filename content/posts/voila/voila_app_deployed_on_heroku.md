Title: Deploy a Jupyter Notebook Online with Voila and Heroku
Date: 2020-01-28 09:01
Modified: 2020-01-28 09:01
Status: draft
Category: jupyter
Tags: python, jupyter, jupyter notebook, voila, heroku, deploy
Slug: deploy-jupyter-notebook-voila-heroku
Authors: Peter D. Kazarinoff

[![Voila Logo]({static}/posts/voila/images/jupyter_voila_heroku.png)]({file}/posts/voila/voila_app_deployment.md)

Jupyter notebooks are a great way to write and run Python code. Jupyter notebooks can produce plots and animations. Static Jupyter notebooks can be shared on GitHub.com and [nbviewer](https://nbviewer.jupyter.org/). A great Python package called [**Voila**](https://voila.readthedocs.io/en/stable/) turns Jupyter notebooks into deployable web apps. In this post, you'll learn how to deploy a Jupyter notebook as a cloud-based web app with Voila and Heroku.

# Prerequisites

This tutorial assumes you have Python installed on your local computer. I recommend installing the [Anaconda distribution of Python](https://anaconda.com/distribution) Version 3.7, but you can also install Python from [Python.org](https://python.org) or the Windows Store. It is also assumed that you either have Windows Subsystem for Linux (WSL) installed or you are using MacOS or Linux itself. I recommend Ubuntu 18.04 LTS for your Linux distribution. You should also be able to bring up a terminal in your prefered operating system and be able to use some basic terminal commands such as ```cd``` to change directories, ```mkdir``` to make a new directory ```pwd``` to list the contents of a directory and ```cd ..``` to go back a directory.

[TOC]

# Voila

<<<<<<< HEAD
**What is Voila?** Voila is a Python package that turns Jupyter notebooks into working web sites. It is pretty amazing. Another Python package called Streamlit turns .py-files into websites. Voila does the same thing for Jupyter notebooks.

Any Jupyter notebook can be turned into a web site with Voila. Voila is specifically useful for turning Jupyter notebooks with embedded widgets into working websites.
=======
[![Voila Logo]({static}/posts/voila/images/voila_logo.png)](https://voila.readthedocs.io/en/latest/)

**What is Voila?** Voila is a Python package that turns Jupyter notebooks into working web sites. It is pretty amazing. Another Python package called Streamlit turns .py-files into websites. Voila does the same thing for Jupyter notebooks.

 > A link to the Voila docs is below:
 [https://voila.readthedocs.io/en/stable/](https://voila.readthedocs.io/en/stable/)

Any Jupyter notebook can be turned into a website with Voila. Voila is specifically useful for turning Jupyter notebooks with embedded widgets into working websites.
>>>>>>> 055cb290c50391f03e3029af580412208160010f

# Install Voila and Jupyter

Before we start writing any code, we need to install Voila and Jupyter. These packages can be installed using a terminal. In our example, we are also going to use NumPy and Matplotlib. The commands below show a virtual environment created with Python's built-in **venv** module. You could also create a virtual environment with **conda**.

```text
mkdir voila
cd voila
python -m venv venv
source venv/bin/activate
pip install voila
pip install jupyter numpy matplotlib
```

Next, open a Jupyter notebook.

```text
jupyter notebook
```

# Create a Jupyter notebook with Widgets

![Jupyter Logo]({static}/posts/voila/images/jupyter_logo.png)

<<<<<<< HEAD
Our Jupyter notebook needs to start with a couple import lines. Note that we don't need to import Volia into the notebook that will become the website. We just need to install Voila into the environment that will _deploy_ the website.
=======
Before we can deploy our Jupyter notebook as a cloud-based web app, we need to write a few cells in our Jupyter notebook. Any markdown cells will become text in on our website. Any plots or widgets will also become part of our website. Code cells can be used on our website, but the code cells will not be seen by our website's visitors. 
>>>>>>> 055cb290c50391f03e3029af580412208160010f

Our Jupyter notebook needs to start with a couple of import lines. Note that we don't need to import Volia into the notebook that will _become_ the website. We just need to install Voila into the environment that will _deploy_ the website.

At the top of the Jupyter notebook, enter some header text into a markdown cell.

```text
# Voila Web App

## A website built out of a Jupyter notebook using Voila
```

Below the markdown cell in the notebook, enter the import lines below into a code cell. These lines of code import NumPy, Matplotlib and Jupyter notebook widgets.

```python
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive
%matplotlib inline
```

Below the imports, enter the code below into a code cell. The code creates an interactive plot of the sine function using Jupyter notebook widgets. 

```python
def plot_func(a, f):
    plt.figure(2)
    x = np.linspace(0, 2*np.pi, num=1000)
    y = a*np.sin(1/f*x)
    plt.plot(x,y)
    plt.ylim(-1.1, 1.1)
    plt.title('a sin(f)')
    plt.show()

interactive_plot = interactive(plot_func, a=(-1,0,0.1), f=(0.1, 1))
output = interactive_plot.children[-1]
output.layout.height = '300px'
interactive_plot
```

Run the code cell and play with the sliders and see the plot change. The sliders should change the frequency and amplitude of the sine wave.

![Jupyter notebook with widget]({static}/posts/voila/images/jupyter_notebook_widget_app.png)

# Test Voila locally

Next, we can test our website running on our local machine. Close the Jupyter notebook and make sure the environment where voila is installed and activate. Type the command below into a tutorial to bring up the app locally. Note how we don't see the code in the code cells, we just see the markdown cells, sliders and plot.

```text
voila app.ipynb
```

![Jupyter notebook with widget]({static}/posts/voila/images/voilia_running_locally.png)

Great! The Voila app works locally and we can move the sliders and see the plot change, just like in the Jupyter notebook. So... next we need to deploy this app online so that other people can see it.

# Deploy Voila App on Heroku

We are going to deploy the app on Heroku. Heroku is a service to host webapps that takes care of the server administration for you. You can deploy Flask or Django apps on Heroku. We can also deploy our Voila app on Heroku. Luckily, Heroku has a free tier- so you can try out deploying Voilia online without having to shell out any money.

![Heroku Logo]({static}/posts/voila/images/heroku_logo.png)

A couple steps need to be completed before we deploy our app on Heroku.

## Create Three Files

The first step to deploying the web app is to create three files required by Heroku. The three required files are:

 * ```requirements.txt```
 * ```runtime.txt```
 * ```Procfile```

### requirements.txt

Create a ```requirements.txt``` file with **pip**. The ```requirements.txt``` file tells Heroku which Python packages to install to run our web app.

```text
pip freeze > requirements.txt
```

### runtime.txt

The ```runtime.txt``` file specifies the version of Python we want Heroku to use. Create a new file called ```runtime.txt```. Inside the file, just one line of text is needed:

```text
python-3.7.6
```

### Procfile

<<<<<<< HEAD
The last required file for our Heroku deployment is a Procfile. This file includes the instructions for Heroku to deploy our Voila app. Create a new file named ```Procfile``` (no extension) and include the text below.
=======
The last required file for our Heroku deployment is a ```Procfile```. This file includes the instructions for Heroku to deploy our Voila app. Create a new file named ```Procfile``` (no extension) and include the text below:
>>>>>>> 055cb290c50391f03e3029af580412208160010f

```text
web: voila —-port=$PORT —-no-browser app.ipynb
```

We need to use the Heroku command line interface (CLI) to deploy our app.

## Install the Heroku CLI

The Heroku CLI (command line interface) is the way we are going to deploy the app online. I had the most success installing the Heroku CLI on Linux, MacOS or WSL (Windows Subsystem for Linux). I had trouble installing the Heroku CLI on regular Windows 10.

## Create git Repo

Because we need to use WSL to use the Heroku CLI, we have to move the whole project into the proper WSL folder. You could move it over manually using the Windows file browser, but the way I did it was to save the project on GitHub and then pull the project down from GitHub.com in WSL using git.

### Create repo on GitHub.com

Log into GitHub.com and create a new repo. I always add a readme, ```.gitignore```, and a license. 

![Heroku Logo]({static}/posts/voila/images/github_add_new_repo.png)

![Heroku Logo]({static}/posts/voila/images/github_add_dot_gitignore.png)

![Heroku Logo]({static}/posts/voila/images/github_copy_url.png)

Make sure to copy the GitHub URL from the repo to make the next step easier.

### Add, commit and push local files to GitHub

Next, back on your local machine, move into the main project directory that contains the ```app.ipynb``` file. Use the commands below to create a local git repo and add the newly created GitHub.com repo as a remote. Add all the files in the directory, commit and push up to Github.

```text
git init
git remote add origin https://github.com/<usename>/<reponame>
git add .
git commit -m "initial commit"
git push origin master
```

## Pull the Repo down into WSL

Now that the repo is up on GitHub.com, we can pull it down into WSL where the Heroku CLI is installed. Back in the Windows Subsystem for Linux terminal, type the following commands.

```text
mkdir voila
cd voila
git init
git remote add origin https://github.com/<usename>/<reponame>
git pull origin master
```

After you pull the repo down from GitHub, the follwoing files should be present.

```text
.
├── LICENSE
├── Procfile
├── README.md
├── app.ipynb
├── requirements.txt
└── runtime.txt
```

Now we can push the project up to heroku.

## Push to Heroku

After the files are pushed to GitHub, we are almost done. All that's left is to push the files to Heroku and view our live web app.

```text
heroku create
```
Output will look something like below:

```text
Creating app... done, ⬢ damp-cove-01735
https://damp-cove-01735.herokuapp.com/ | https://git.heroku.com/damp-cove-01735.git
```

Last thing to do is push the changes to Heroku to publish our app.

```
git push heroku master
```

The first time the command is run, it will take a little time. 

# View the Web App Online

![Image Desc]({static}/posts/voila/images/jupyter_voila_heroku.png)

# Summary

In this post, we created a website from a Jupyter notebook using Voila. First we created a Jupyter notebook with an interactive widget. Then we ran Voila locally and saw a preview of what the app would look like online. Lastly we published the app on Heroku using the Heroku CLI. Thanks to all the maintainers of Voila. It is a wondeful package.
