Title: Oregon Engineering College Transfer App - Part 6: User Login
Date: 2018-10-18 12:40
Modified: 2018-10-18 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-6-user-login
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 6
Summary: This is the 6th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this sixth post, add a way for users to log into the site.

This is the 6th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this sixth post, add a way for users to log into the site.

[TOC]

## Who is going to log in and out?

4-year University administrators need to be able to log in and out of the site. The 4-year University administrators need to be able to log in so that they can post which classes at a Community College transfer to which classes at their 4-year University. Administrators at other Universities will be able to do the same, but only for class equivalences at their University. 

## Install django-crispy-forms

To help with the forms part of the login and logout pages, we'll use a Python package called django-crispy-forms. This package will help use build the login form and give some bootstrap4 styling to the form. We have bootstrap styling on the rest of the site on the home and about pages, so having bootstrap styling on the login page too helps keep the look of the site consistant. To install django-crispy-forms, we can use the Anaconda prompt and install from the conda-forge channel. Make sure to intall django-crisp-forms into the ```(transfer)``` virtual environment.

```text
> conda activate transfer
(transfer) > conda install -c conda-forge django-crispy-forms
```

### Add django-crispy-forms to the list of installed apps in settings.py

Now that django-crispy-forms is installed, we need to include the package in our list of installed apps in transfer_project/settings.py.  We will also include ```CRISPY_TEMPLATE_PACK = 'bootstrap4'``` at the bottom of the setting.py file to notify the crispy forms app to use bootstrap4 styling.

```python
# transfer_project/settings.py

INSTALLED_APPS = [
    # project specific
    'pages.apps.PagesConfig',
    'users.apps.UsersConfig',

    # 3rd party
    'crispy_forms',
    
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

...

CRISPY_TEMPLATE_PACK = 'bootstrap4'

...

```


## Add a login template

We need to build a login page so the Univeristy administrators can log in and out. First we'll build a login template. Let's put this tempate in the templates/users directory. The directory strucutre of the entire Django project is below:

```text
├───pages
│   ├───migrations
│   │   └───__pycache__
│   ├───static
│   │   └───css
│   └───__pycache__
├───templates
│   ├───registration
│   └───users
├───transfer_project
│   └───__pycache__
└───users
```

In the templates/users/login.html template below, notice how we include the tag ```{% load crispy_forms_tags %}```.  Within the body of the form, we also include the tag ```{{ form|crispy }}```.

```html
<!-- templates/users/login.html -->

{% extends 'bootstrap_base.html' %}
{% load crispy_forms_tags %}

{% block content %}
    <div class="jumbotron">
        <div class="content-section">
            <form method="POST">
                {% csrf_token %}
                <fieldset class="form-group">
                    <legend class="border-bottom mb-4"><h1>Log In</h1></legend>
                    {{ form|crispy }}
                </fieldset>
                <div class="form-group">
                    <button class="btn btn-lg btn-success" type="submit">Login</button>
                </div>
            </form>
            <div class="border-top pt-3">
                <small class="text-muted">
                    Need An Account? <a class="ml-2" href="{% url 'home' %}">Sign Up Now</a>
                </small>
            </div>
        </div>
    </div>
{% endblock content %}
```

## Modify project urls

Now that the login template is created, we need to create a url pattern that points to the template. When a user browses to https://domain.com/login, the login template should pop up. Edit the transfer_project/urls.py file to include a new route for the login template. We'll use Djangos build in ```django.contrib.auth.views.LoginView``` as the view function. Note the import line ```from django.contrib.auth import views as auth_views```. There are going to end up being a lot of functions in this urls.py file with the name ```views```, so we create the alias ```auth_views``` to prevent function name duplication.

```python
# transfer_project/urls.py

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    path('', include('pages.urls')),
]

```

## Modify the nav template to include the login url

We have a login template, a login url and a login view. What we need now is a link on the site for users to click so they can find the login page. Let's put the login link as part of our navigation bar in the page header. We need to modify the nav.html template link the login page with the login menu button in the page nav. Note the tag: ```<a class="dropdown-item" href="{% url 'login' %}">Login</a>```. This tag provides the link to our login page.

```html
<!-- templates/nav.html -->

<nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="#">Navbar</a>
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
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="https://example.com" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Administrators</a>
            <div class="dropdown-menu" aria-labelledby="dropdown01">
              <a class="dropdown-item" href="{% url 'login' %}">Login</a>
              <a class="dropdown-item" href="#">View Transfer Equivalencies</a>
              <a class="dropdown-item" href="#">Modify Transfer Equivalencies</a>
            </div>
          </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>

```


## Run the local server and login

Start the local server with:

```text
(transfer) > python manage.py runserver
```

Browse to http://localhost:8000 and select the [Administrators] dropdown from the navigation bar at the top of the page. Click the [Login] link.

![Home Page Login Link]({static}/posts/transfer_app/images/home_page_login_menu.png)

The login page should look something like this:

![Login Page Login Link]({static}/posts/transfer_app/images/home_page_login_menu.png)

Login with the superuser username and password we created earlier.  Problem is, when we click [Login], we get a Page not found error. Django is trying to direct us to the accounts/profile url, but this page doesn't exist. For right now, let's direct users back to the homepage when they login. We can specify where users go after they login by specifying ```LOGIN_REDIRECT_URL = ``` in our transfer_project/settings.py file. At the bottom of the settings.py file, include the extra two lines at the bottom below the ```CRISPY_TEMPLATE_PACK``` line.

```html
# transfer_project/settings.py

...

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
```

Now go back to the login page, log in again and see we are directed back to the homepage.

![Login Page Login Link]({static}/posts/transfer_app/images/home_page_after_login.png)

## Build tests for login page

Since we have two new pages, we need to write some new tests. We already have a couple tests. There is a test for the homepage and a test for the about page. We can improve these tests by adding an ```assertTemplateUsed()``` test for both pages.

```python
# pages/tests.py

from django.test import SimpleTestCase, TestCase

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class AboutPageTests(SimpleTestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

class LoginPageTests(SimpleTestCase):

        def test_login_page_status_code(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_login_view_uses_correct_template(self):
        response = self.client.get(reverse('logout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/users/login.html')

```

Now let's run our tests and see if they all pass. At the Anaconda Prompt, type:

```text
(transfer) > python manage.py test
```

Everything passes! Great. Another part of the Django project down.

## Summary

In this post we created a user login page template and and view. We installed and used django-crispy-forms to help with the login page style and functionality. We added a link to the login page to our nav bar at the top of the site.  We logged into the site with our superuser user name and password and then specified the homepage as the landing site after users login.

## Future Work

Next, we'll build a way for users to logout. We'll also add a visual indication in the nav bar to show users that they are logged in and provide a link for them to logout. We also will build a logout landing page that results after users successfully logout.