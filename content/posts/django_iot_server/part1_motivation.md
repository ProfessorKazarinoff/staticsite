Title: Django IoT Server - Part 1 Motivation
Date: 2019-03-20 09:20
Modified: 2017-03-20 09:21
Status: draft
Category: Django
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part1-motivation
Authors: Peter D. Kazarinoff

In this post, I am going to introduce this series about building a Django IoT server

## Why am I building a django IoT Server?

I am building a Django IoT server because students have built projects to upload data and pull down data. Right now they are using ThingSpeak.com, but there are a couple of problems.

 * ThingSpeak only allows uploads every 15 seconds
 * ThingSpeak accounts require a username and password, students can't use college usernames and passwords
 * ThingSpeak can't create groups so that multiple users can access the same channel

 ## Features needed in the Django IoT Server

  * Students login with college usernames and passwords
  * Only college usernames and passwords work
  * Students don't have to set up accounts
  * All plots are shown on the main page
  * Click on a plot to see the private view
  * Each channel can have multiple feeds
  * Each channel can have multiple users
  * Users can add other users to their channels
  * Channels generate API keys
  * Plots run in realtime
  * Plots can show floats or a string

## Summary

This post explained what we need to don

## Next Steps

In the next post, we will review the development environment, set up a GitHub repo and create a virtual environment.