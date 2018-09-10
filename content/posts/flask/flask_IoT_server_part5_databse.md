Title: Building an IoT Server with flask and Python - Part 5 Adding a Database
Date: 2018-09-10 09:01
Modified: 2018-09-10 09:01
Status: draft
Category: flask
Tags: python, flask, thingspeak, mobile, IoT, sensor
Slug: flask-iot-server-database
Authors: Peter D. Kazarinoff

This is the fifth part of a series of posts about building an Internet of Things (IoT) server with **flask**, Python and ESP8266 microcontrollers. In this post we'll add a sqlite3 database to our IoT server so that we can store all the temperature data points that come in from our ESP8266-based WiFi weather stations. We will also use Python's **datetime** library to mark each datapoint with the time when it is stored.

[TOC]

## Introduction

In the last post, we built in some validation to our web API so that only certain API keys and mac addresses are allowed. We also used Python's **datetime** module to time stamp each data point as it comes in. 

This is great, but it would be really nice to _save_ every datapoint that comes in. Right now, when a new data point comes into our server, the old data point gets erased.  

There are a couple of ways we could store the temperature data that comes in from our ESP8266-baed WiFi weather stations:

 * We could save the data in a text file, and write a line to the text file for each data point.
 * We could use a .csv file and give the text file a little more structure.
 * We could use a pandas dataframe and store the data points as rows in the dataframe. 
 * We could use a database to store the data points with each data point being an entry in the database. 
 
 For our **flask** IoT server, we are going to add a sqlite3 datase to store and retrieve the data.

## Why an sqlite3 database?

Why use an sqlite3 database? One of the key reasons is that sqlite3 is part of the Python Standard Library. We don't have to install any external packages to use sqlite3. Sqlite3 is also light weight and won't take up a lot of space on our system. But the real reason I choose to use sqlite3 is that the library has good documentation and I could build off the sqlite3 examples of others. 

## Database design
 
Before adding any data to the database, we need to think a little bit about database design. Our sqlite3 database is going to be a a pretty simple database. We will only employ one table (what I kind of think of as a sheet or tab in Microsoft Excel), and each data point from the WiFi weather stations will represent one record in the database (what I kind of think of as one row a Microsoft Excel). The web API we built brings in a couple of identifiers for each datapoint. Based on an a valid URL such as

> https://mydomain.com/update/API_key=ASCIISTR/mac=6c:rf:7f:2b:0e:g8/field=1/data=72.3
 
In the URL above we've provided:

 * ```update``` (to tell the IoT server to save the data point, not just serve a webpage)
 * ```API_key = ASCIISTR``` (to identify the user)
 * ```mac = 6c:rf:7f:2b:0e:g8``` (to identify the ESP8255-based WiFi weather station)
 * ```field = 1``` (to specify this is a temperature data point, not a humidity data point)
 * ```data = 72.3``` (to specify the temperature is 72.3 degrees)

 Our database needs to be able to save the four fields:

 * ```API_key```
 * ```mac```
 * ```field```
 * ```data```

As well as:

 * ```date``` and ```time```
 * some sort of primary key that uniquley identifies each record

Two example records on our database might look like:

| primary_key | API_key | mac | field | data | data_time |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | PHDNGI2345 | 6c:rf:7f:2b:0e:g8 | 1 | 72.3 | 2018-09-10 08:23:45 PM |

## Prototype the sqlite3 database

I didn't have very much experience building or using databases before this **flask** IoT server project. Before I started coding, I tried out a couple of commands in a jupyter notebook.



## Add the sqlite database to the server

## Add time stamps to each datapoint

## Update the webpage with the newest database entry

## Summary 

It works! We have a working sqlite3 database.

## Next steps 
 In the next post, we'll upload new **_.py_** files to our ESP8266-based WiFi weather stations. This will give the WiFi weather stations the ability to post temperature data to our IoT server.