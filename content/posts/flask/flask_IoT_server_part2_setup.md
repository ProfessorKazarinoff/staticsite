Title: Building an IoT Server with flask and Python - Part 2 Set Up
Date: 2018-08-05 09:01
Modified: 2018-08-05 09:01
Status: published
Category: flask
Tags: python, flask, thingspeak, mobile, IoT, sensor
Slug: flask-iot-server-setup
Authors: Peter D. Kazarinoff
Series: Building an IoT Server with Flask and Python
Series_index: 2

This post is the second part of a series of posts which detail building an Internet-of-Things (IoT) server with **flask**, Python and ESP8266 microcontrollers. In this post, we'll describe server setup and microcontroller hardware used in the project.

[TOC]

## Introduction

This **flask** IoT server project builds upon the [ESP8266 WiFi weather station project]({filename}/posts/micropython/micropython_upload_code.md) and the [flask app on Digital Ocean project]({filename}/posts/flask/flask_single_page_app.md). In the flask app on Digital Ocean project, a flask app pulled a measurement temperature down from ThingSpeak.com and displayed the temperature on a webpage. In the ESP8266 WiFi weather station project, an ESP8266 microcontroller (connected to a temperature sensor) posted the temperature up to ThingSpeak.com. The problem with using ThingSpeak.com as an IoT platform is there are limits to how often data can be posted. Building my own IoT server with **flask** is an exciting and interesting project and solves the "only one data post every 15 seconds" limitation imposed by ThingSpeak.


## Prerequisites

Previously, I built a single page flask app that displays the temperature measured by WiFi weather stations. That single page flask app is running on a Digital Ocean cloud server. The flask app pulls a temperature data point using the ThingSpeak.com web API and displays the temperature on a webpage using **flask** and a **jinja** template. See the [flask app hosted on Digital Ocean]({filename}/posts/flask/flask_app_no_template.png) post to see the starting point for this project's **flask** IoT server. 

If you are starting from scratch, the prerequisites needed to build an Internet-of-Things server with **flask**, Python and ESP8266 microcontrollers are:

### Server

 * A Digital Ocean cloud server (just called _the server_ from here on out). See [this post]({filename}/posts/jupyterhub/new_DO_droplet.md) and part of [this post.](http://pythonforundergradengineers.com/flask-app-on-digital-ocean.html#create-a-new-droplet)
 * A domain name hooked up to the server. See part of [this post.](http://pythonforundergradengineers.com/flask-app-on-digital-ocean.html#point-dns-severs-at-digital-ocean)
 * [PuTTY](https://www.putty.org) or a terminal that can SSH into the server
 * The following packages ```apt-get``` installed on the server: ```python3-pip``` ```python3-dev``` ```python3-setuptools``` ```python3-venv``` ```build-essential``` ```libssl-dev``` ```libffi-dev```
  * A Python 3.6 virtual environment set up on the sever with ```flask``` and ```uwsgi``` ```pip install```ed. See part of [this post.](http://pythonforundergradengineers.com/flask-app-on-digital-ocean.html#install-packages)
  *  **uWSGI** and **NGINX** installed on configured on the server. See part of [this post.](http://pythonforundergradengineers.com/flask-app-on-digital-ocean.html#set-up-uwsgi-nginx-ssl-and-systemctl). The configuration files I used can be found on github: [**_myproject.ini_**](https://github.com/ProfessorKazarinoff/flask-IoT/blob/master/myproject.ini), [**_wsgi.py_**](https://github.com/ProfessorKazarinoff/flask-IoT/blob/master/wsgi.py), [**_sites-avialable_**](https://gist.github.com/ProfessorKazarinoff/633abea34c5ea2420f1278deae61c091) (nginx config)
  * The flask app running as a system service. See [this gist](https://gist.github.com/ProfessorKazarinoff/51f819f7001b3fc92982413eb9df4ed5) for the systemd [**_flaskapp.service_**](https://gist.github.com/ProfessorKazarinoff/51f819f7001b3fc92982413eb9df4ed5) file.
  * SSL attached to the domain name and **NGINX** instance. See part of [this post](http://pythonforundergradengineers.com/flask-app-on-digital-ocean.html#apply-ssl-security) and [this post.]({filename}/posts/jupyterhub/SSL_and_nginx_with_jupyterhub.md)

The webpage produced by the flask app is below:

![flask app simple index]({filename}/posts/flask/simple_index.png)

### Hardware

  The below is a list of hardware used to build the ESP8266-based WiFi weather stations. See [this post]({filename}/posts/micropython/micropython_temp_sensor.md) and the Fritzing sketch below for hardware setup.

 * [Adafruit Feather Huzzah ESP8266](https://www.adafruit.com/product/2821)
 * [MCP9808 temperature sensor](https://www.adafruit.com/product/1782), [BMP280 temperature sensor](https://www.adafruit.com/product/2651)
 * [jumper wires](https://www.adafruit.com/product/758), [breadboard](https://www.adafruit.com/product/64)
 * [microUSB cable](https://www.adafruit.com/product/592).
 * [Micropython firmware for the ESP8266](http://micropython.org/download#esp8266) loaded on the ESP8266 board. See [this post.]({filename}/posts/micropython/micropython_install.md)
 * The following **_.py_** files (available on github) were loaded onto the board with **ampy**: [BMP280.py](https://github.com/ProfessorKazarinoff/MATLAB-Arduino-ESP8266-IoT/blob/master/BMP280.py), [MCP9808](https://github.com/ProfessorKazarinoff/MATLAB-Arduino-ESP8266-IoT/blob/master/MCP9808.py), [wifitools.py](https://github.com/ProfessorKazarinoff/MATLAB-Arduino-ESP8266-IoT/blob/master/wifitools.py). See [this post.](content/posts/micropython/micropython_upload_code.md)
 
![fritzing sketch]({filename}/posts/micropython/feather_huzzah_temp_sensor_fritzing.png)

Note that as part of this project, I'm using two ESP8266 microcontrollers. One ESP8266 is connected to a BMP280 temperature sensor and the other ESP8266 is connected to an MCP9808 temperature sensor. These two temperature sensors are leftover from previous projects (I would have used two of the same sensor, but one BMP280 and one MCP9808 is what I have lying around). 

One ESP8266-tempsensor combo is used to measure the temperature outside, the other ESP8266-tempsensor combo is used to measure the temperature inside. 

![ESP8266-based WiFi weather station]({filename}/posts/flask/esp8266-based_wifi_weather_station.png)

## The starting place

The flask app I built was relatively basic and mainly comprised of 2 files: **_showtemp.py_** and **_index.html_**. The file structure on the Digital Ocean server looks like this:

```text
~/
└── flaskapp
    ├── flaskapp.ini
    ├── showtemp.py
    ├── flaskapp.sock
    ├── flaskappenv
    ├── templates
    │   ├── index.html
    └── wsgi.py
```

The main file to run the **flask** app is **_showtemp.py_**

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

The only **jinja** template used by the flask app to build web pages was in the ```/templates``` directory and named **_index.html_**:

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

With the flask app created and the domain name, **nginx**, **uWSGI**, **systemd** and SSL configured- the app is started on the server with:

```bash
$ sudo systemctl start flaskapp
$ sudo systemctl status flaskapp
# [ctrl-c] to exit.
```

The resulting web page looks like this:

![flask app simple index]({filename}/posts/flask/simple_index.png)

## Summary

This post detailed the server setup and microcontroller hardware used in our IoT server with **flask** and Python project. The server running on Digital Ocean has a domain name connected to it and is running a **nginx** --> **uWSGI** --> **flask** web stack. The flask app currently returns a webpage with a temperature pulled from ThingSpeak.com. The hardware includes two Adafruit Feather Huzzah ESP8266 microcontrollers connected to temperature sensors. 

## Next steps
 
In the next post, we'll build a web API with **flask** and push temperature values up to our very own IoT server.
