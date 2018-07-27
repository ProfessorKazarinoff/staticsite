Title: A single page Flask App to show data from ThingSpeak.com
Date: 2018-07-20 09:01
Modified: 2018-07-20 09:01
Status: Draft
Category: flask
Tags: python, flask, thingspeak, mobile
Slug: flask-app-show-data-from-thingspeak
Authors: Peter D. Kazarinoff
Summary: In this post, I'll run through how I set up a single page flask app that shows a temperature posted to ThingSpeak.com. I wanted to be able to see the temperature recorded by my WiFi weather station on a phone or tablet. By building a flask app and hosting it on Digital Ocean, I can now view the temperature from anywhere.

In this post, I'll run through how I set up a single page flask app that shows a temperature posted to ThingSpeak.com. I wanted to be able to see the temperature recorded by my WiFi weather station on a phone or tablet. By building a flask app and hosting it on Digital Ocean, I can now view the temperature from anywhere.

## Aquire a domain name

### Purchase Domain

### Point DNS Severs at Digital Ocean

## Setting Up Digital Ocean Droplet

### Create a New Droplet

### Login and create a non-root sudo user

### Copy SSH keys to non-root sudo user

## Building the Flask App

### Installing Packages

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