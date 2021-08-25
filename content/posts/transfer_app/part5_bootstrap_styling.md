Title: Oregon Engineering College Transfer App - Part 5: Bootstrap Styling
Date: 2021-08-25 12:40
Modified: 2021-08-25 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-5-bootstrap-styling
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 5
Summary: This is the 5th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. It will show which classes from their community college engineering program will transfer for which classes in a 4-year University engineering program. In this part of the project, we'll add bootstrap styling to our home and about pages.

This is the 5th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. It will show which classes from their community college engineering program will transfer for which classes in a 4-year University engineering program. In this part of the project, we'll add bootstrap styling to our home and about pages.

[TOC]

## What is Bootstrap?

What is Bootstrap and why add it to the django project? [Bootstrap](https://getbootstrap.com/) is a collection of html, javascript and css that produces mobile-responsive web wages. Bootstrap will make the Oregon Transfer App website look good on phones, tablets and laptops. In this part of the project, we'll add bootstrap functionality to our Django templates and produce a navigation menu and styled home and about pages.

## Add Bootstrap styling to templates

Now we'll add bootstrap styling to the templates. We're going to use the bootstrap CDN for simplicity instead of downloading and using the css and javascript files that make up bootstrap. As long there is an internet connection, the CDN link will work.

### Modify the base.html template to use bootstrap

In the templates directory modify the html file called ```base.html```. Include the following in the template. Note in the block stylesheets section there is a link to the bootstrap css. Near the bottom of the page, there are links to the bootstrap javascript. According to the bootstrap docs, the order of javascript links should go: ```jquery```, ```popper.js```, ```bootstrap.js```. The links for the bootstrap CDN may change, the links I used are [here](https://getbootstrap.com/docs/4.1/getting-started/introduction/).

```html
<!-- templates/base.html -->

{% load static %}

{% block doctype %}
    <!doctype html>
    <html lang="en">
{% endblock doctype %}

{% block head %}
    <head>
    {% block meta %}
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Peter Kazarinoff">
    {% endblock meta %}
    {% block favicon %}{% endblock favicon %}
        <title>{% block title %}College Transfer App{% endblock title %}</title>

        {% block stylesheets %}
            <!-- bootstrap 4 CDN -->
            <!-- <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous"> -->
            <!-- bootswatch theme -->
            <link rel="stylesheet" href="{% static 'css/bootswatch_materia.min.css' %}">
            {% block custom_stylesheets %}
            {% endblock custom_stylesheets %}
        {% endblock stylesheets %}
    </head>
{% endblock head %}

{% block body %}
<body>
{%  block nav %}
    {% include "nav.html" %}
{% endblock nav %}
{% block breadcrumb %}{% endblock breadcrumb %}

<main role="main" class="flex-shrink-0">
    {% block content %}
    {% endblock %}
</main><!-- /.container -->

{% block javascripts %}
    <!-- jquery.js CDN -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>

    <!-- popper.js CDN -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>

    <!-- bootstrap.js CDN -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
{% endblock javascripts %}
    </body>
{% endblock body %}
</html>

```

### Add the bootswatch materia bootstrap theme css to the pages app/static/css folder

I want the [bootswatch](https://bootswatch.com/) [materia theme](https://bootswatch.com/materia/) to style the site. I downloaded the [materia theme css]([https://bootswatch.com/4/materia/bootstrap.css](https://bootswatch.com/4/materia/bootstrap.css)) and added the css file to ```pages/static/css/``` as ```bootswatch_materia.min.css```. That's the name of the css file we used in the ```base.html``` template. Note how the ```base.html``` template has the tag ```{% load staticfiles %}```. This tag loads static files (css, javascript, images).

[https://bootswatch.com/4/materia/bootstrap.css](https://bootswatch.com/4/materia/bootstrap.css)

### Build a nav.html template

The ```base.html``` template has a section for a nav bar. The nav bar html is included in the ```base.html``` template in an ```{% include %}``` block:

```html
<!-- templates/base.html -->

{%  block nav %}
    {% include "nav.html" %}
{% endblock nav %}
```

So we need to make a new ```nav.html``` template in the templates directory.

```html
<!-- templates/nav.html -->

<nav class="navbar navbar-expand-md navbar-light fixed-top bg-light">
    <a class="navbar-brand" href="{% url 'home' %}">Oregon Engineering Transfer</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
  
    <div class="collapse navbar-collapse" id="navbarsExampleDefault">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="{% url 'home' %}">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'about' %}">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'major_list' %}">Majors</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'college_list' %}">Colleges</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'course_list' %}">Courses</a>
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
  
```

### Modify the home.html template to use bootstrap

Next modify the home page template to use bootstrap styling. Note the bootstrap_base.html template is now used as the parent template.

```html
<!-- templates/home.html -->

{% extends 'base.html' %}

{% load static %}

{% block custom_stylesheets %}
    <link href="{% static 'css/advising_guide.css' %}" rel="stylesheet">
    <link href="{% static 'css/home.css' %}" rel="stylesheet">
{% endblock custom_stylesheets %}

{% block content %}
<div class="container">
    <div class="jumbotron">
        <h1>Oregon Engineering Transfer Advising Guides</h1>
        <p class="lead">Below are the course transfer guides for engineering students</p>
        <a class="btn btn-lg btn-success" href="{% url 'major_list' %}" role="button">View All Majors »</a>
    </div>

    <div class="container">
        <!-- Example row of columns -->
        <div class="row">
          <div class="col-md-4">
            <h2>Mechanical Engineering</h2>
            <p>Mechanical engineering is an engineering branch that combines engineering physics and mathematics principles with materials science to design, analyze, manufacture, and maintain mechanical systems. </p>
            <p><a class="btn btn-secondary" href="/majors/major/me/" role="button">View details &raquo;</a></p>
          </div>
          <div class="col-md-4">
            <h2>Civil Engineering</h2>
            <p>Civil engineering is a professional engineering discipline that deals with the design, construction, and maintenance of the physical and naturally built environment, including public works such as roads, bridges, canals, dams, airports, sewerage systems, pipelines, structural components of buildings, and railways. </p>
            <p><a class="btn btn-secondary" href="/majors/major/cive/" role="button">View details &raquo;</a></p>
          </div>
          <div class="col-md-4">
            <h2>Electrical Engineering</h2>
            <p>Electrical engineering is an engineering discipline concerned with the study, design and application of equipment, devices and systems which use electricity, electronics, and electromagnetism.</p>
            <p><a class="btn btn-secondary" href="/majors/major/ee/" role="button">View details &raquo;</a></p>
          </div>
        </div>
    
        <hr>
    
      </div> <!-- /container -->
    </div>
{% endblock content %}

```

### Modify the about.html template to use bootstrap

Now modify the about page template to use bootstrap styling. Note again how the ```base.html``` template is used as the parent template.

```html
<!-- templates/about.html -->

{% extends 'base.html' %}

{% load static %}

{% block custom_stylesheets %}
    <link href="{% static 'css/advising_guide.css' %}" rel="stylesheet">
    <link href="{% static 'css/home.css' %}" rel="stylesheet">
{% endblock custom_stylesheets %}

{% block content %}
<div class="container">
    <div class="jumbotron">
        <h1>About Engineering Transfer Advising Guides</h1>
        <p class="lead">These guides were constructed with Portland Community College's transfer guide pages. Additional transfer equivalences were provided by Portland State transfer maps, Oregon State transfer equivalencies and Oregon Institute of Technology transfer mapping pages.</p>
        <a class="btn btn-lg btn-success" href="{% url 'major_list' %}" role="button">View All Majors »</a>
    </div>
</div> <!-- /container -->
{% endblock content %}

```

All the new template and css files ends up with the following directory structure:

![file structure after bootstrap]({static}/posts/transfer_app/images/file_structure_after_bootstrap.png)

## Run the server locally. See if the bootstrap styling works.

OK, let's run the server locally and see if all the bootstrap styling changes made a difference. Run the local server from the Anaconda Prompt using the command below.

```text
> conda activate transfer
(transfer)> python manage.py runserver
```

![about page with bootstrap styling]({static}/posts/transfer_app/images/home_page_bootstrap_stying.png)

![homepage with bootstrap styling]({static}/posts/transfer_app/images/about_page_bootstrap_styling.png)

Awesome! The home and about pages look great!

## Write and run tests for two pages

It's good practice to write tests for our Django project. Django has a built-in test framework that allows us to test the home page and test the about page. In the pages app, we'll modify the ```tests.py``` file to include these tests. Once the tests are written, the tests can be run from the Anaconda Prompt.

### Write tests

Write the tests in the pages/tests.py file:

```python
# pages/tests.py

from django.test import SimpleTestCase


class PagesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

```

### Run tests

Run the tests with the ```manage.py test``` command. If the local server is still running key in [Ctrl-c] to stop the server.

```text
(transfer)> python manage.py test
```

The output I got after running the tests looked something like:

```text
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.018s

OK
Destroying test database for alias 'default'...

```

Great! Both tests passed.

## Summary

We got a lot of work done on the transfer app built with Django and Python. First we created a new pages URL route and created two new pages using Django's class-based views. Then we built some basic templates in Django's built-in templating language. Next, we built a new base template which included the bootstrap CDN. We modified the home and about templates to use some bootstrap elements. We also built a nav template that created a nav bar for the site. Finally we wrote two tests, one test for the home page and one test for the about page. Both tests passed.

## Future Work

Next, we need to build a user app into our Django project. The user app will create functionality to allow users to register and login to the site. Eventually these logged-in users will have access to modify the transfer equivalencies.
