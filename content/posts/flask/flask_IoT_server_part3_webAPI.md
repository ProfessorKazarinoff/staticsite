Title: Building a Flask IoT Server with Python - Part 3 Web API
Date: 2018-08-02 09:01
Modified: 2018-08-02 09:01
Status: draft
Category: flask
Tags: python, flask, thingspeak, mobile, IoT, sensor
Slug: flask-iot-server-web-API
Authors: Peter D. Kazarinoff

This is the third part of a series of posts about building an Internet of Things (IoT) server with **flask**, Python and ESP8266 microcontrollers. In the last post we reviewed the server and hardware setup. In this post we'll build a web API with **flask** and push temperature data to our web API with a web browser.

[TOC]

## Introduction

We already have a working flask app on Digital Ocean. Now we need to add a web API to it's functionality

### What is a web API?

A _web API_ is a web-based Application Programming Interface. That's a fancy way of saying a server that saves input or produces output based on a URL. An example of a web API is the ThingSpeak web API. When a web browser like chrome is pointed to the followoing URL:

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

If the URL pasted into the web browser is constructed like below, ThingSpeak will store a new data point.

>  https://api.thingspeak.com/update?api_key=THECLASSAPIKEY&field1=87

The datapoint ThingSpeak stores when it recieves the GET request is:

 * user with an API Key = THECLASSAPIKEY
 * field 1
 * data = 87

The web API we are going to build with **flask** needs to be able to do the same two functions that the ThingSpeak web API does: 

 1. Output a particular data point based on a the URL it receives
 2. Store a data point based on a URL receives
 
 ## Web API Design
 
 We are going to mimic part of the ThingSpeak.com web API for our **flask** IoT server. In order to store a data point based on the URL our server recieves, we need to specify how the URL must be structured in order for the data point to be store. The data will go into our IoT server from ESP8266-based WiFi weather stations. There are a couple unique aspects to each of the ESP8266-based WiFi weather stations.
 
  * A user: Each WiFi weather station has a user. In this case the user is me
  * A mac address: A mac address is a unique address assigned to each piece of hardware. Each of the ESP8266-based WiFi weather stations has a different mac address
  * field: The ESP8266-based WiFi weather stations have the capability to output temperature and humidity. Right now we are just going to deal with temperature, but is will be nice to have an extra field available for multiple data outputs from the same device.
  * data: The temperature that comes out of each ESP8266-based WiFi weather station.
  
If we put these 4 identifiers as part of our URL, our IoT server will provide the functionality the WiFi weather stations need. 

Below is the general form of our web API url:

 > https://mydomain.com/update/API_key=ASCIISTR/mac=6c:rf:7f:2b:0e:g8/field=1/data=72.3
 
In the URL above we've provided:
 * update (to tell the IoT server to save the data point, not just serve a webpage)
 * API_key = ASCIISTR (to identify the user)
 * mac = 6c:rf:7f:2b:0e:g8 (to identify the ESP8255-based WiFi weather station)
 * fieled = 1 (to specify this is a temperature data point)
 * data = 72.3 (to specify the temperature is 72.3 degrees)

Now we need to make our flask app store a data point when a URL like the one we specified above comes in.

## Construct a **flask** web API

### Create a new route

### Create a new template

## Test the web API

Now we can restart

## Summary 

It works! When we put a specific URL into a web browser, it causes the temperature we see on the web to change.

## Next steps 
 In the next post, we'll add an sqlite database to our flask IoT server so that all the data points which come into the server can be saved.