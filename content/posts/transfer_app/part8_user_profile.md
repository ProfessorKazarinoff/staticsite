Title: Oregon Engineering College Transfer App - Part 8: User Profile
Date: 2018-10-19 12:40
Modified: 2018-10-19 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-8-user-profile
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 8
Summary: This is the 8th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this eigth post, we'll add a user profile page that contains user details and a way modify those details.

This is the 8th part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges who want to transfer to 4-year Universities. The transfer web app will show which classes from their Community College Engineering program will transfer to which classes in a 4-year University Engineering program. In this eigth post, we'll add a user profile page that contains user details and a way modify those details.

[TOC]

## Why have a user profile

We want administrators to be able to change their username, email address, job or university. We also want a way for administrators to include some of that information if it isn't part of their profile yet.

## Create a profile page

We need to build a profile page so the Univeristy administrators can see their user details and make changes to their user details. To create the profile page functionality, first we'll build a new profile.html template. Let's put the profile.html tempate in the templates/users directory. The directory strucutre of the entire Django project is below:

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
│        ├───login.html
│        ├───profile.html
│        └───logout.html
├───transfer_project
│   └───__pycache__
└───users
```

In the templates/users/profile.html template below, notice how we include tags for each of the user's details such as username, email, job and university

```html
<!-- templates/users/profile.html -->

{% extends 'bootstrap_base.html' %}

{% block content %}

{{ user.username }}

{{ user.email }}

{{ user.university }}

{{ user.job }}

{% endblock content %}

```

## Modify project urls

Now that the user profile template is created, we need to create a url pattern that points to the template. When a user browses to https://domain.com/users/profile, the profile template should pop up. Edit the transfer_project/urls.py file to include a new route for the user profile template. We'll point to the user app's url's from the project url's. The logic to serve the profile page view will come from the user app's urls.py file.

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

    path('', include('pages.urls')),
]

```

## Modify user app urls

Now that the project urls point to the user app urls, we need to modify the user app urls to point to our profile view.

```python
# users/urls.py

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', ProfilePageView.as_view(), name='profile'),

]

```

## Create a class-based profile page view in users/views.py

```pthon
#from django.views.generic import DetailView


#class ProfilePageView(DetailView):
    #template_name = 'users/profile.html'

# pass some other stuff to the template
```

## Modify the nav bar so that the profile link goes to the profile page

```html
<!-- templates/logged_in_nav_dropdown.html -->

<ul class="nav justify-content-end">
    <li class="nav-item dropdown">
        <a class="btn btn-secondary dropdown-toggle" href="https://example.com" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Logged in as: {{ user.username }}</a>
        <div class="dropdown-menu" aria-labelledby="dropdown01">
            <a class="dropdown-item" href="{% url 'logout' %}">Logout</a>
            <a class="dropdown-item" href="#">Administrator Dashboard</a>
            <a class="dropdown-item" href="{% url 'profile' %}">Profile</a>
            <a class="dropdown-item" href="#">Change Password</a>
        </div>
    </li>
</ul>

```

## Run the local server to see the results

OK. We should be able to see the profile page now. Let's start the local server, login and browse to the profile page using the dropdown menu on the righthand side of the nav bar.

```text
(transfer) > python manage.py runserver
``` 

When the user is not logged in, the page looks like:

![Logout Page]({filename}/posts/transfer_app/images/home_page_login_button.png)

If we click the [Login] button on the upper right, we are brought to the login screen

![Login Page]({filename}/posts/transfer_app/images/login_page.png)

After we log in, we are taken back to the homepage, but now the menu in the upper right shows our user name and has some additional options.

![Home Page Logged in as Peter]({filename}/posts/transfer_app/images/home_page_logged_in_as_peter.png)

If will click [Profile] from the drop down menu, we are brought to the profile page. Awesome!

## Build tests for profile page

Since we have a new page, we need to write some new tests. We already have a couple tests. There is a test for the homepage, about page, login page and logoutpage. We can improve our test coverage by adding tests for the new profile page.

```python
# pages/tests.py

...

class ProfilePageTests(TestCase):
        def test_profile_page_status_code(self):
        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_view_uses_correct_template(self):
        response = self.client.get(reverse('users/profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/users/profile.html')

```

Now let's run our tests and see if they all pass. At the Anaconda Prompt, type:

```text
(transfer) > python manage.py test
```

The tests passed! Now our Django app has a working profile page.

## Summary

In this post we created a user profile page that shows the users username, email, university and position.

## Future Work

Next, we'll build a way for users to modify their profile and do things like change their username, email address, college and job.
