Title: Building a Flask IoT Server with Python - Part 5 Posting Data with an ESP8266
Date: 2018-08-02 09:01
Modified: 2018-08-02 09:01
Status: draft
Category: flask
Tags: python, flask, thingspeak, mobile, IoT, sensor
Slug: flask-iot-server-esp8266
Authors: Peter D. Kazarinoff

This is the fifth part of a series of posts about building an Internet of Things (IoT) server with **flask**, Python and ESP8266 microcontrollers. In this post we'll add a sqlite3 database to our IoT server so that we can store all the temperature data points that come in from our ESP8266-based WiFi weather stations. We will also use Python's **datetime** library to mark each datapoint with a time when it is stored.

[TOC]

## Introduction

In the last post we built a web API for our **flask** IoT server. Each temperature datapoint that came into the server as a GET request URL was stored in a variable that was shown on a webpage. This is great, but it would be really nice to save every datapoint that comes in. Right now when a new data point comes into our server, the old data point gets erased.  There are a couple of ways we could store the temperature data that comes in from our ESP8266-baed WiFi weather stations. We could save the data in a text file, and write a line to the text file for each data point. We could use a .csv file and give the text file a little more structure. We could use a pandas dataframe and store the data points are rows in the dataframe. Or we could use a database to store the data points with each data point being an entry in the database. For our **flask** IoT server, we are going to add a sqlite3 datase to store and retrieve the data.

## Hardware Setup


## Upload firmware and **_.py_** files
 
 
## Construct **_run.py_** files

## Test ESP8266-based weather stations

## Upload **_main.py_** files

## Summary 

It works! We have a working Internet of Things (IoT) server that has a working web API that ESP8266-based WiFi weather stations can post to.