Title: Django IoT Server - Part 8 Bootstrap and Content
Date: 2019-03-21 09:21
Modified: 2019-03-21 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part8-bootstrap-and-content
Authors: Peter D. Kazarinoff

In this post, we are going add bootstrap styling to our Django IoT server. We will also build some content for our main page and our docs page.

[TOC]

## Basic Steps

## Get bootstrap components

go to 
https://getbootstrap.com/docs/4.1/getting-started/introduction/

copy the starter template

## Modify base.html

```html
<!-- templates/base.html -->

{% block doctype %}
    <!DOCTYPE html>
    <html lang="en">
{% endblock %}

{% block head %}
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

        {% block title %}
            <title>Django IoT Server</title>
        {% endblock %}
    </head>
{% endblock %}
{% block body %}
<body>
    {% block header %} {% endblock %}

    {% block content %}{% endblock %}

    {% block footer %}{% endblock %}

    {% block footerjs %}
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
    {% endblock %}

</body>
{% endblock %}
</html>

```

## View on Local Server

## Create static dir and add css to it

project_dir/static

project_dir/static/css/style.css

## Modify settings.py

```python
# settings.py

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

```

## Modify base.html to include static files and new css file

```html
<!-- templates/base.html -->

{% load static %}

{% block doctype %}
    <!DOCTYPE html>
    <html lang="en">
{% endblock %}

{% block head %}
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        
        {% block stylsheets %}
            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
            <link href="{% static 'css/mypcc.min.css' %}" rel="stylesheet">
        {% endblock %}

        {% block title %}
            <title>Django IoT Server</title>
        {% endblock %}
    </head>
{% endblock %}
```

## Modify home.html

## Modify docs.html

## test the server

```text
> cd Documents
> cd django-iot-project
> conda activate djangoiot
(djangoiot)> python manage.py runserver
```

browse to:

 > http://localhost:8000

 > http://localhost:8000/docs


## Summary

This post, we added boostrap styling and some content to our Django IoT server.

## Next Steps

In the next post, we discuss our deployment steps.
