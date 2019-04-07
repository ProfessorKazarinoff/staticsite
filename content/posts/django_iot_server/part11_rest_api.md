Title: Django IoT Server - Part 11 Rest API
Date: 2019-03-21 09:21
Modified: 2019-03-21 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part11-rest-api
Authors: Peter D. Kazarinoff

In this post, we are going add a REST API to our Django IoT server using Django REST framework. After we build the REST API, we will test it using the Django admin and the web interface that Django REST Framework creates for us.

[TOC]

## What is a REST API?

## What do we want to be able to do with the REST API?

## Pull most recient version of the project down from GitHub

## Activate virtual environment and install Django REST Framework

```text
(djangoiot)> pip install djangorestframework
```

## Create a users app

## Create a data app

## Create user Model

## Create data Model

## Migrate the database and create a super user

## Test with the Django Admin

## Create Serializers

## Create Views

## Create URL routes

## Test with the built-in django rest framework frontend


SSH keys are sort of like passwords. When we log into the server, we aren't going to do it with a user name and password, like logging into your email account. Instead, we are going to log into the server using a program called PuTTY using an SSH key instead of a password.

We'll store the SSH keys on our computer. The SSH keys are just files that PuTTY Gen creates. SSH keys usually come in pairs: a public key and a private key. The public key will be saved on our virtual private server. The private key will be saved on our computer.  

## Create a Virtual Private Server

The next deployment step is to create a virtual private server on Digital Ocean. Digital Ocean calls these _Droplets_.

## Create a non-sudo root user

After the server is created, we will need to log into the server and create a non-sudo root user

## Install Python on the server

## Create a virtual environment on the server and install Python packages

## Run the Django IoT Server live

## Add nginx and gunicorn

## Add SSL Security

## Summary

This post, we reviewed how we are going to deploy our Django IoT server out in the wild on a Digital Ocean server.

## Next Steps

In the next post, we will start the Django IoT server deployment by creating a set of public and private SSH keys.
