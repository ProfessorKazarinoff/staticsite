Title: Building a single page Flask App on Digital Ocean
Date: 2018-08-02 09:01
Modified: 2018-08-02 09:01
Status: Draft
Category: flask
Tags: python, flask, thingspeak, mobile, IoT
Slug: flask-app-show-data-from-thingspeak
Authors: Peter D. Kazarinoff
Summary: In this post, I'll run through how I set up a single page flask app that shows a temperature pulled from ThingSpeak.com. ThingSpeak has nice looking graphs, but it is actually kind of hard to see the value of an individual data point. I wanted to be able to see the most recent temperature point recorded by my [ESP8266 WiFi weather station]({filename}/posts/micropython/micropython_upload_code.md) on a phone or tablet. By building a flask app and hosting it on Digital Ocean, I can now view the current temperature from anywhere.


In this post, I'll run through how I set up a single page flask app that shows a temperature pulled from ThingSpeak.com. ThingSpeak has nice looking graphs, but it is actually kind of hard to see the value of an individual data point. I wanted to be able to see the most recent temperature point recorded by my [ESP8266 WiFi weather station]({filename}/posts/micropython/micropython_upload_code.md) on a phone or tablet. By building a flask app and hosting it on Digital Ocean, I can now view the current temperature from anywhere.

[TOC]

## Set up a new Digital Ocean Droplet

The flask app needs a server to run on. I choose Digital Ocean as my cloud server provider. After creating a new server, it is best practice to create a non-root sudo user.

### Create a New Droplet

The [**flask**](http://flask.pocoo.org/docs/1.0/) single page web app will be hosted on [Digital Ocean](https://www.digitalocean.com/). Digital Ocean hosts virtual private servers that run in the cloud. Setting up a server on Digital Ocean is pretty cheap ($5/month) and quick. I host [my **Jupyter Hub** server]({filename}/posts/jupyterhub/why_jupyter_hub.md) on Digital Ocean, so I am also more familiar with spinning up their servers compared to other cloud providers like Linode or AWS.

Creating a new cloud server, called a _Droplet_ in DigitalOcean-speak, involves creating an account on Digital Ocean, logging in and selecting Create --> Droplets in the upper right menu.

![DO create new droplet]({filename}/posts/flask/DO_create_new_droplet.PNG)

For the new Digital Ocean Droplet options I choose:

 * Ubuntu 18.04.1 x64
 * Size: Memory 1G, SSD 25 GB, Transfer 1 TB, Price $5/mo
 * Datacenter Region: San Fransisco 2
 * Additional Options: None
 * SSH keys: **Added all of [my saved SSH keys]({filename}/posts/jupyterhub/PuTTYgen_ssh_key.md). You need this to log into the server with PuTTY!**

Create the server with the big green [**Create**] button.

After the Droplet is created, note the IP address of the server. You'll need the IP address of the droplet for the next step.

### Login to Server with PuTTY

Our first interaction with the server is to log in as root. Then we'll create a non-root sudo user to interact with the server from here on out.

Open PuTTY and log onto the server as root. See a [previous post]({filename}/posts/jupyterhub/new_DO_droplet.md) on how to set up PuTTY on Windows 10. To log into the server as root, set the following in PuTYY:

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

I followed along with the [Digital Ocean Initial Server Setup Tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04) to create a non-root sudo user. The commands entered into the PuTTY SSH terminal are below. Note you should change the username to something other than ```peter```. Here and in the [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04), a hash symbol ```#``` is shown before these commands. The hash ```#``` symbol should not be typed, it just represents the fact you are operating as root.

```text
# adduser peter
# usermod -aG sudo peter
# ufw allow OpenSSH
# ufw enable
```

### Copy SSH keys to the non-root sudo user

Next we'll to move over the SSH keys stored in the root user's profile to the new sudo user's profile (in my case ```peter```). I've had trouble with moving these files and setting the permissions correctly in Linux. A [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04) has a great line that copies the SSH Keys and sets the permissions correctly in one step. If you skip this step, you won't be able to log into the server as the new sudo user you just created. Note that you should probably change the user name to something other than ```peter```.

```text
# rsync --archive --chown=peter:peter ~/.ssh /home/peter
```

Now to check everything works, exit the PuTTY window by typing ```exit``` at the prompt. Open up a new SSH session in PuTTY setting Connection --> Data --> Auto-login username as your non-root sudo user. (I put ```peter``` in the Auto-login username box). When the terminal window opens, you should see your username listed before the prompt. At the prompt, try the following command. Note the dollar sign ```$``` does not need to be typed. The dollar sign ```$``` is there to indicate the command prompt.

```bash
$ sudo -l
User peter may run the following commands on flask-app-server:
    (ALL : ALL) ALL
```

You can type the command ```exit``` to close the terminal.

## Acquire and configure domain name

To use secure SSL connections and https with the flask single page app, we need a real domain name.

### Purchase a domain name

I bought my domain name at [Google Domains](https://domains.google/) for $12/year. The price seems reasonable and Digital Ocean has a tutorial that shows how to connect a google domain's purchased domain name and hook it up to Digital Ocean DNS servers.

### Point DNS severs at Digital Ocean

Once the domain is purchased, the domain's Name Server needs to be pointed at Digital Ocean.

![Google Domains DNS Routing]({filename}/posts/jupyterhub/google_domains_dns_routing.png)

### Link the domain name to the server IP address

On Digital Ocean, login and click [Create] --> [Domains/DNS]. Type in the newly purchased domain name in the box and click [Add Domain]. 

Link the new Domain to the Digital Ocean Droplet by typing in the ```@``` symbol in the [HOSTNAME] box and selecting the new Droplet name in the [WILL DIRECT TO] drop down box. Click [Create Record] to link the domain name to the server. You can also link ```www``` in the [HOSTNAME] box and select the new Droplet in the [WILL DIRECT TO] dropdown box to link ```www.yourdomain.com``` to the server.

![Digital Ocean Domains-DNS]({filename}/posts/jupyterhub/DO_manage_domains.png)

## Build the Flask App

Now that the server is set up and the domain name routed to the server, it's time to actually build the **flask** single page web app.

### Install Packages

Before the single page flask app can be built, a number of packages need to be installed on the server. I followed along with [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04) from Digital Ocean. Log onto the server with PuTTY and type the following commands:

```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3-pip python3-dev python3-setuptools python3-venv
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

With the virtual environment created and activated, I installed **flask**, **wheel**, **uwsgi** and **requests** with **pip**. We'll use **requests** a little later to pull down temperature data from ThingSpeak.com. Note ```(flaskappenv)``` is shown before the command prompt when the virtual environment is active. Make sure to only ```pip install``` in the ```(flaskappenv)``` virtual environment.

```bash
(flaskappenv)$ pip install wheel
(flaskappenv)$ pip install flask
(flaskappenv)$ pip install uwsgi
(flaskappenv)$ pip install requests
```

### Build the first simple **flask** app

With the Python packages installed, next I built a very simple version of the flask app and viewed it in a web browser.

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

You can paste into PuTTY using the right mouse button. Selecting text in PuTTY copies the text to the clip board. Don't use [ctrl-c] or [ctrl-v] to copy and paste. To exit the nano text editor use [ctrl-x].

### Testing the first simple flask app

With the first version of **_showtemp.py_** complete, I ran the **flask** app for the first time to test that everything is working so properly.

To run the **flask** app, I had to make sure I was in the virtual environment built earlier. I also needed to allow port 5000 open on the **ufw** firewall. Port 5000 is the default port **flask** runs on.

```text
(flaskappenv)$ sudo ufw allow 5000
(flaskappenv)$ python showtemp.py
```

It works! By pointing a browser to the droplet IP address followed by ```:5000```, I could see my simple message: "The temperature is 91.2 F".

![flask app no styling]({filename}/posts/flask/flask_app_no_template.png)

## Set up uWSGI, nginx, SSL and systemctl

There are going to be two layers between the flask app and the outside internet. The requests will first come into **NGINX** then go to **uWSGI**. 

### Configuring uWSGI

I installed **uWSGI** earlier when I ```pip``` installed **flask**. Now **uWSGI** needs to be configured and tested. I followed the [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04) closely for this step.

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

#### Testing uWSGI

Next I tested the configuration. **uWSGI** can be run from the command line with a couple flags:

```bash
(flaskappenv)$ uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
```

By pointing a browser to the droplet IP address followed by ```:5000```, I could still see the simple message: "The temperature is 91.2 F". The flask app still seems to be working!

![flask app no styling]({filename}/posts/flask/flask_app_no_template.png)

#### Construct the uWSGI configuration file

Now for another layer of **uWSGI** goodness- building a uWSGI **_.ini_** configuration file.

```bash
(flaskappenv)$ deactivate
$ pwd
# ~/flaskapp
$ nano flaskapp.ini
```

Inside the **_flaskapp.ini_** file I included the following:

```text
[uwsgi]
module = wsgi:app

master = true
processes = 5

socket = flaskapp.sock
chmod-socket = 660
vacuum = true

die-on-term = true
```

### NGINX Configuration

To use NGINX as part of the web stack, we need to create a configuration file in the ```/etc/nginx/sites-available/``` directory. The [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04) was really helpful for this step. NGINX configuration was something I struggled with when I built [my **Jupyter Hub** server]({filename}/posts/jupyterhub/why_jupyter_hub.md) .

```bash
$ sudo nano /etc/nginx/sites-available/flaskapp
```

Edit the NGINX config file **_flaskapp_** the ```/sites-available``` directory to include the following. Make sure to change the ```your_domain``` and ```www.your_domain``` fields:

```
server {
    listen 80;
    server_name your_domain wwww.your_domain;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/peter/flaskapp/flaskapp.sock;
    }
}
```

Now we have to link the NGINX config file to the ```/etc/nginx/sites-enabled``` directory and restart NGINX with the new configuration. If something doesn't look right on the systemctl status screen, you can check for problems with the command ```sudo nginx -t```. 

```bash
$ sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled
$ sudo systemctl restart nginx
$ sudo systemctl status nginx
#ctrl-c to exit
```

Let's also shut off the ```5000``` development port now that NGINX and uWSGI are running.

```bash
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
```

### Apply SSL Security

One of the reasons for getting a real domain name is so the server can run with SSL and https. Adding SSL can be done with **certbot**, a Python program that assists with generating SSL certificates. I followed the [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04) steps to acquire the certificate. Make sure to replace ```your_domain``` with your actual domain name.

```bash
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt install python-certbot-nginx
$ sudo certbot --nginx -d your_domain -d www.your_domain
```

As part of the **certbot** setup I selected option ``2.``

```text
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
```

Now we no longer need to run NGINX with HTTP, since we can now run NGINX with HTTPS and all the traffic will get forwarded to https.

```bash
$ sudo ufw delete allow 'Nginx HTTP'
```

### Construct a **systemd** file

Because I want to have the flask app running all the time, I created a **systemd** control file to get the flask app running as a system service.

```bash
$ sudo nano /etc/systemd/system/flaskapp.service
```

In the **_flaskapp.service_** file, I included the following as described in the [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04). Note the username ```peter``` should be replaced with your non-root sudo user.

```text
[Unit]
Description=uWSGI instance to serve flaskapp
After=network.target

[Service]
User=peter
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

The ```status``` call should show the service as ```active (running)```. Use [ctrl-c] to exit the status screen. This will not stop the service.

After pointing a web browser to the droplet IP address followed by ```:5000```, I can still see the simple message: "The temperature is 91.2 F". It looks like the **NGINX**-->**uWSGI**-->**flask** stack is working properly.

![flask app no styling]({filename}/posts/flask/flask_app_no_template.png)

## Add Bootstrap Styling

The single page app is pretty basic right now. It also isn't designed to look good on phones or tablets. I plan on using my phone the most to view the flask app, so I decided to use bootstrap styling and the jumbotron component from bootstrap in the web app. 

To keep things simple I used the bootstrap CDN instead of installing the whole bootstrap package to the server. On the [bootstrap3 install page](https://getbootstrap.com/docs/3.3/getting-started/) is the content we need to add to the top of our **_.html_** template. I choose to use the CDN instead of installing all of the bootstrap static files on the server. To make the temperature display look nicer, I utilized the [jumbotron component of bootstrap](https://github.com/heimrichhannot/bootstrap/blob/master/docs/4.0/examples/jumbotron/index.html). If you follow the link, you will see a couple lines of html that need to be included first in the ```<header>``` portion of the template.

To add the bootstrap styling I created a jinga template called **_index.html_** and placed a modified version of the html for the jumbotron component and bootstrap CDN inside. On the server, we need to create a templates directory for the jinja template. This is the default location for jinga templates when running **flask**.

```bash
$ cd ~/flaskapp
$ mkdir templates
$ cd templates
$ nano index.html
```

The **_index.html_** template contains a ```<header>``` with the bootstrap3 CDN and a ```<body>``` which contains the jumbotron component.

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">    
<title>show temp</title>

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

</head>

<body>

<div class="container-fluid">
    <div class="jumbotron">
        <hr class="my-4">
        <h1 class="display-4"> 91.4 F</h1>
        <p class="lead">temperature inside</p>
        <hr class="my-4">
    </div>        
</div>

</body>
</html>
```

Now we need to modify the **_showtemp.py_** file to point to our **_index.html_** template. A new **flask** function, ```render_template()``` is used. ```render_template()``` must be included in the imports and is used as the ```return``` action of the ```@app.route("/")``` ```index()``` function. The revised **_showtemp.py_** file is below.

```python
# showtemp.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

## Pull the temperature from ThingSpeak.com with **requests**

The final step of this project is to dynamically pull the temperature from ThingSpeak.com and show it on our single page flask app. Right now the flask app only shows the static temperature ```91.4 F```.  The whole point of the app is to see the current temperatures the WiFi weather stations measure.

To grab the temperatures off of ThingSpeak.com, we'll use the **requests** package. According to the [ThingSpeak.com web API documentation](https://www.mathworks.com/help/thingspeak/rest-api.html), the format of our GET request needs to be:

```text
https://api.thingspeak.com/channels/<channel_id>/fields/<field_id>/last.<format>
```

```<channel_id>``` corresponds to the channel number on ThingSpeak.com. My WiFi weather stations are on a public channel. ```<field_id>``` is the field number held by the ThingSpeak channel. Each ThingSpeak channel can have multiple fields. The temperature we care about is in field ```1```. The ```<format>``` we want is ```.txt```. We could grab ```.json``` or a ```.csv``` off of ThingSpeak, but since we are only grabbing one temperature reading at a time, ```.txt``` is the easiest. In the Python REPL we can try out the ThingSpeak web API. Make sure **requests** is installed in the virtual environment before importing it. On the server try:

```bash
$ source flaskapp/bin/activate
(flaskappenv)$ python

>>> import requests
>>> r = requests.get('https://api.thingspeak.com/channels/266256/fields/2/last.txt')
>>> print(r.text)
-1
>>> exit()

(flaskappenv)$ deactivate
$
```

Now we need to use this same web API call in the flask app. Modify **_showtemp.py_** to include the **requests** package and include the web API request as a line the ```index()``` function. I also included a line to convert the temperature from &deg;F to &deg;C. When the temperature value comes in from ThingSpeak, it is a string. The temperature value needs to be converted to a float before the &deg;C to &deg;F conversion can be accomplished. After the conversion, the temperature in &deg;F needs to be converted back to a string. A string is needed because the temperature in &deg;F is passed to the ```render_template()``` as the parameter ```temp``` which will be used in a revised version of our jinja template **_index.html_**. The extra argument in the ```render_template()``` function transfers the variable ```temp_f``` from the **_showtemp.py_** file to the template **_index.html_**.

```python
# showtemp.py

from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get('https://api.thingspeak.com/channels/254616/fields/1/last.txt')
    temp_c_in = r.text
    temp_f = str(round(((9.0 / 5.0) * float(temp_c_in) + 32), 1)) + ' F'
    return render_template("index.html", temp=temp_f)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

Finally, we need to modify the **_index.html_** template and test the whole flask app. We passed a parameter ```temp``` from **_showtemp.py_** to this template. The ```temp``` parameter can be used programmatically in the jinja **_index.html_** template. The value stored in ```temp``` will end up displayed on the working web page. Jinja templates use code blocks that start and end with double curly brackets ```{{ }}```. Our ```temp``` parameter goes into one of these blocks.

```bash
$ cd ~/flaskapp/templates
$ nano index.html
```

The revised **_index.html_** file is below:

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">    
<title>show temp</title>

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

</head>

<body>

<div class="container-fluid">
    <div class="jumbotron">
        <hr class="my-4">
        <h1 class="display-4"> {{ temp }} </h1>
        <p class="lead">temperature inside</p>
        <hr class="my-4">
    </div>        
</div>

</body>
</html>
```

## View the Final flask app in a Browser

With the changes to **_readtemp.py_** and **_index.html_** complete, we can restart the system service and view our app with a web browser. The final single page flask web app is complete!


```bash
$ sudo systemctl start myproject
$ sudo systemctl status myproject
# ctrl-c to exit
```

If everything is working correctly, you should see the working app running on your domain.

![flask app running]({filename}/posts/flask/simple_index.png)

## Summary

It was a long process setting up this **flask** single page webapp. A lot for technologies and languages were used. An incomplete list is below:

 * cloud servers
 * Linux
 * systemd
 * SSH and SSH keys
 * PuTTY
 * SSL
 * DNS Servers
 * NGINX
 * uWSGI
 * Python
 * web API
 * Flask
 * jinja templates
 * html
 * bootstrap
 
 That's a lot of stuff to go in one project. The next thing I'm thinking about is building a **flask** IoT (internet of things) server that accepts GET requests from my ESP8266 weather stations. ThingSpeak.com works great as an IoT sever, but there are limits to how often data can be posted and how often data can be accessed. I think writing my own IoT server in **flask** would be fun too!
