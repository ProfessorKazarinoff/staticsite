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
Summary: This is the 6th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this sixth post, add a way for users to log in and out of the site.

This is the 6th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this sixth post, add a way for users to log in and out of the site.

[TOC]

## Who is going to log in and out?

4-year University Administrators

## Install django-crispy-forms

We are going to use a Python package called django-crispy-forms to help make our login form look nice. Django-crispy-forms can be installed at the Anaconda Prompt. Make sure you are in the ```(transfer)``` virtual environment before installing the package.

```text
> conda activate transfer
(transfer) >conda install -c conda-forge django-crispy-forms
```

## Add django-crispy-forms to the list of installed apps

Now that django-crispy forms is installed, it needs to be added to our list of installed apps in the project settings.py file.

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

```



## Add a login template

```html
<!-- templates/users/login.html -->

{% extends 'bootstrap_base.html' %}
{% load crispy_forms_tags %}

{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Log In</legend>
                {{ form|crispy }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Login</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Need An Account? <a class="ml-2" href="{% url 'register' %}">Sign Up Now</a>
            </small>
        </div>
    </div>
{% endblock content %}
```

## Modify project urls

```python
# transfer_project/urls.py

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    #path('users/', include('users.urls')),
    #path('users/', include('django.contrib.auth.urls')),

    path('', include('pages.urls')),
]

```

## Change login redirect

Right now, if we try to login, django sends us to /accounts/users, but for right now, let's have django direct us back to the home page. We can set the url where we end up after logging in the project's settings.py file at the very bottom. We are also going to specify our login URL and set django-crispy-forms to use bootstrap4 styling.

```python
# transfer_project/settings.py

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'


```

## Modify the logout template

```html
<!-- templates/users/logout.html -->

{% extends 'bootstrap_base.html' %}

{% block content %}
<h2>You have been logged out</h2>
    <div class="border-top pt-3">
        <small class="text-muted">
            <a href="{% url 'login' %}">Log In Again</a>
        </small>
    </div>
{% endblock content %}
```

## Modify the navbar to show if we are logged in or note



## Summary

That was a ton of work, but we got the new user model working. We created the users app, added a user model to the users app and then incorporated the user model into the Django admin. Then we ran the Django admin and created a new user. Finally we modified the users/admin.py file so that we could see our custom fields 'university' and 'job' listed on the Django admin users pannel

## Future Work

Next, we'll incorporate a way for users to log in. We have the ability to create new users through the Django admin pannel. Now we need a way for those users to log in and out of the site. 