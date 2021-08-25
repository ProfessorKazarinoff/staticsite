Title: Oregon Engineering College Transfer App - Part 3: A new Django project
Date: 2021-08-25 12:40
Modified: 2021-08-25 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-3-new-django-project
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 3
Summary: This is the third part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The web app will show which classes from their community college engineering program will transfer to which classes at a 4-year University engineering program. In this third post, we'll create a new Django project. Then we'll run Django's built-in development server locally to ensure our project is on the right track.

This is the third part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The web app will show which classes from their community college engineering program will transfer to which classes at a 4-year University engineering program. In this third post, we'll create a new Django project. Then we'll run Django's built-in development server locally to ensure our project is on the right track.

## Django Projects and Django Apps

What is a Django project and how is it different from a Django app? A Django app is part of a Django project. One Django project can contain many apps. We'll start out by creating a Django project. Eventually we will add a couple Django apps to the project.

## Create a Django Project

Our website will be build in one Django project. The command below starts a new Django project in the current working directory. Use the Anaconda Prompt to enter the commands.

```text
> cd Documents
> cd transfer
> conda activate transfer
(transfer) > django-admin startproject transfer_project . 
```

This command creates a few files and a new folder in our ```transfer/``` directory. 

```text
transfer/
│   .gitignore
│   LICENSE
│   manage.py
│   README.md
│   requirements.txt
│   runtime.txt
│
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
(transfer) > python manage.py runserver
```

Open up a web browser and type the URL below into the address bar

```text
localhost:8000
```

You should see the Django launch screen with a little rocket, like the picture below.

![django launch sreen]({static}/posts/transfer_app/images/django_launch_screen.png)

You can key in [Ctrl] + [c] to stop the local development server, and get back to the regular Anaconda Prompt.

## Add, Commit and Push Changes up to GitHub

Since we've added new files to our project, we need to add, commit and push these changes up to github.com. Type the commands below into the Anaconda Prompt to ensure the code saved on our local computer is the same as the code saved on GitHub.com

```text
> git add .
> git commit -m "commit message"
> git push origin main
```

## Summary

In this post, we created a new Django project and ran the Django development server for the first time. Our new project is called ```transfer_project```. When we ran the command to create our new Django project, a new folder and a few new files were created. When we ran the development server, we saw the Django launch screen. Our website build is going great so far.

## Next Steps

In the next post, we are going to create our first Django App. This Django app is going create the homepage of our website. 
