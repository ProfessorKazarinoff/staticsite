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

## Summary

## Next Steps
