Title: Deploy a Jupyter Notebook Online with Voila and Heroku
Date: 2020-01-27 09:01
Modified: 2020-01-27 09:01
Status: draft
Category: jupyter
Tags: python, jupyter, jupyter notebook, voila, heroku, deploy
Slug: deploy-jupyter-notebook-voila-heroku
Authors: Peter D. Kazarinoff

[![Voila Logo]({static}/posts/voila/images/voila_logo.png)]({file}/posts/voila/voila_app_deployment.md)

Jupyter notebooks are a great way to write and run Python code. Jupyter notebooks can produce plots and animatons.  Static Jupyter notebooks can be shared on GitHub.com and [nbviewer](https://nbviewer.jupyter.org/). A great Python package called [Voila](https://voila.readthedocs.io/en/stable/) turns Jupyter notebooks into deployable web apps. In this post, you'll learn how to deploy a Jupyter notebook as a cloud-based web app with Voila and Heroku.

[TOC]

# Voila

**What is Voila?** Voila is a Python package that turns Jupyter notebooks into working web sites. It is pretty amazing. Another Python package called Streamlit turns .py-files into websites. Voila does the same thing for Jupyter notebooks.

Any Jupyter notebook can be turned into a website with Voila. Voila is specifically useful for turning Jupyter notebooks with embedded widgets into working websites.

# Install Voila and Jupyter

Before we start writing any code, we need to install Voila and Jupyter. These packages can be installed using a terminal. In our example, we are also going to use NumPy and Matplotlib. The commands below show a virtual environment created with Python's built-in **venv** module. You could also create a virtual environment with **conda**.

```text
mkdir voila
cd voila
python -m venv venv
souce venv/bin/activate
pip install voila
pip install jupyter numpy matplotlib
```

Next, open a Jupyter notebook.

```text
jupyter notebook
```

# Create a Jupyter notebook with Widgets

Before we can deploy our Jupyter notebook as a cloud-based web app, we need write a few cells in our Jupyter notebook. Any markdown cells will become text in on our website. Any plots or widgets will also become part of our website. Code cells can be used in our website, but the code cells will not be seen by our website's visitors. 

Our Jupyter notebook needs to start with a couple import lines. Note that we don't need to import Volia into the notebook that will _become_ the website. We just need to install Voila into the environment that will _deploy_ the website.

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

Below the imports, enter the code below into a code cell. The code creates an interactivate plot of the sine function using Jupyter notebook widgets. 

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

# Test Voila locally

Next, we can test our website running on our local machine.

```text
voila app.ipynb
```

# Deploy Voila app on Heroku

## Create three files

Next we will create three files required by Heroku

 * ```requirments.txt```
 * ```runtime.txt```
 * ```Procfile```

### requirements.txt

Create a requirments.txt file with **pip**. The requirements.txt file tells Heroku which Python packages to install to run our app.

```text
pip freeze > requirements.txt
```

### runtime.txt

The runtime.txt file specifies the version of Python we want Heroku to use. Create a new file called ```runtime.txt```. Inside the file, just one line of text is needed.

```text
python-3.7.6
```

### Procfile

The last required file for our Heroku deployment is a Procfile. This file includes the instructions for Heroku to deploy our Voila app. Create a new file named ```Procfile``` (no extension) and include the text below.

```text
web: voila —-port=$PORT —-no-browser app.ipynb
```

## Install the Heroku CLI

## Create git repo

### Create repo on GitHub.com

### Add, commit and push local files

```text
git init
git remote add origin https://github.com/<usename>/<reponame>
git add .
git commit -m "initial commit"
git push origin master
```

## Push to Heroku

```text
heroku create voila_app
git push heroku master
```

# View Website online

# Summary

In this post, we created a website from a Jupyter notebook using Voila.
