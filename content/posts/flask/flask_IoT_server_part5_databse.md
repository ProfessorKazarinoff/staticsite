Title: Building an IoT Server with flask and Python - Part 4 Adding a Database
Date: 2018-08-02 09:01
Modified: 2018-08-02 09:01
Status: draft
Category: flask
Tags: python, flask, thingspeak, mobile, IoT, sensor
Slug: flask-iot-server-database
Authors: Peter D. Kazarinoff

This is the fourth part of a series of posts about building an Internet of Things (IoT) server with **flask**, Python and ESP8266 microcontrollers. In this post we'll add a sqlite3 database to our IoT server so that we can store all the temperature data points that come in from our ESP8266-based WiFi weather stations. We will also use Python's **datetime** library to mark each datapoint with a time when it is stored.

[TOC]

## Introduction

In the last post we built a web API for our **flask** IoT server. Each temperature datapoint that came into the server as a GET request URL was stored in a variable that was shown on a webpage. This is great, but it would be really nice to save every datapoint that comes in. Right now when a new data point comes into our server, the old data point gets erased.  There are a couple of ways we could store the temperature data that comes in from our ESP8266-baed WiFi weather stations. We could save the data in a text file, and write a line to the text file for each data point. We could use a .csv file and give the text file a little more structure. We could use a pandas dataframe and store the data points are rows in the dataframe. Or we could use a database to store the data points with each data point being an entry in the database. For our **flask** IoT server, we are going to add a sqlite3 datase to store and retrieve the data.

## Why an sqlite3 database?


## Database design
 
 
## Prototype the sqlite3 database

## Add the sqlite database to the server

## Add time stamps to each datapoint

## Update the webpage with the newest database entry

## Summary 

It works! We have a working sqlite3 database.

## Next steps 
 In the next post, we'll upload new **_.py_** files to our ESP8266-based WiFi weather stations. This will give the WiFi weather stations the ability to post temperature data to our IoT server.