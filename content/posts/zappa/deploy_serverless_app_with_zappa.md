Title: Deploy a Serverless App with Zappa
Date: 2020-01-08 09:01
Modified: 2020-01-08 09:01
Status: draft
Category: web
Tags: python, flask, zappa, deployment, heroku
Slug: deploy-serverless-app-zappa
Authors: Peter D. Kazarinoff

Zappa is a way to deploy a serverless web app on AWS lamda. In this post, we will build a simple Flask web app with Python and run the web app on AWS Lambda in only a few steps.

[TOC]

![Zappa Icon]({static}/posts/zappa/images/zappa_icon.png)

# What is Zappa?

Zappa is a Python package the packages up web apps written in Flask or Django and deploys them to AWS Lamda. Why is Zappa so great then? Becuase instead of deploying your Flask or Django web app on a cloud server like an AWS EC2 instance or a droplet on Digital Ocean, you can deploy your app serverless as an AWS Lamda function. This isn't really "serverless", but with an AWS Lamda function, you don't have to spin up servers, install packages on them, make sure security paches are up do date, and most of all, you don't have to pay for server time that isn't being using. 

 > A cloud server has to be on all the time, whether or not someone visits your website. But an AWS Lamda function only runs when requested.

Cloud servers are kind of like rental cars. AWS Lamda is sort of like calling an Uber. With Uber, you only pay for the rides you take. The rental car has to be paid for even when it's just sitting in your driveway. For only a trip or two in a month, Uber is pretty cheap compared to renting a car for a month that you only take one or two trips with.

So as long as your web traffic is low, running a web app serverless on AWS Lambda is pretty cheap compared to a regular cloud server. AWS Lamda has a free tier. For a simple temporary hobby project, AWS is effectivly free.

# Install Zappa and Flask

Before we can deploy our web app on AWS Lamda with Zappa, first we need to install Zappa and the web framwork to build our web app with. In this example we are going to build a Flask app, so Flask needs to be installed too. You can install both of the packages with pip, the Python package manager. 

Using a terminal, create a project directory and ```cd``` into it. Create a virtual environment, activate it, and install Zappa and Flask.

```text
mkdir zappa_app
cd zappa_app
python -m venv venv
source venv/bin/activate
# on windows: venv\Scripts\activate
pip install flask
pip install zappa
```

![Zappa Icon]({static}/posts/zappa/images/flask_icon.png)

# A Simple App

Next, we'll build a simple web app in Flask. This app is super small and basic, but it will give you and idea of how Zappa and running a web app on AWS Lamda works.

A GitHub repo with all the code used in the rest of this post can be found here: [https://github.com/ProfessorKazarinoff/flask-zappa-tutorial](https://github.com/ProfessorKazarinoff/flask-zappa-tutorial)

Create a file called ```app.py``` in the main project directory. Inside the ```app.py``` file, paste in the following code. This super simple Flask app will just show one webpage that includes the text **Yeah, that is Zappa! Zappa! Zap!**. You can modify the text to include any message you want.

![zappa zap zap]({static}/posts/zappa/images/simple_app_webpage.png)

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

Next, let's test the Flask app locally. From a terminal, run the command below. Make sure to run the command in the virtual environment we installed Flask and Zappa into. You should see ```(venv)``` before the terminal prompt.

```text
flask run
```

Browse to the URL shown in the terminal [http://127.0.0.1:5000/](Running on http://127.0.0.1:5000/). The webpage should look something like the screenshot below.

![zappa zap zap]({static}/posts/zappa/images/flask_run_locally.png)

**Great! Our web app works locally!** There are a couple more steps before we can run our web app serverless on AWS Lamda. And Zappa is going to help.

# AWS Credentials

Before we can deploy our serverless web app on AWS Lamda, we need to have an AWS account and create and save a set of AWS credentials.

## Sign up for AWS

![zappa zap zap]({static}/posts/zappa/images/aws_account_page.png)

If you don't have an AWS account yet, you can sign up here: [https://aws.amazon.com/account/](https://aws.amazon.com/account/)

## Create AWS access keys

Next, you need to create a new AWS access key id and secret access key. For me, this was suprisingly tricky. I mean **_how hard can it be to get an access key from AWS?_** It turns out permissions in AWS is a complicated beast.

![zappa zap zap]({static}/posts/zappa/images/bear_scratch.jpg)

Log into your AWS account at [https://aws.amazon.com/](https://aws.amazon.com/)

Click the orange [Sign into the Console] button.

![zappa zap zap]({static}/posts/zappa/images/aws_sign_into_the_console.png)

Within the AWS Console, type ```IAM``` into the search box.

![zappa zap zap]({static}/posts/zappa/images/IAM_search.png)

In the IAM Dashboard, click [Groups] on the lefthand menu. And then create a new group with the [Create New Group] button.

![zappa zap zap]({static}/posts/zappa/images/IAM_groups.png)

Give your group a name and click [Next Step].

![zappa zap zap]({static}/posts/zappa/images/IAM_set_group_name.png)

Add APIGateway security policies and Lambda security policies. It is easiest to search for these. Once the security policies are added, click [Next Step].

![zappa zap zap]({static}/posts/zappa/images/IAM_APIGateway_Policy.png)

![zappa zap zap]({static}/posts/zappa/images/IAM_Lambda_Policy.png)

Review the group security policies and click [Create Group]

![zappa zap zap]({static}/posts/zappa/images/IAM_Review_Grou.png)

Back at the IAM Dashboard, create a new user with the [Users] lefthand menu option and the [Create New User] button.

![zappa zap zap]({static}/posts/zappa/images/IAM_add_user.png)

Give your new user a name and select the Access Type for [Programmatic Access]. Click the [Next: Permissions] button.

![zappa zap zap]({static}/posts/zappa/images/IAM_set_user_details.png)

Add the new user to the group we just created. Click [Next: Tags]

![zappa zap zap]({static}/posts/zappa/images/IAM_add_user_to_group.png)

Tags are optional. Add tags if you want, then click [Next: Review]

![zappa zap zap]({static}/posts/zappa/images/IAM_add_tags.png)

Review the user details and click [Create user]

![zappa zap zap]({static}/posts/zappa/images/IAM_review_user.png)

You should now be able to see your new user attached to your new group. 

![zappa zap zap]({static}/posts/zappa/images/IAM_user_success.png)

Click the [Show] button under the [Secret Access Key] Heading. You should now be able to see both the [Access key ID]  and the [Secret access key]. We need both of these keys to deploy our Zappa app.

![zappa zap zap]({static}/posts/zappa/images/IAM_secrets_shown.png)

Don't close the AWS IAM window yet. In the next step you will need to be able to copy and paste these keys into a file. _But first, a little yum yum._

## AWS Security Policies

**Double, double toil and trouble...** I had a tough time figuring out what the AWS security policies I needed to attach to my AWS IAM User to get Zappa to work. In the end, I attached two manually created policies to the User and had four AWS pre-created group policies attached to the group the user was part of. The json output of the two individual policies are below:

The inline group policy I applied to my new IAM group and then attached the new user to that IAM group is below. I think it's a good idea to attach the security policy to the group and then you can add and delete users easily without loosing any info in the inline security policy. Note the ```XXXXXXXXXXX``` should be replaced by your AWS Account Number.

The AWS Account Number can be found by clicking [Support] --> [Support Center]. In the Support Center on the upper left hand side will be your Account Number.

```text
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:AttachRolePolicy",
        "iam:GetRole",
        "iam:CreateRole",
        "iam:PassRole",
        "iam:PutRolePolicy"
      ],
      "Resource": [
        "arn:aws:iam::XXXXXXXXXXXXXX:role/*-ZappaLambdaExecutionRole"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "apigateway:DELETE",
        "apigateway:GET",
        "apigateway:PATCH",
        "apigateway:POST",
        "apigateway:PUT",
        "events:DeleteRule",
        "events:DescribeRule",
        "events:ListRules",
        "events:ListRuleNamesByTarget",
        "events:ListTargetsByRule",
        "events:PutRule",
        "events:PutTargets",
        "events:RemoveTargets",
        "lambda:AddPermission",
        "lambda:CreateFunction",
        "lambda:DeleteFunction",
        "lambda:GetAlias",
        "lambda:GetFunction",
        "lambda:GetFunctionConfiguration",
        "lambda:GetPolicy",
        "lambda:InvokeFunction",
        "lambda:ListVersionsByFunction",
        "lambda:RemovePermission",
        "lambda:UpdateFunctionCode",
        "lambda:UpdateFunctionConfiguration",
        "cloudformation:CreateStack",
        "cloudformation:DeleteStack",
        "cloudformation:DescribeStackResource",
        "cloudformation:DescribeStacks",
        "cloudformation:ListStackResources",
        "cloudformation:UpdateStack",
        "cloudfront:UpdateDistribution",
        "logs:DeleteLogGroup",
        "logs:DescribeLogStreams",
        "logs:FilterLogEvents",
        "route53:ListHostedZones"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:CreateBucket",
        "s3:ListBucket",
        "s3:ListBucketMultipartUploads"
      ],
      "Resource": [
        "arn:aws:s3:::zappa-*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:PutObject",
        "s3:AbortMultipartUpload",
        "s3:ListMultipartUploadParts"
      ],
      "Resource": [
        "arn:aws:s3:::zappa-*/*"
      ]
    }
  ]
}

```

The json above is what worked in the end. I expect this set of security permissions may be too open. You could slowly pare down the permissions granted to the IAM Group (and therefore the IAM User attached to the group) and see if Zappa still deploys. The settings above are the ones that finally got it working for me. You can dig through this discussion on GitHub if you want to know more [https://github.com/Miserlou/Zappa/issues/244](https://github.com/Miserlou/Zappa/issues/244). 

## Save AWS access key id and secret access key

Save the AWS access key id and secret access key in the file ```~/.aws/credentials```. Note the ```.aws/``` directory needs to be in your home directory and the ```credentials``` file has no file extension.

 > Note: On windows save the credentials file in ```C:\> dir "%UserProfile%\.aws```

In the ```credentials``` file, copy the text below then modify the ```XXXXXXXX``` portions to include your keys (no quotes).

```text
[default]
aws_access_key_id = XXXXXXXXXXXXXXXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Now that our AWS credentials are set, close the AWS IAM browser window and we can work on **getting Zappa to do it's magic!**.

# Create Zappa settings file

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
        "project_name": "zappa-flask-app",
        "runtime": "python3.7",
        "s3_bucket": "zappa-9cf4j0c1h",
        "aws_region": "us-west-2"
    }
}
```

# Save the requirements.txt

Before we deploy (we are almost done!), we'll create a ```requirements.txt``` file using ```pip freeze```

```text
pip freeze > requirements.txt
```

> I saved my project directory in a GitHub repo and included a ```LICENSE```, ```.gitignore``` and a ```README.md```  as part of the repo. Saving the project on GitHub isn't necessary, but I like to keep my code in multiple places and GitHub acts as the central storage place.

The following files should now be in the main project directory:

```text
zappa_app/
├── app.py
├── requirements.txt
├── venv/
└── zappa_settings.json
```

# Deploy on AWS

It's time to deploy our Flask app on AWS Lambda. Deploy with the simple command below:

```text
zappa deploy dev
```

If everything worked, you should be able to browse to the URL listed in the terminal and see your Zappa web app in all it's serverless glory.

# Modify the App and re-deploy

Change the return within the ```<h1>``` tags to:

```text
Yeah, that is Zappa! Zappa! Zap! Zap! I am revised
```

Then re-deploy the app.

```text
zappa update dev
```

# Shut down and delete the app

To remote the Zappa app, use the following command:

```text
 zappa undeploy dev
 ```


# Summary
In this post, we reviewed how to create a simple web app with flask and deploy it to AWS Lamda. It's pretty neat how little code you need to get a serverless app up and running with Zappa.
