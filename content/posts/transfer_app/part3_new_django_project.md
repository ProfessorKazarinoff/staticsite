Title: Oregon Engineering College Transfer App - Part 3: A new Django project
Date: 2021-08-23 12:40
Modified: 2021-08-23 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-3-new-django-project
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 3
Summary: This is the third part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this third post, I'll review building the first pages app. The first app to add to the django project. This includes creating the app at the command line, adding the app to the project, creating a view, and creating a urlpattern. Then we'll run the server locally and see if the pages app works.

This is the third part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this third post, I'll review building the first pages app. The first app to add to the django project. This includes creating the app at the command line, adding the app to the project, creating a view, and creating a urlpattern. Then we'll run the server locally and see if the pages app works.

## Django Projects and Django Apps

What is a Django project and how is it different from a Django app? A Django app is part of a Django project. One Django project can contain many apps. We'll start out by creating a Django project. Eventually we will add a couple Django apps to the project.

## Create a Django Project

Our website will be build from one Django project. The command below starts a new Django project in the current working directory.

```text
> cd Documents
> cd transfer-app
> conda activate transfer-app
(transfer-app) > django-admin startproject transfer_project . 
```

This command creates a few files and a new folder in our ```transfer-app``` directory. 

```text
transfer-app/
  │   manage.py
  └───transfer_project
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
```


## Run the local development server

Now that our new Django project is created, we can run Django's built-in development server to ensure our Django installation and Django project creation was successful. Key in the command below to start the development server.

```text
(transfer-app) > python manage.py runserver
```

Next, open up a webbrowser and type the URL below into the address bar

```text
localhost:8000
```

You should see the Django launch screen with a little rocket, like the picture below.

![django launch sreen]({static}/posts/transfer_app/images/django_launch_screen.png)

## Summary

In this post, we created a new Django project and ran the Django development server for the first time. Our new project is called ```transfer_project```. When we ran the command to create our new Django project, a new folder and a few new files were created. When we ran the development server, we saw the Django launch screen. Our website build is going great so far.

## Next Steps

In the next post, we are going to create our first Django App. This Django app is going to be for the homepage and about pages of our website. 
