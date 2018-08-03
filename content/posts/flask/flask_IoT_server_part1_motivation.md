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

There are two problems I am trying to solve with this project. 

### The heat problem

## Current solution
 
 
## Proposed solution

## Next steps



