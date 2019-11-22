Title: How to Build a Streamlit App in Python
Date: 2019-11-20 08:11
Modified: 2019-11-20 08:11
Status: published
Category: Python
Tags: streamlit, matplotlib, engineering
Slug: how-to-build-a-streamlit-app
Authors: Peter D. Kazarinoff

Streamlit is an app-building framework for Python. Steamlit is a way to create mostly simple single-page web apps that are easy to deploy. Streamlit is usefull for engineers and data scientists who have some app functionality, like a plot that dynamically changes based on user interaction, but don't want to build out a full website using a tool like Django or Flask.

Streamlit builds web-apps from a single Python file. Only a couple additional lines of code are needed to turn a Python ```.py``` file into a web-app using Streamlit.

## Installing Steamlit

Streamlit can be installed with **pip** the Python package manager. It's a good idea to install Streamlit into a virtaul environment, rather than installing Streamlit into the base or built-in version of Python installed on your machine. I use the **Anaconda Prompt** to create virtual environments. The commands below are designed to run on the **Anaconda Prompt** and will create a virtual environment called ```(streamlit)``` and install the Streamlit package into that environment. Note that at the time of writing, Streamlit can not be installed with **conda**, it must be installed with **pip**. 

```text
conda create -y -n streamlit python=3.7
conda activate streamlit
pip install streamlit
```

Once Streamlit is installed, you can confirm your installation by opening up the Python REPL and typing the commands below:

```text
import streamlit
streamlit.__version__
```

## Running Streamlit for the First Time

## Creating a very simple Streamlit App

## Creating a Mohr's Circle Streamlit App

## Deploying on Heroku

Sign up for a Heroku account. 

Use Windows Subsystem for Linux (WSL) to install the Heroku CLI

```
sudo apt-get -y update && sudo apt-get -y upgrade
curl https://cli-assets.heroku.com/install.sh | sh
source .bashrc
```

Create a virtual environment, install packages and save a requirements.txt file

```
conda create -n mohrs_circle python=3.7
conda activate mohrs_circle
python -m pip install streamlit bokeh numpy
pip freeze > requirements.txt
```

Test and make sure the streamlit app runs

```
streamlit run streamlit_app_bokeh.py
```

Save all the changes to Git

```
git add .
git commit -m "add Heroku Profile setup.sh requirements.txt"
git push origin master
```

Create a Procfile and a setup.sh file

In Profile (the file name is Profile with a capital P and no file extension)

```
web: sh setup.sh && streamlit run streamlit_app_bokeh.py
```

In setup.sh

```
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

Now in the project directory the following files should be present:

```
mohrs_circle/
├── LICENSE
├── Procfile
├── README.md
├── requirements.txt
├── setup.sh
├── streamlit_app.py
├── streamlit_app_bokeh.py
├── test.py
└── user_funcs.py
```

Commit all the files and push to GitHub

```
git add .
git commit -m "add Profile, setup.sh, requirements.txt"
```


Log into Heroku with the Heroku CLI, create the Heroku project and push to Heroku


```
heroku login
heroku create
git push heroku master
# see if it's running
heroku ps:scale web=1
```

Check the URL provided by the Heroku CLI

## Summary

In this post, we created an app with streamlit and deployed it on Heroku

## Next Steps
