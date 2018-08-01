Title: A single page Flask App to show data from ThingSpeak.com
Date: 2018-07-20 09:01
Modified: 2018-07-20 09:01
Status: Draft
Category: flask
Tags: python, flask, thingspeak, mobile
Slug: flask-app-show-data-from-thingspeak
Authors: Peter D. Kazarinoff
Summary: In this post, I'll run through how I set up a single page flask app that shows a temperature posted on ThingSpeak.com. ThingSpeak has nice looking graphs, but it is actually kind of hard to see the value of individual data points. I wanted to be able to see the most recent temperature point recorded by my [ESP8266 WiFi weather station]({filename}/posts/micropython/micropython_upload_code.md) on a phone or tablet. By building a flask app and hosting it on Digital Ocean, I can now view the current temperature from anywhere.

In this post, I'll run through how I set up a single page flask app that shows a temperature posted on ThingSpeak.com. ThingSpeak has nice looking graphs, but it is actually kind of hard to see the value of individual data points. I wanted to be able to see the most recent temperature point recorded by my [ESP8266 WiFi weather station]({filename}/posts/micropython/micropython_upload_code.md) on a phone or tablet. By building a flask app and hosting it on Digital Ocean, I can now view the current temperature from anywhere.

[TOC]

## Set up a new Digital Ocean Droplet

The flask app needs a server to run on. I choose Digital Ocean as my cloud server provider. After creating a new server, it is best practice to create a non-root sudo user.

### Create a New Droplet

The [**flask**](http://flask.pocoo.org/docs/1.0/) single page web app will be hosted on [Digital Ocean](https://www.digitalocean.com/). Digital Ocean is hosts virtual private servers that run in the cloud. Setting up a server on Digital Ocean is pretty cheap ($5/month) and quick. I host [my **Jupyter Hub** server]({filename}//posts/jupyterhub/why_jupyter_hub.md} on Digital Ocean so I am also more familiar with spinning up their servers compared to Linode, AWS or other cloud providers.

Creating a new Digital Ocean cloud server, called a _Droplet_ in Digital Ocean speak involves creating a new account on Digital Ocean, logging in and selecting **Create --> Droplets** in the upper right menu.

![DO create new droplet]({filename}/posts/flask/DO_create_new_droplet.PNG)

For the Droplet options I choose:

 * Ubuntu 18.04.1 x64
 * Size: Memory 1G, SSD 25 GB, Transfer 1 TB, Price $5/mo
 * Datacenter Region: San Fransisco 2
 * Additional Options: None
 * SSH keys: **Added all of [my saved SSH keys]({filename}/posts/jupyterhub/PuTTYgen_ssh_key.md). You need this to log into the server with PuTTY**

Create the server with the big green **Create** button.

After the Droplet is created, note the IP address of the server. You'll need the IP address for the next step.

### Login and create a non-root sudo user

Our first interaction with the server is to log in as root. Then we'll create a non-root sudo user to interact with the server from here on out.

Open PuTTY and log onto the server as root. See a [previous post]({filename}/posts/jupyterhub/new_DO_droplet.md}) on how to set up PuTTY to log in as root.

### Copy SSH keys to non-root sudo user

## Aquire a domain name

### Purchase a domain name

### Point DNS severs at Digital Ocean

### Point domain name to Digitial Ocean Droplet

## Build the Flask App

### Install Packages

Before the single page flask app can be built, a number of packages need to be installed on the server.

```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt install python3-pip python3-dev python3-setuptools python3-venv
$ sudo apt-get install build-essential libssl-dev libffi-dev 
```

### Create a Virtual Environment and install **flask**

Once the necessary libraries are installed, I created a virtual environment to run the flask app. I usually use **conda** to create virtual environment, but since I'm not using the Anaconda distribution of Python, **venv** will have to do instead.

```bash
$ cd ~
$ mkdir flaskapp
$ cd flaskapp
$ python3.6 -m venv flaskappenv
$ source flaskapp/bin/activate
```

With the virtual environment activated, I installed flask, wheel, uwsgi and requests with **pip**

```bash
(flaskappenv)$ pip install wheel
(flaskappenv)$ pip install flask
(flaskappenv)$ pip install uwsgi
(flaskappenv)$ pip install requests
```

### Building the first simple flask app

With the Python packages installed, next I build a very simple version of the flask app and viewed it in a web browser using the IP address of the DO droplet.

```bash
(flaskappenv)$ pwd
# ~/flaskapp
(flaskappenv)$ nano showtemp.py
```

In the **_showtemp.py_** file,  I included the bare minimum flask app to see if it works:

```python
# showtemp.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>The temperature is 91.2 F</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

### Testing the first simple flask app

With the first version of the **_showtemp.py_** file complete, I ran the flask app for the first time to see if anything came out. 

To run the flask app, I had to make sure I was in the virtual environment I built earlier. I also needed to allow port 5000 open, becuase that is the default port that flask runs on. 

```text
(flaskappenv)$ sudo ufw allow 5000
(flaskappenv)$ python showtemp.py
```

It works! By pointing a browser to the droplet IP address followed by ```:5000```, I could see my simple message: "The temperature is 91.2 F".

## Setting up uWSGI, nginx and systemctl

### Configuring uWSGI

```bash
(flaskappenv)$ pwd
# ~/flaskapp
(flaskappenv)$ nano wsgi.py
```

in **_wsgi.py_**, I included

```python
# wsgi.py

from showtemp import app

if __name__ == "__main__":
    app.run()
```

### Testing uWSGI

uWSGI can be run from the command line with a couple flags

```bash
flaskappenv)$ uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
```

Still seems to be working! By pointing a browser to the droplet IP address followed by ```:5000```, I could still see The simple message: "The temperature is 91.2 F".

### Making a uWSGI configuration file

Now for another layer of uWSGI goodness- building a uWSGI configuration file

```bash
(flaskappenv)$ deactivate
$ pwd
# ~/flaskapp
$ nano flaskapp.ini
```

Inside the **_flaskapp.ini_** file I included the followingL

```text
[uwsgi]
module = wsgi:app

master = true
processes = 5

socket = myproject.sock
chmod-socket = 660
vacuum = true

die-on-term = true
```

### Making a systemd file

Because I want to have the flask app running all the time, I created a systemd control file to get the flask app running as a system service.

```bash
$ sudo nano /etc/systemd/system/flaskapp.service
```

In the **_flaskapp.service_** file, I included the following

```text
[Unit]
Description=uWSGI instance to serve myproject
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/peter/flaskapp
Environment="PATH=/home/peter/flaskapp/flaskappenv/bin"
ExecStart=/home/peter/flaskapp/flaskappenv/bin/uwsgi --ini flaskapp.ini

[Install]
WantedBy=multi-user.target
```

## Adding Bootstrap Styling