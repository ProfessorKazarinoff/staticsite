Title: Deploy a Jupyter Notebook Online with Voila and Heroku
Date: 2019-12-24 09:01
Modified: 2019-12-24 09:01
Status: draft
Category: jupyter
Tags: python, jupyter, jupyter notebook, voila, heroku, deploy
Slug: deploy-jupyter-notebook-voila-heroku
Authors: Peter D. Kazarinoff

Jupyter notebooks are a great way to write Python code and view the results of that code, like plots and animatons. Static Jupyter notebooks can be shared on GitHub and nbviewer. A great Python package called Voila turns Jupyter notebooks into deployable web apps. In this post, you will see how to deploy a Jupyter notebook as a cloud-based web app with Voila and Heroku.

[TOC]

# Voila

**What is Voila?** Voila is a Python package that turns Jupyter notebooks into working web sites. It is pretty amazing. Another Python package called Streamlit turns .py-files into websites. Voila does the same thing for Jupyter notebooks. Any Jupyter notebook can be turned into a web site with Voila. Voila is specifically useful for turning Jupyter notebooks with embedded widgets into working websites.

# Install Voila and Jupyter

Before we start writing any code, we need to install Voila and Jupyter. These packages can be installed using a terminal. 

```text
mkdir voila
cd voila
python -m venv venv
souce venv/bin/activate
pip install voila
pip install jupyter numpy matplotlib
```

Next, open a Jupyter notebook

```text
jupyter notebook
```

# Create a Jupyter notebook with Widgets

Before we can deploy our Jupyter notebook as a cloud-based web app, we need write a few cells in our Jupyter notebook. Any markdown cells will become text in on our website. Any plots or widgets will also become part of our website. 

Our Jupyter notebook needs to start with a couple import lines. Note that we don't need to import Volia into the notebook that will become the website. We just need to install Voila into the environment that will deploy the website.

```python
import numpy as np
import matplotlib.pyploat as plt
%matplotlib inline
```

Next, we can enter some header text into a markdown cell.

```text
# Voila Web App

## A website built out of a Jupyter notebook using Voila
```

Below the markdown cell, enter the code below into a code cell. The code creates an interactivate plot of the sine function using Jupyter widgets. 

```python

```

# Test Voila locally

```text
voila app.ipynb
```

# Deploy Voila app on Heroku

## Create three files

Next we will create three files required by Heroku

 * ```requirments.txt```
 * ```runtime.txt```
 * ```Profile```

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

### Profile

The last required file for our Heroku deployment is a Procfile. This file includes the instructions for Heroku to deploy our Voila app. Create a new file named ```Profile``` (no extension) and include the text below.

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

In this post,
