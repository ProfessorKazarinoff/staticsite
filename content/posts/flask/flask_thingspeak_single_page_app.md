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

The [**flask**](http://flask.pocoo.org/docs/1.0/) single page web app will be hosted on [Digital Ocean](https://www.digitalocean.com/). Digital Ocean is hosts virtual private servers that run in the cloud. Setting up a server on Digital Ocean is pretty cheap ($5/month) and quick. I host [my **Jupyter Hub** server]({filename}/posts/jupyterhub/why_jupyter_hub.md) on Digital Ocean so I am also more familiar with spinning up their servers compared to other cloud providers like Linode or AWS.

Creating a new Digital Ocean cloud server, called a _Droplet_ in Digital Ocean speak involves creating am account on Digital Ocean, logging in and selecting **Create --> Droplets** in the upper right menu.

![DO create new droplet]({filename}/posts/flask/DO_create_new_droplet.PNG)

For the new Digital Ocean Droplet options I choose:

 * Ubuntu 18.04.1 x64
 * Size: Memory 1G, SSD 25 GB, Transfer 1 TB, Price $5/mo
 * Datacenter Region: San Fransisco 2
 * Additional Options: None
 * SSH keys: **Added all of [my saved SSH keys]({filename}/posts/jupyterhub/PuTTYgen_ssh_key.md). You need this to log into the server with PuTTY!**

Create the server with the big green **Create** button.

After the Droplet is created, note the IP address of the server. You'll need the IP address of the droplet for the next step.

### Login to Server with PuTTY

Our first interaction with the server is to log in as root. Then we'll create a non-root sudo user to interact with the server from here on out.

Open PuTTY and log onto the server as root. See a [previous post]({filename}/posts/jupyterhub/new_DO_droplet.md) on how to set up PuTTY. To log into the server as root, set the following in PuTYY:

 * Hostname (or IP Address): The IP address of the server
 * Port: 22
 * Connection Type: SSH
 * Connection:
   * Data:
     * Auto-login username: root
 * Connection:
   * SSH:
     * Auth:
       * Private keyfile for Authentication: your saved private SSH key

![PuTTY IP Address]({filename}/posts/jupyterhub/puTTY_IP_and_Port.png)

![PuTTY IP Login name]({filename}/posts/jupyterhub/putty_login_details.png)

![PuTTY IP Login name]({filename}/posts/jupyterhub/putty_Auth_SSH_private_key.png)

### Create a non-root sudo user

I followed along with the [Digital Ocean Initial Server Setup Tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04) to create a non-root sudo user. The commands to enter into the PuTTY SSH terminal are below. Note you should change the user name to something other than ```peter```. In the [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04), a hash symbol ```#``` is shown before these commands. The hash ```#``` symbol should not be typed, it just represents the fact that you are operating as root.

```bash
# adduser peter
# usermod -aG sudo peter
# ufw allow OpenSSH
# ufw enable
```
### Copy SSH keys to non-root sudo user

Next you'll need to move over the SSH keys stored in the root user's profile to the new sudo user's profile (in my case ```peter```). I've had trouble with setting moving these files and setting the permissions correctly in Linux. The Digital Ocean Tutorial has a great line to more the SSH Keys and set permissions in one step. If you skip this step, you won't be able to log into the server as the new sudo user you just created. Note that you should again change the user name to something other than ```peter```.

```bash
# rsync --archive --chown=peter:peter ~/.ssh /home/peter
```

Now to check that everything works, exit the PuTTY window by typing ```exit``` at the prompt, and open up a new SSH session in PuTTY setting Connection --> Data --> Auto-login username as your non-root sudo user. (I put ```peter``` in the Auto-login username box). When the terminal window opens, you should see your username listed before the prompt. At the prompt, try the following command. Note the dollar sign ```$``` does not need to be typed, it is there to show the command prompt:

```bash
$ sudo -l
User peter may run the following commands on flask-app-server:
    (ALL : ALL) ALL
```

You can type the command ```exit``` to close the terminal.

## Acquire and configure domain name

To use secure SSL connections and https with the flask single page app, I needed a real domain name.

### Purchase a domain name

I bought my domain name at [Google Domains](https://domains.google/) for $12/year. The price seems reasonable and Digital Ocean has a tutorial that shows how to connect a google domain's purchased domain name and hook it up to Digital Ocean DNS servers.

### Point DNS severs at Digital Ocean

Once the domain is purchased, the domain's Name Server needs to be pointed at Digital Ocean.

![Google Domains DNS Routing]({filename}/posts/jupyterhub/google_domains_dns_routing.png)

### Link the domain name to the server IP address

On Digital Ocean, login and click [Create] --> [Domains/DNS]. Type in the newly purchased domain name in the box and click [Add Domain]. Then link the new Domain to the new Digital Ocean Droplet by typing an at symbol ```@``` in the [HOSTNAME] box and selecting the new Droplet in the [WILL DIRECT TO] dropdown box. Click [Create Record] to link the domain name to the server. You can also link ```www``` in the [HOSTNAME] box and select the new Droplet in the [WILL DIRECT TO] dropdown box to link ```www.yourdomain.com``` to the Droplet.

![Digital Ocean Domains-DNS]({filename}/posts/jupyterhub/DO_manage_domains.png)

## Build the Flask App

Now that the server is set up and the domain name is hooked up the the server, it's time to actually build the **flask** single page web app.

### Install Packages

Before the single page flask app can be built, a number of packages need to be installed on the server. I followed along with [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04) from Digital Ocean. Log onto the server with PuTTY and type the following commands.

```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt install python3-pip python3-dev python3-setuptools python3-venv
$ sudo apt-get install build-essential libssl-dev libffi-dev 
```

### Create a Virtual Environment and install **flask**

Once the necessary libraries are installed, I created a virtual environment to run the flask app. I usually use **conda** to create virtual environments, but since I'm not using the Anaconda distribution of Python for this **flask** app, **venv** will have to do instead.

```bash
$ cd ~
$ mkdir flaskapp
$ cd flaskapp
$ python3.6 -m venv flaskappenv
$ source flaskapp/bin/activate
```

With the virtual environment created and activated, I installed flask, wheel, uwsgi and requests with **pip**. Note that ```(flaskappenv)``` is shown before the prompt when the virtual environment is active. Make sure to only ```pip install``` in the virtual environment.

```bash
(flaskappenv)$ pip install wheel
(flaskappenv)$ pip install flask
(flaskappenv)$ pip install uwsgi
(flaskappenv)$ pip install requests
```

### Build the first simple **flask** app

With the Python packages installed, next I built a very simple version of the **flask** app and viewed it in a web browser.

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

You can paste into PuTTY using the right mouse button. Note that [ctrl-x] exits the nano text editor.

### Testing the first simple flask app

With the first version of the **_showtemp.py_** file complete, I ran the **flask** app for the first time to see if anything came out.

To run the **flask** app, I had to make sure I was in the virtual environment I built earlier. I also needed to allow port 5000 open, because that is the default port that flask runs on.

```text
(flaskappenv)$ sudo ufw allow 5000
(flaskappenv)$ python showtemp.py
```

It works! By pointing a browser to the droplet IP address followed by ```:5000```, I could see my simple message: "The temperature is 91.2 F".

## Set up uWSGI, nginx and systemctl

### Configuring uWSGI

There are going to be two layers between the flask app and the outside internet. The requests will first come into **NGINX** then go to **uWSGI**. I installed **uWSGI** earlier when I ```pip``` installed flask. Now uWSGI needs to be configured and tested:

```bash
(flaskappenv)$ pwd
# ~/flaskapp
(flaskappenv)$ nano wsgi.py
```

In the **_wsgi.py_** file, I included:

```python
# wsgi.py

from showtemp import app

if __name__ == "__main__":
    app.run()
```

### Testing uWSGI

Next I tested the configuration. uWSGI can be run from the command line with a couple flags:

```bash
flaskappenv)$ uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
```

Still seems to be working! By pointing a browser to the droplet IP address followed by ```:5000```, I could still see The simple message: "The temperature is 91.2 F".

### Making a uWSGI configuration file

Now for another layer of uWSGI goodness- building a uWSGI **_.ini_** configuration file

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

Because I want to have the flask app running all the time, I created a **systemd** control file to get the flask app running as a system service.

```bash
$ sudo nano /etc/systemd/system/flaskapp.service
```

In the **_flaskapp.service_** file, I included the following. Note that the username ```peter``` should be replaced with your non-root sudo user.

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

### Test with systemctl

After the **_flaskapp.service_** file is complete and saved, we can test our service using:

```bash
$ sudo systemctl start myproject
$ sudo systemctl status myproject
```

The ```status``` call should show the service as ```active (running)```. Use [ctrl]-[c] to exit the status screen. This will not stop the service.

After pointing a web browser to the droplet IP address followed by ```:5000```, I could still see The simple message: "The temperature is 91.2 F". Looks like the **NGINX**-**uWSGI**-**flask** stack is working properly.

## Add Bootstrap Styling


## Pull the temperature with **requests**