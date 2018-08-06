Title: Building an IoT Server with flask and Python - Part 4 Validation and Timestamps
Date: 2018-08-02 09:01
Modified: 2018-08-02 09:01
Status: draft
Category: flask
Tags: python, flask, thingspeak, mobile, IoT, sensor
Slug: flask-iot-server-validation-time-stamps
Authors: Peter D. Kazarinoff

This is the fourth part of a series of posts about building an Internet of Things (IoT) server with **flask**, Python and ESP8266 microcontrollers. In the last post we reviewed how to build a web API with flask that accepts temperature measurements. In this post we'll build in some validation to our web API so that only certain API keys and mac addresses are allowed. We will also use Python's datetime module to time stamp each data point as it comes in.

[TOC]

## Introduction

Now that we have a web API, we can make ```GET``` requests using a web browser and see the output in the webpage flask sends back. What's not to like? Well right now any string added to the URL specified by our web API will get through. We don't want just any WiFi weather station to upload data. What we need is some data validation.

### Why data validation?

A _web API_ is a web-based Application Programming Interface. That's a fancy way of saying a server that saves input or produces output based on the URL someone types into their web browser. An example of a web API is the ThingSpeak.com web API. When a web browser, like chrome, is pointed to the followoing URL:

> https://api.thingspeak.com/channels/266256/fields/2/last.txt

The response will be the last data entry that ThingSpeak.com has stored in:

 * channel 266256
 * field 2
 * last entry
 * .txt format

If the URL pasted into the web browser is different, ThingSpeak's response will also be different

> https://api.thingspeak.com/channels/9/fields/1/last.json

The response will be the last data entry that ThingSpeak.com has stored in:

 * channel 9
 * field 1
 * last entry
 * .json format

Most web API's allow you to _pull_ data off of their sites, but many web API's also give you the ability to _put_ data up on their site.

If the URL pasted into the web browser is constructed in the format below, ThingSpeak will store a new data point.

>  https://api.thingspeak.com/update?api_key=THECLASSAPIKEY&field1=87

The datapoint ThingSpeak stores when it recieves the GET request is:

 * user with an API Key = THECLASSAPIKEY
 * field 1
 * data = 87

The web API we are going to build with **flask** needs to be able to do the same two functions that the ThingSpeak web API does: 

 1. Output a particular data point based on a the URL it receives
 2. Store a data point based on a URL it receives
 
 ## Validating incoming URLS
 
 We are going to mimic part of the ThingSpeak.com web API for our **flask** IoT server web API. In order to store a data point based on the URL our server recieves, we need to specify how the URL must be structured in order for the data point to be stored. 
 
 The data will go into our IoT server from ESP8266-based WiFi weather stations. There are a couple unique aspects to each of the ESP8266-based WiFi weather stations.
 
  * A user: Each WiFi weather station has a user. In this case the user is me
  * A mac address: A mac address is a unique address assigned to each piece of hardware. Each of the ESP8266-based WiFi weather stations has a different mac address
  * field: The ESP8266-based WiFi weather stations have the capability to output temperature and humidity. Right now we are just going to deal with temperature, but is will be nice to have an extra field available for multiple data outputs from the same device.
  * data: The temperature data that comes out of each ESP8266-based WiFi weather station.
  
If we put these 4 identifiers as part of our URL, our IoT server will provide the functionality the WiFi weather stations need. 

Below is the general form of our web API url:

 > https://mydomain.com/update/API_key=ASCIISTR/mac=6c:rf:7f:2b:0e:g8/field=1/data=72.3
 
In the URL above we've provided:
 * update (to tell the IoT server to save the data point, not just serve a webpage)
 * API_key = ASCIISTR (to identify the user)
 * mac = 6c:rf:7f:2b:0e:g8 (to identify the ESP8255-based WiFi weather station)
 * fielded = 1 (to specify this is a temperature data point, not a humidity data point)
 * data = 72.3 (to specify the temperature is 72.3 degrees)

Now we need to make our flask app store a data point when a URL like the one we specified above comes in.

## Construct a **flask** web API

Building web API's in **flask** is pretty easy due to **flask's** variable in a route passed to a function functionality. The general syntax is below:

```python
@app.route("/update/key=<route_var>", methods=['GET'])
def update(route_var):
  # code to run
  return render_template("index.html")
```

In the code above, our route ```"/update/key=<route_var>"``` has a variable contained in it, the variable ```<route_var>```. The greater than/less than symboles ```< >``` tell flask there is a variable in the route. In the next line, the variable ```route_var``` that came in from the ```@app.route()``` line is passed as an argument to the ```update()``` function. Then code is run in the body of the function to save the data point, or write a line in a database, or validate the data etc. Finally, the ```update()``` function returns a tempate called ```index.html```. 

### Create a new route

There are four variables to assign in the ```@pp.route()``` URL of our flask web API:

| parameter | purpose | route variable |
| API key | uniqly identigy each user | ```<api_key>``` |
| mac address | unique identifier for each ESP8266 device | ```<mac>``` |
| field | temperature or humidity | ```<field>``` |
| data | data point to save on the server | ```<data>``` |

The complete ```@pp.route()``` URL for our web API looks like:

```text
"/update/API_key=<api_key>/mac=<mac>/field=<int:field>/data=<data>"
```

We can now build a new ```@app.route()```-function pair for this URL. Note that we return a new template called **_update.html_**

```python
@app.route("/update/API_key=<api_key>/mac=<mac>/field=<int:field>/data=<data>", methods=['GET'])
def update(api_key, mac, field, data):
    return render_template("update.html", data=data)
```

### Create a new template

Since we are calling a new template, we need to construct a new template. The template **_update.html_** can have the same form as **_index.html_**. Let's create a new file and copy in the following html code and jinja fields.

```bash
$ cd ~
$ cd flaskapp
$ cd templates
$ nano update.html
```

The code for the new **_update.html_** template is below:

```html
<!-- update.html -->
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
        <p class="lead">last temperature uploaded</p>
        <hr class="my-4">
    </div>        
</div>

</body>
</html>
```


## Test the web API

Now we can restart the flask app and see if our web API works.

```bash
```bash
$ sudo systemctl start flaskapp
$ sudo systemctl status flaskapp
# [ctrl-c] to exit.
```

If we browse to the web address of the server, we should still see the same index template rendered

![flask app running]({filename}/posts/flask/simple_index.png)

But now if we go to the web address:

 > https://yourdomain.com//update/API_key=APGLMD/mac=a3:45:b5:c9/field=1/data=98.6

 You should see the update tempate rendered with a temperature of ```98.6``` shown.

## Summary 

It works! When we put a specific URL into a web browser, it causes the temperature we see on the web to change.

## Next steps 
 In the next post, we'll modify our flask IoT server to do some validation of the input from the web API. We don't want just any person to bang away at the API and upload data points. We are also going to delve into Python's datetime module and add a datetime to each data point uploaded to the web API.