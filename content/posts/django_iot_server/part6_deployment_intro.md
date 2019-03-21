Title: Django IoT Server - Part 6 Introduction to Deployment
Date: 2019-03-21 09:21
Modified: 2019-03-21 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part6-deployment-intro
Authors: Peter D. Kazarinoff

In this post, we are going to go over the steps to deploy our Django IoT project. We'll deploy the project on a digital ocean virtual private server.

[TOC]

## What is a virtual private server?

## Digital Ocean Account

The first step in deployment is to set up a Digital Ocean account. You can sign up for a Digital Ocean account [here](#)

## Create SSH keys with PuTTY Gen

Before we create the server on Digital Ocean, we need to create a _public and private SSH key pair_. 

### What are SSH keys and why do we need to create one?

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

This post, we reviewed how we are going to deploy our Django IoT server out in the wild.

## Next Steps

In the next post, we will start the server deployment by creating a set of public and private SSH keys.
