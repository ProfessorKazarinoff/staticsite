Title: Deploy a Serverless App with Zappa
Date: 2019-12-24 09:01
Modified: 2019-12-24 09:01
Status: draft
Category: jupyter
Tags: python, jupyter, jupyter notebook, voila, heroku, deploy
Slug: deploy-serverless-app-zappa
Authors: Peter D. Kazarinoff

Zappa is a way to deploy a serverless web app on AWS lamda

[TOC]

# Zappa

# A Simple App

GitHub repo can be found here: [https://github.com/ProfessorKazarinoff/flask-zappa-tutorial](https://github.com/ProfessorKazarinoff/flask-zappa-tutorial)

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

```text
flask run app.py
```

# AWS Credentials

Before we can deploy our serverless app on AWS Lamda, we need to have an AWS account and create and save a set of AWS credentials.

## Sign up for AWS
If you don't have an AWS account yet, you can sign up here: [https://aws.amazon.com/](https://aws.amazon.com/)

## Save AWS access key id and secret access key

Next, you need to create a new AWS access key id and secret access key. Save these in ```~/.aws/credentials```

```text
[default]
aws_access_key_id = XXXXXXXXXXXXXXXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

# Create zappa setting file

Now we need to create a Zappa settings file: ```zappa_settings.json```. Create this file with the ```zappa init``` command.

```text
zappa init
```

Edit the file so that the profile name comes from ```.aws/credentials```. aws_region needs to be set, all other settings from zappa init are OK.

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
