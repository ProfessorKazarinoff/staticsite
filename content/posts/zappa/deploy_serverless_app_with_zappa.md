Title: Deploy a Serverless App with Zappa
Date: 2020-01-08 09:01
Modified: 2020-01-08 09:01
Status: draft
Category: web
Tags: python, flask, zappa, deployment, heroku
Slug: deploy-serverless-app-zappa
Authors: Peter D. Kazarinoff

Zappa is a way to deploy a serverless web app on AWS lamda

[TOC]

# What is Zappa?

Zappa is a Python package the packages up web apps written in Flask or Django and deploys them to AWS Lamda. Why is Zappa so great then? Becuase instead of deploying your Flask or Django web app on a cloud server like an AWS EC2 instance or a droplet on Digital Ocean, you can deploy your app serverless as an AWS Lamda function. This isn't really "serverless", but with an AWS Lamda function, you don't have to spin up servers, install packages on them, make sure security paches are up do date, and most of all, you don't have to pay for server time that isn't being using. A cloud server has to be on all the time, whether or not someone visits your website. But an AWS Lamda function only runs when requested.

Cloud servers are kind of like rental cars. AWS Lamda is sort of like calling an Uber. With Uber, you only pay for the rides you take. The rental car has to be paid for even when it' just sitting in your driveway. For only a trip or two in a month, Uber is pretty cheap compared to renting a car for a month that you only sometimes use.

So as long as your web traffic is low, running a web app serverless on AWS Lamda is pretty cheap compared to a cloud server. AWS Lamda has a free tier. For a simple temporary hobby project, AWS is effectivly free.

# Install Zappa and Flask

Before we can deploy our web app on AWS Lamda with Zappa, we first need to install Zappa and the web framwork to build our web app in. In this example we are going to a Flask app, so Flask needs to be installed to. You can install both of the packages with pip, the Python package manager. 

Using a terminal, create a project directory and cd into it. Create a virtual environment, activate it and install Zappa and Flask.

```text
mkdir zappa_app
cd zappa_app
python -m venv venv
source venv/bin/activate
# on windows: venv\Scripts\activate
pip install flask
pip install zappa
```

# A Simple App

Next, we'll build a simple app in Flask. This App is super small and basic, but it will give you and idea of how Zappa and running a web app on AWS Lamda works.

GitHub repo can be found here: [https://github.com/ProfessorKazarinoff/flask-zappa-tutorial](https://github.com/ProfessorKazarinoff/flask-zappa-tutorial)

Create a file called ```app.py```. Inside the file, paste in the following code. This simple script will just show one webpage that includes the text **Yeah, that is Zappa! Zappa! Zap!**. You can modify the text to include any message you want.

```text
# app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Yeah, that is Zappa! Zappa! Zap! Zap!</h1>'

# We only need this for local development.
if __name__ == '__main__':
    app.run()
```

# Test Locally

Next, let's test the Flask app locally. From a terminal, run the command below. Make sure to run the commands in the virtual environment we installed Flask and Zappa into. You should see ```(venv)``` before the terminal prompt.

```text
flask run app.py
```

Browse to the URL shown in the terminal. The webpage should look something like the screenshot below.


Great! Our web app works locally. There are a couple more steps before we can run the web app serverless on AWS Lamda.

# AWS Credentials

Before we can deploy our serverless web app on AWS Lamda, we need to have an AWS account and create and save a set of AWS credentials.

## Sign up for AWS

If you don't have an AWS account yet, you can sign up here: [https://aws.amazon.com/](https://aws.amazon.com/)

## Create AWS access keys

Next, you need to create a new AWS access key id and secret access key. To me, this was suprisingly tricky. I mean _how hard can it be to get an access key from AWS?_ It turns out permissions in AWS is a complicated beast.

## Save AWS access key id and secret access key

Save these keys in the file ```~/.aws/credentials```. Note the ```.aws/``` directory needs to be in your home directory and the ```credentials``` file has no file extension.

In the ```credentials``` file, copy the text below then modify the ```XXXXXXXX``` portions to include your keys (no quotes).

```text
[default]
aws_access_key_id = XXXXXXXXXXXXXXXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

 > Note: On windows save the credentials file in ```C:\> dir "%UserProfile%\.aws```

Now that our AWS credentials are set, we can work on **getting Zappa to do it's magic**.

# Create zappa settings file

Next, we need to create a Zappa settings file: ```zappa_settings.json```. Create this file by typing the command  ```zappa init``` into a terminal. (Remember the virtual environment needs to be active)

```text
zappa init
```

The result is a file ```zappa_settings.json``` in the directory where the command was run.

Edit the ```zappa_settings.json``` file so that the ```"profile_name": "default"``` corresponds to the name in square brackets we specified in ```.aws/credentials```. The ```"aws_region"``` also needs to be set. I'm in Oregon, so I choose ```"us-west-2"```. All other settings from ```zappa init``` are OK. 

My complete ```zapp_settings.json``` file is below:

```text
{
    "dev": {
        "app_function": "app.app",
        "profile_name": "default",
        "project_name": "flask-zappa-tut",
        "runtime": "python3.7",
        "s3_bucket": "zappa-9cf4j0c1h",
        "aws_region": "us-west-2"
    }
}
```

# Save the requirements.txt

```text
pip freeze > requirements.txt
```

# Deploy on AWS

Deploy with a simple command:

```text
zappa deploy dev
```

# Modify the App and re-deploy

```text
zappa update dev
```

# Summary
In this post, we reviewed how to create a simple web app with flask and deploy it to AWS Lamda. It's pretty neat how little code you need to get a serverless app up and running with Zappa.
