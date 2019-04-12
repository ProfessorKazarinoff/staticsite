Title: Django IoT Server - Part 1 Motivation
Date: 2019-04-12 09:21
Modified: 2019-04-12 09:21
Status: draft
Category: Django
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part1-motivation
Authors: Peter D. Kazarinoff

In this post, I am going to introduce you to a series about building a Django Internet of Things (IoT) server with Python.

[TOC]

## Why am I building a Django IoT Server?

I am building a Django IoT server because of a problem we had this quarter.  There were a bunch of student projects that needed to upload data to an IoT server and download data from an IoT server. This quarter, we used ThingSpeak.com as our IoT server, but there were a couple of problems.

 * ThingSpeak only allows on upload every 15 seconds
 * ThingSpeak accounts require a username and password, students can't use college usernames and passwords.
 * ThingSpeak can't create groups. Multiple users can not have access to the same channel.
 * ThingSpeak doesn't allow strings to be uploaded (it can go in metadata, but not as a channel feed), only numbers can be uploaded.

 Below are the features I would like in an IoT Server

 ## Features needed in the Django IoT Server

  * Students log in to the IoT server with their college usernames and passwords
  * Only college usernames and passwords work
  * Students don't have to set up accounts on the IoT server
  * All plots are shown on the main page
  * Click on a chart on the main page to see the public channel view
  * Each channel can have multiple feeds
  * Each channel can have multiple users
  * Users can add other users to their channels
  * Channels generate API keys
  * Plots update in real-time
  * Plots can show floats or a strings
  * Site looks good on phones and tablets

That is a pretty hefty list of requirements. Previously, I built an IoT server with Flask. That server worked great, but it was only for one user (me), and there was a fixed number of channels. The data shown on the server wasn't updated in real-time. I had to reload the webpage each time I wanted to see the most recent data point. 

## How am I going to accomplish this?

I really don't know. But I like learning new things and building this IoT server will allow me to learn about some Python packages that I don't have a lot of experience with yet, but want to learn. I plan on using Django to build the web server backend and have some sort of database to keep track of users and data uploads. There is going to need to be some sort of REST-like API for students to ping to upload or download data. I am going to have to use web sockets or at least ajax calls to plot data "in real time" (actually once a second is probably quick enough). And the plots will have to update dynamically in some way.

Together this sounds like a pretty complete software project. 

## Which Python packages will I use?

Below is a list of the software and Python packages I think I will use to build out the IoT server. 

 * Python 3.7 - most of the code will be Python code. I use the Anaconda Distribution of Python and the Anaconda Prompt.
 * Virtual environments - I use conda and the Anaconda Prompt to create virtual environments and install packages
 * Django - the website backend will be built with Django
 * Google OAuth2 - authentication (user names and passwords) will be handled by Google. Our college uses the Google Apps suite. I have used Google authentication to run JupyterHub, and it worked great.
 * Django REST framework - the web-API calls to the IoT server will be defined using the Django REST framework
 * A database - hopefully SQlight3 that is built into Python and Django will work. If not, a standard SQL database or in memory database might be needed
 * Plotting front end - don't think this will be Matplotlib, it might be Boquet, Altair, Dash, Plotly or a Javascript plotting library
 * Possibly Django channels to handle the "real-time" communication
 * Nginx and Gunicorn running on Digital Ocean
 * Git and GitHub to store the source code

## What do I want to avoid?

There are a couple of things that I don't want to spend a lot of time doing and don't have a tremendous amount of interest in.

 * Javascript - I'll use someone else's JS code, but I don't really want to write my own. I don't know Javascript very well. I don't want to use a Javascript front-end like Angular or React if I can help it. 
 * Front end styling - I'm just not great at front end design. I plan on using bootstrap and a pre-built theme
 * Making it perfect - The use case is for students to be able to upload data, download data and see data. If there isn't 100% test coverage or a "real" REST interface, that's OK with me.

## How do you build a Django IoT server?

Right now, I don't know. But I think there are going to be a couple of steps. Many of these steps don't have to happen in order, although some steps do depend on others. Below is a possible sequence.

 * Set up the development environment, install Python, create a virtual environment and install Django
 * Create a GitHub repo and link the repo to the computers I use
 * Create a minimal Django website
 * Add a couple pages and some styling to the Django website
 * Deploy the site to Digital Ocean with Nginx and Gunicorn
 * Add user login and logout
 * Add user login with Google OAuth
 * Allow users to add other users to their group
 * Create a simple Web API that allows downloads
 * Add to the Web API so that uploads are possible
 * Create real-time plots
 * Allow for strings as well as numbers to be uploaded
 * Build in some measure of security

That's a whole lot of work, but I think it's possible. I know that at least trying is possible.

## Summary

In this post, I outlined what I want our Django IoT server to be able to do. I discussed some of the tools and technologies I want to use such as Python, Django, and bootstrap. I also touched on some things I don't want to spend a lot of time on such as Javascript and front-end design.

## Next Steps

In the next post, we will review the development environment and set up a GitHub repo. We'll create a Python virtual environment and install Django into it.
