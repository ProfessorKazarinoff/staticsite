Title: Django IoT Server - Part 4 Start a Django Project
Date: 2019-03-21 09:21
Modified: 2019-03-21 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part4-start-django-project
Authors: Peter D. Kazarinoff

In this post, I am going to review how to start django project and get our IoT server running at the bare minimum.

[TOC]

## Start Django project

```text
> cd Documents
> conda activate djangoiot
(djangoiot)> django-admin startproject django_iot_project
```

## Review project directory structure

## Run the local development server

```text
> cd Documents
> cd django_iot_project
> conda activate djangoiot
(djangoiot)> python manage.py makemigrations
(djangoiot)> python manage.py migrate
(djangoiot)> python manage.py runserver
```



## Summary

This post explained how to start a Django project and which files are present

## Next Steps

In the next post, we will review how to create the homepage
