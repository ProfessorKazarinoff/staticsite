Title: Building a Drop Timer using Micropython on an Adadfruit Feather Huzzah ESP8266
Date: 2018-02-17 09:01
Modified: 2018-02-17 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller, WiFi, timer
Slug: micropython-drop-timer-intro
Authors: Peter D. Kazarinoff
Series: drop timer
series_index:1

This is the first part of a multipart series on building a drop timer using Micropython. In this first post, I'll explain what the drop timer is and what it will be used for. I'll also go over some of the constraints that both make the project more difficult and make it more contained.

Problem: Create a system to calculate the drop time of student parachutes dropped from two stories high. The timing system will need to calculat the time between the parachute release and the parachute hitting the ground.

Constraints: The WiFi network has username and password security in addition to an SSID. The parachutes carry a small weight. Part of the time can fit in this weight, but the weight can not have a wire in it.