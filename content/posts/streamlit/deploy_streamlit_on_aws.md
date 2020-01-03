Title: How to Deploy a Streamlit App with AWS
Date: 2019-12-29 08:11
Modified: 2019-12-29 08:11
Status: draft
Category: Python
Tags: streamlit, bokeh, engineering
Slug: streamlit-app-aws
Authors: Peter D. Kazarinoff

![Anaconda Prompt run_mohrs_circle_app.py]({static}/posts/streamlit/images/mohrs_circle_app.png)

[**Streamlit**](https://streamlit.io/docs/) is a web app-building framework for Python. Streamlit is a way to create mostly simple single-page web apps that are easy to deploy. Streamlit is useful for engineers and data scientists who have some app functionality, like a plot that dynamically changes based on user interaction, but don't want to build out a full website using a web framework like Django or Flask. 

In this post, we will create a Streamlit app that displays a Bokeh plot and deploy it online with Amazon Web Services (AWS)

### Deploy on AWS

### Log into AWS

Log into AWS. The Login URL is below. If you don't have an AWS account yet, you can create one for free.

 > [aws.amazon.com](https://aws.amazon.com)

 Click the [Sign into the console] button and supply your username and password. 

### Create a new EC2 instance

In the search dialog, enter ```EC2``` then press return. An EC2 instance is Amazon's term for a single cloud server. When we say we want to deploy our Streamlit app on a cloud server, specifically we are deploying our Streamlit app on an AWS EC2 instance. 

In the AWS EC2 Dashboard, scroll down and click the [Launch Instance] button and select [Launch Instance].

There are a number of steps to complete to create our cloud server (launch our AWS instance)

1. Choose the Amazon Machine Image (AIM)

Type ```ubuntu``` into the search box. Choose the [Ubuntu Server 18.04 LTS] image. This image is part of AWS's free tier. Click [Select] 64 bit (x86). AIM stands for Amazon Machine Image. This basically means which operating system our server gets. Options include a Windows Sever, an Ubuntu server or a Red Hat Linux server. 

Need to configure security rule for TCP port 8501



2. Choose Instance Type

Choose the "Free Tier Eligable" instance type. This is the ```t2.micro``` type.

3. Configure Instance

The defaults can be left as-is.

4. Add storage

The defaults can be left as-is.

5. Add tags

You can add a tag such as ```Streamlit App``` if you want. A tag isn't required.

6. Configure Security Gourps

Add your IP Address to the SSH group

7. Review

After all seven steps, click [Launch]. This should bring up an Add Key Pair Dialog box.

### Connect to the AWS EC2 Instance with SSH

Open PuTTY or a terminal and copy the Public DNS address of the newly created instance.

 * in the IP address box, paste the EC2 instance's public IP. Something like ```ec2-64-195-8-347.us-west-2.compute.amazonaws.com```
 * in the auto-login user name: ```ubuntu```
 * under SSH --> Security. Select the private key file downloaded earlier.

Go back to the PuTTY home screen and click connect.

This should log you into the AWS EC2 cloud server.

### Update the server

At the server prompt, type the update commands:

```text
sudo apt-get -y update && sudo apt-get -y upgrade
```

### Clone the GitHub Repo that contains Streamlit App code

```text
git clone https://github.com/ProfessorKazarinoff/mohrs_circle.git
```

### Create the virtual environment

```text
cd mohrs_circle
sudo apt-get install -y python3-venv
python3 venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Run streamlit

```text
streamlit run mohrs_circle_streamlit_app.py
```

### Browse to the DNS address of the EC2 Instance


7. Review






That's it! The Streamlit app should now be running on our AWS EC2 instance.

### View the Streamlit App live on the web

Check the URL provided by Azure dashboard. The app works the same as when we ran it locally, but now it's live on the internet. Anyone with the URL can view our Streamlit app.

The Streamlit app opens on a phone too. 

## Summary

In this post, we created a web app with Streamlit and deployed it on Microsoft's Azure cloud service
