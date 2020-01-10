Title: Deploy a Serverless App with Zappa
Date: 2020-01-08 09:01
Modified: 2020-01-08 09:01
Status: draft
Category: web
Tags: python, flask, zappa, deployment, heroku
Slug: deploy-serverless-app-zappa
Authors: Peter D. Kazarinoff

Zappa is a way to deploy a serverless web app on AWS lamda. In this post, we will build a simple Flask web app with Python and run the web app on AWS Lambda using Zappa in only a few steps.

[TOC]

![Zappa Icon]({static}/posts/zappa/images/zappa_icon.png)

# What is Zappa?

Zappa is a Python package that packages up web apps written in Flask or Django and deploys them to AWS Lamda. Why is Zappa so great then? Becuase instead of deploying your Flask or Django web app on a cloud server like an AWS EC2 instance or a Droplet on Digital Ocean, you can deploy your app serverless as an AWS Lamda function. This isn't really "serverless" (servers run AWS Lambda), but with an AWS Lambda function, you don't have to spin up servers, install packages, make sure security paches are up do date, and most of all: **you don't have to pay for server time that isn't being using.** 

 > A cloud server has to be on all the time, whether or not someone visits your website. But an AWS Lamda function only runs when requested.

Cloud servers are kind of like rental cars. AWS Lamda is sort of like calling an Uber. With Uber, you only pay for the rides you take. The rental car on the other hand has to be paid for even when it's just sitting in your driveway. For only a trip or two in a month, Uber is pretty cheap compared to renting a car for a month.

So as long as your web traffic is low, running a web app serverless on AWS Lambda is pretty cheap compared to running a regular cloud server. AWS Lambda has a free tier. For a simple temporary hobby project, AWS is effectivly free.

Let's get started building our web app with Flask and deploying it on AWS Lambda with Zappa!

# Install Zappa and Flask

Before we can deploy our web app on AWS Lamda with Zappa, first we need to install Zappa and a web framwork to build our web app with. In this example, we are going to build a Flask app, so Flask needs to be installed too. You can install both of the packages with **pip**, the Python package manager. 

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

Create a file called ```app.py``` in the main project directory. Inside the ```app.py``` file, paste the following code. This super simple Flask app will show one webpage that includes the text **Yeah, that is Zappa! Zappa! Zap!**. You can modify the text to include any message you want.

Ultimetly, our web app will look something like the screen cap below.

![zappa zap zap]({static}/posts/zappa/images/simple_app_webpage.png)

Copy the code below into ```app.py```.

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

Next, let's test the Flask app locally. We want to make sure the web app runs on our computer correctly before we deploy the app with Zappa. From a terminal, run the command below. Make sure to run the command in the virtual environment we installed Flask and Zappa into in the previous step. You should see ```(venv)``` before the terminal prompt.

```text
flask run
```

Browse to the URL shown in the terminal [http://127.0.0.1:5000/](Running on http://127.0.0.1:5000/). The webpage should look something like the screenshot below.

![zappa zap zap]({static}/posts/zappa/images/flask_run_locally.png)

**Great! Our web app works locally!** But before we can run our web app serverless on AWS Lamda, there are a couple more steps. Next we need to dive into AWS (Amazon Web Services)

# AWS Credentials

Before we can deploy our serverless web app on AWS Lamda, we need to have an AWS account and create and save a set of AWS credentials.

## Sign up for AWS

![zappa zap zap]({static}/posts/zappa/images/aws_account_page.png)

If you don't have an AWS account yet, you can sign up here: [https://aws.amazon.com/account/](https://aws.amazon.com/account/)

## Create AWS access keys

Next, we need to create a new AWS access key id and secret access key. For me, this was suprisingly tricky. I mean **_how hard can it be to get an access key from AWS?_**

It turns out permissions in AWS is a complicated beast.

![zappa zap zap]({static}/posts/zappa/images/bear_scratch.jpg)

Log into your AWS account at [https://aws.amazon.com/](https://aws.amazon.com/)

Click the orange [Sign In to the Console] button.

![zappa zap zap]({static}/posts/zappa/images/aws_sign_into_the_console.png)

Within the AWS Console, type ```IAM``` into the search box. IAM in the AWS user and permissions dashboard.

![zappa zap zap]({static}/posts/zappa/images/IAM_search.png)

Before we go any further, let's talk a little about permissions in AWS. This took me a while to figure out. There are a couple layers and roles to understand: accounts, groups, users, permissions, and policies.

 * **Accounts**: One person has an AWS account. An AWS account is usually defined by an email address username and a password. Accounts are not the same thing as users.
 * **Users**: Each account can have multiple users associated with it. The account administrator (you) can create new users and delete old users. Users have a set of permissions and policies that determines what they can do on AWS. Users can belong to groups and inheret any of the permissions or policies that come with that group. Each user has an access key id and secret access key. I generally do not assign permissions and policies to users. Instead, I usually have user's inherit permissions and policies from their group.
 * **Groups**: Each account can have multiple groups. User's belong to groups. A group has a particular set of permissions and policies that get passed to the users that are part of the group. Groups do not have access key id's or secret access keys. I generally assign permissions and policies to groups.
 * **Permissions**: A permission is a small piece of work a user or group is allowed do in AWS. For instance, one permission could allow a user or group to upload to an S3 bucket. Another permission could allow a user or group to shut down an EC2 instance. Permissions are grouped together into policies.
 * **Policy**: Policies are groups of permissions assembled together. Since a user will probably want to both upload and download from S3, these two permissions could be combined into one policy. Users and groups can have many policies assigned to them.
 * **Managed Policy**: Managed policies are permissions grouped together by Amazon that covers some sort of sub-functionality of AWS. For instance one managed policy created by Amazon is AWSLambdaFullAccess. This managed policy allows a user or group to do anything on AWS Lambda. 
 * **Inline Policy**: Inline policies are permissions grouped together by you. You can pick individual permissions and assemble them together into an inline policy. A user or group can have many inline and managed policies at the same time.

To get our AWS credentials to run our web app, we need to go through a couple steps:

1. Create a group
2. Assign an inline policy to the group
3. Create a user
4. Add the user to the group
5. Copy the user's keys

### 1. Create a Group

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

### 2. Assign an inline policy to the group

**Double, double toil and trouble...** I had a tough time figuring out what the AWS security policies I needed to attach to my AWS IAM User to get Zappa to work. In the end, I attached one manually created inline policy to the group.

The inline group policy I applied to my new IAM group and then attached the new user to that IAM group is below. I think it's a good idea to attach the security policy to the group and then you can add and delete users easily without loosing any info in the inline security policy. Note the ```XXXXXXXXXXX``` in the inline policy should be replaced by your AWS Account Number.

Your AWS Account Number can be found by clicking [Support] --> [Support Center]. In the Support Center on the upper left hand side will be your Account Number.

The json for the inline policy applied to the group is below.

```text



```

The json above is what worked for me. I expect this set of security permissions may be too open. You could slowly pare down the permissions granted to the IAM Group (and therefore the IAM User attached to the group) and see if Zappa still deploys. The settings above are the ones that finally got Zappa working for me. You can dig through this discussion on GitHub if you want to learn more: [https://github.com/Miserlou/Zappa/issues/244](https://github.com/Miserlou/Zappa/issues/244). 

###  Copy the user's keys

Save the AWS **access key id** and **secret access key** from the IAM User in the file ```~/.aws/credentials```. Note the ```.aws/``` directory needs to be in your home directory and the ```credentials``` file has no file extension.

 > Note: On windows save the credentials file in ```C:\> dir "%UserProfile%\.aws```

In the ```credentials``` file, copy the text below then modify the ```XXXXXXXX``` portions to include your IAM User's keys (no quotes).

```text
[default]
aws_access_key_id = XXXXXXXXXXXXXXXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Now that our AWS credentials are set, close the AWS IAM browser window. Almost time to **see Zappa to do it's magic!**.

# Create Zappa settings file

Next, we need to create the Zappa settings file: ```zappa_settings.json```. Create this file by typing the command  ```zappa init``` into a terminal. (Remember the virtual environment needs to be active when the command is entered)

```text
zappa init
```

The result is a file ```zappa_settings.json``` in the directory where the command was run.

Edit the ```zappa_settings.json``` file so that the ```"profile_name": "default"``` corresponds to the name in square brackets we specified in ```.aws/credentials```. The ```"aws_region"``` also needs to be set. I'm in Oregon, so I choose ```"us-west-2"```. All other settings from ```zappa init``` are OK. 

My complete ```zappa_settings.json``` file is below:

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

> **NOTE:** I saved my project directory in a GitHub repo and included a ```LICENSE```, ```.gitignore``` and a ```README.md```  as part of the repo. Saving the project on GitHub isn't necessary, but I like to keep my code in multiple places and GitHub acts as the central storage location.

The following files should now be in the main project directory:

```text
zappa_app/
├── app.py
├── requirements.txt
├── venv/
└── zappa_settings.json
```

# Deploy on AWS

**It's time to deploy our Flask app on AWS Lambda!** Deploy with app with command below:

```text
zappa deploy dev
```

If everything worked, you should be able to browse to the URL listed in the terminal and see your Zappa web app in all it's serverless glory.

# Modify the App and re-deploy

We can modify our app and see the results live on the web. Open ```app.py``` and change the text in between the ```<h1>     </h1>``` tags to:

```text
# app.py
...

Yeah, that is Zappa! Zappa! Zap! Zap! I am revised

...
```

We can re-deploy the app using the command below:

```text
zappa update dev
```

# Shut down and delete the app

To remove the Zappa app (who knows? maybe you web app sees a ton of traffic in the future), use the following command:

```text
 zappa undeploy dev
 ```

# Summary
In this post, we reviewed how to create a simple web app with Flask and deploy it to AWS Lamda with Zappa. We accomplished the project in a few steps. First we built and run the app locally. Next we messed around with AWS permissions. Finally we ran the Zappa magic. It's pretty neat how little code you need to get a serverless app up and running. 
