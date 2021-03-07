Title: How to send an email with Python
Date: 2021-03-06 09:30
Modified: 2021-03-06 09:30
Status: draft
Category: python
Tags: python, email, cronjob
Slug: how-to-send-an-email-with-python
Authors: Peter D. Kazarinoff

![segmented cone]({static}/posts/engr213/images/segmented_cone.png) 

In this post, I'll go over how to send an email with Python. First we'll go over how to send one email, then we'll set up a server to send emails on a schedule. By the end of the post, you'll learn how to automate sending reminder emails to a group of people. 

[TOC]

## Why send email with Python

Why send email with Python? The use case I have is that each week, I have class that starts on the same days at the same time. About an hour before class, I send a reminder email to the students that class will start soon and include the Zoom link for the class. This is a repedative task. There must be a way to automate this with Python.

## Prerequisits

## Send an email to the command line

First, we are going to send an email from a Python script to the command line. This is a good first step because it doesn't require us to set up an email account. The code below is a modification of the code from a Real Python article [Sending Emails with Python](https://realpython.com/python-send-email/).

From the Anaconda Prompt, start an email server on your local computer with the command below. This local email server running on your computer is where we will send our first email to. Instead of going to a real email address, our outgoing email will be printed to the command line.

```text
python -m smtpd -c DebuggingServer -n localhost:1025
```
![start local email server]({static}/posts/email/images/start_local_email_server_in_anaconda_prompt.PNG)

The terminal will just hang out until an email is sent to it. Don't expect any output until we send our first email.

Copy the Python code below into a file called ```local_email.py```. This script will send an email to the local server we started from the command line above.

```python
# local_email.py

import smtplib

port = 1025
sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost', port=port)
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except:
   print("Error: unable to send email")

```

Run the script above called ```local_email.py``` from a seperate terminal.

```text
python local_email.py
```

You should see an email pop up in the first terminal. 

![email recieved in anaconda prompt]({static}/posts/email/images/email_received_in_anaconda_prompt.PNG)

Great! We were able to send an email locally with our Python script. Next we are going to send an email to a real email address.

## Set up a Google email address

Next we are going to set up a "throw away" gmail account to use for testing. Sign up for a new gmail account and make sure you remember the email address and password.

![email recieved in anaconda prompt]({static}/posts/email/images/gmail_signup_page1.PNG)

After the "throw away" email account is set up, you need to change an account setting to allow less secure apps.

Turn [Allow less secure apps](https://myaccount.google.com/lesssecureapps) to ON. This makes it easier for others to gain access to your account. Only make this security change for your "throw away" email accout.

![email recieved in anaconda prompt]({static}/posts/email/images/gmail_allow_less_secure_apps_on.PNG)

Now we are reay to send an email to a real email address.

## Send an email using a Google email address

Now that we have a "throw away" email account and changed the account settings to allow less secure apps, we can try sending emails with this account.

Create a new Python script called ```send_gmail.py```. Copy the code below into the script.

```python
# send_gmail.py

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "mythrowawayemail@gmail.com"  # your throw away gmail address
receiver_email = "mythrowawayemail@gmail.com"  # your throw away gamil address
password = input("Enter throw away gmail account password: ")
message = """\
Subject: Test Email from Python

This message was sent from Python.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
```

Go to your "throw away" gmail inbox and see the message you sent.

![throw away gmail inbox]({static}/posts/email/images/see_email_in_gmail_inbox.PNG)

This method works to send emails, but the problem is we are entering a plain text password and using an insecure gmail account. Next, we'll see how to use a service called mailgun (that has a pretty generous free tier) to send emails for us.

## Sign up for a Sendgrid account

Next, we are going to use a service called Sendgrid to send emails using Python. Sendgrid has a free tier that you can use to test out sending emails. There is a limit to the number of emails you can send per month, but the limit is pretty high. So for a practice project the free tier will work just fine.

![email recieved in anaconda prompt]({static}/posts/email/images/sendgrid_pricing.png)

## Get a Sendgrid API Key

After you sign up for a Sendgrid account, the next thing to do is secure a Sendgrid API key. The API key is the thing we'll use in our Python script so that Sendgrid knows were the email is coming from and that we have a Sendgrid account.

In order to get an API key, first we need to create a Sendgrid *sender*. I'm not exactly sure what a *sender* is, but we need to create one.

![email recieved in anaconda prompt]({static}/posts/email/images/create_sendgrid_sender.png)

After the *sender* is created, we can get our API key. Use the left-hand menu and scroll down to Settings. Under Settings, click API Keys.

![email recieved in anaconda prompt]({static}/posts/email/images/settings_api_keys.png)

Copy the API key to somewhere safe on your computer. Make sure not to share the API key in version control or on GitHub.

## Create a virtual environment and install the Sendgrid package

Next, we're going to create a virtual environment and install the sendgrid package. It's best practice to create a seperate virtual environment for each project. I use the Anaconda distribution of Python and the Anaconda Prompt to create and manage virtual environments. You could also create a virtual environment using Python's venv module instead.

```text
conda create -y -n email python=3.8
```

Next activate the virtual environment and install the sendgrid package.

```text
conda activate sendgrid
python -m pip install sendgrid
```

## Send an email with Sendgrid

Great, now we can send an email with Sendgrid. Creat a new Python file called ```config.py```. If you are following along and keeping your code in a GitHub repo or another public place, make sure to keep this file out of version control. Add ```config.py``` to your ```.gitignore``` file.

```python
# config.py
# KEEP OUT OF VERSION CONTROL
# ADD TO .gitignore

# config.py
SENDGRID_API_KEY = "SG.XXXXXXXXXXXXXXXXXXXXXXXX"
FROM_EMAIL = "first.last@college.edu"
TO_EMAIL = "first.last@domain.com"
```

Now we'll make the script that will send the email. Copy the code below into a Python file called ```sendgrid_email.py```

```python
# sendgrid_email.py

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from config import SENDGRID_API_KEY, FROM_EMAIL, TO_EMAIL

message = Mail(
    from_email=FROM_EMAIL,
    to_emails=TO_EMAIL,
    subject='Subject for a test email',
    html_content="""This is a reminder:\n\n
    Remember to do that thing.
    """
    )

def main():
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

if __name__ == "__main__":
    main()

```

To send the email, run the ```sendgrid_email.py``` script. Make sure the ```(email)``` virtual environment is active when the script is run.

```text
> python sendgrid_email.py
```

Now pop over to your email and see the awesome email you just sent. Pretty cool right?

It's great that we can run the email reminder program from our computer. But the point of this project is to send automated reminder emails. If I have to run the program each time I want to send an email reminder, that sort of takes away the point of scripting this all in Python.

Therefore, what we are going to do next is deploy our Python script to a cloud server and have the cloud server send the reminder emails for us.

## Run the email program on a server

## Schedule the email program with a cron job on a server

## Wrap Up
