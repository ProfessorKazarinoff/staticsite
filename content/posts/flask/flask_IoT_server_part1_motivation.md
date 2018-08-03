Title: Building a Flask IoT Server with Python - Part 1 Motivation
Date: 2018-08-02 09:01
Modified: 2018-08-02 09:01
Status: draft
Category: flask
Tags: python, flask, thingspeak, mobile, IoT, sensor
Slug: flask-iot-server-motivation
Authors: Peter D. Kazarinoff

This is the first part of a series of posts about building an Internet of Things (IoT) server with **flask**, Python and ESP8266 microcontrollers. In this post we'll I'll dicuss the problem I'm trying to solve and the issues I have with the current solution. We'll also review what the Internet of Things (IoT) is and what and IoT server does.

[TOC]

## Introduction

In the next couple of posts, I'm going to show how I built and Internet of Things server with **flask** and Python. The Internet of Things (IoT) is network of computers, phones, tablets and physical devices like thermostats, garage door openers, light bulbs, doorbell cameras connected together. When we talk about the _internet_ we are usually refering to computers, tablets, phones and servers communicating with webpages, programs and apps. The Internet of Things builds on the internet by including devices other than computers, phones, tablets and servers. 

### IoT devices

I have two ESP8266-based WiFi weather stations. These little devices are part of the Internet of Things. The little WiFi weather stations cost about $20 each and run on very little power. The ESP8266-based WiFi weather stations beam temperature measurments up to servers in the cloud. My ESP8266-based WiFi weather stations are part of the Internet of Things. My WiFi weather stations are called IoT devices

### IoT servers

Servers that interact with Internet of Things devices (like my ESP8266-based WiFi weather stations) are called Internet of Things servers or IoT servers. IoT servers communicate with IoT devices.  Right now, my ESP8266-based WiFi weather stations communicate with ThingSpeak.com IoT servers. The weather stations send temperature measurements up to ThingSpeak.com where the data is saved. In a [previous post]({filename}/posts/flask/flask_single_page_app.md) I detailed how to build a **flask** single page web app that pulls temperature data from ThingSpeak.com

## The Problem 

There are two problems I am trying to solve with this project. One is the problem of summer heat and the other is the problem with ThingSpeak.

### The Heat Problem

I live in Portland, OR and it was **HOT** last week. For the Pacific Northwest really hot. During the day the temperature climbed to 98 degrees one day. I know that if you live in Ft. Worth, TX 98 degrees isn't too bad, but for us in the upper west coast 98 is hot.

One way to keep our house cool during the heat is to open windows at night and use fans to blow cool outside air into the hot stuffy house. The question is: When should I open the windows and turn on the fans? 

During the day, it is hotter outside than inside so I keep the windows closed. But it has been so hot that the even after the sun goes down, it is still hotter outside than inside. 

What I want to know is when does the temperature outside go lower than the temeperature inside. When that I happens I'll open the windows and blow cool air inside. I also want to know when the temperature outside getts hotter than the temperature inside. When that happens I'll close the windows and turn off the fans.

### The ThingSpeak.com problem

Last week, the solution to the temperature inside/temperature outside problem was tackled with ESP8266-based WiFi weather stations. On WiFi weatherstation was taped to a window outside my kids room and another WiFi weather station sat on top of my daughter's dresser. These WiFi weather stations measured temperature once every 60 seconds and posted the temperature to ThingSpeak.com

The WiFi weather stations connected to ThingSpeak.com worked pretty good. But there were a couple issues. One issue is the 15 second limit between data point uploads on ThingSpeak. With two weather stations publishing a data point every 60 seconds, it seems like the data points would be 30 seconds apart. On _average_ every 30 seconds, one of the two weather stations publishes a temperature to ThingSpeak. But a 30 second interval between posts to ThingSpeak is dependant upon the two weather stations synched up so that the two stations measure and send temeratures 30 seconds apart. 

In practice when I plug in both ESP8266-based WiFi weather stations, it is hard to get one plugged in- then exactly 30 seconds later plug the other one in. Also if I only unplug only _one_ of the weather stations it isn't practically possible to know when exactly to plug it back in. Maybe when it is plugged back in, one weather station takes a temperature at 0:02 minutes past the minute mark and the other weather station takes the temperature at 0:10 seconds past the minute mark. If that's the case, then the two measurements are sent within a 15 second window and ThingSpeak will only record the first data from the first weather station.

## Proposed solution

What I propose to do to solve this problem is build my own Internet of Things server with **flask** and Python. With my own IoT server, I can set the limit of how often devices (WiFi weather stations) can post data points. Since I only have two weather stations, the server can accept data points at a faster rate than every 15 seconds. 

In addition to solving a problem, this project also intrests me. I already built a [single page web app with **flask** and Python]({filename}/posts/flask/flask_single_page_app.md). How can this project be taken further? Turning the single page web app into an IoT server is one way of extending the previous project.

### IoT Server Requirements

So what must our IoT server built with **flask** and Python be able to do? It needs to be able to do two main functions:

 * accept and store temperature measurements from two ESP8266-base WiFi weather stations
 * publish the temperture measured by two ESP8266-base WiFi weather stations as a webpage

### Project steps

Building an IoT server with **flask** and Python is a multi-part problem. We can segment the problem into steps:

1. Setup
  1. get a **flask**-based server running in the cloud (Digital Ocean)
  2. assemble the hardware for the WiFi weather stations
2. Built a web API with **flask** and Python that accepts requrest from webbrowers and saves data points
3. Add a database to the server to save the data points one the server
4. Upload code on the ESP8266-based weather stations to send temperture measurements to our web API 

## Next steps

In the next post we will complete the initial setup of our server and hardware. This includes starting a new Droplet (new server) on Digital Ocean as well assembling and connecting two ESP8266 microcontrollers to temperature sensors.



