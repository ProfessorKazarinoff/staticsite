Title: JupyterHub Deployment Part 7: DNS Routing
Date: 2009-12-21 12:40
Modified: 2019-12-21 12:40
Status: draft
Category: jupyterhub
Tags: jupyter, jupyterhub, jupyter notebooks, python, cloud server
Slug: jupyterhub-dns-routing
Authors: Peter D. Kazarinoff
Series: JupyterHub Deployment
Series_index: 7
This is the 7th part of a multi-part series that shows how to deploy JupyterHub on Digital Ocean. In this post, we are going to route our domain name to our JupyterHub server. This process is called DNS routing. Once we complete this process, we will be able to access our JupyterHub server by typing our domain name into a web browser instead of typing an IP address like 215.288.548.671 

[TOC]

# Link your domain name to the server's IP address

When we started JupyterHub in the previous step, it ran, we could log in, and we could run Python code. What's not to like, right? **Well, security is the big problem.**

!!! Warning
  Do not run JupyterHub in production without SSL security.
In the initial setup, JupyterHub was running under regular http, not https. With a web application that has usernames and passwords, like JupyterHub, having https and SSL security is best (or really manditory).

In order to use https, we need to generate an SSL certificate. The SSL certificate should correspond to the domain name linked to our server. Therefore, the first step on our way to SSL security, is purchasing a domain name and pointing the domain name at the Digital Ocean DNS servers. Then we'll link the domain name to our JupyterHub server.

domain name --> Digital Ocean DNS servers --> our server

# Google Domains

I purchased the domain for this JupyterHub deployment from Google Domains ([domains.google.com](https://domains.google.com)). The domain cost $12/year (which seems pretty reasonable) and Google domains makes set up pretty easy.

After purchasing the domain, I added the Digital Ocean DNS servers as a set of custom name servers to my domain options on Google Domains.

!!! Google Domains Image !!!

To add a set of custom name servers on the Google Domains dashboard, click the button with the two bars under the DNS header. This brings up a page where you can enter in the Digital Ocean DNS server addressess.

```text
ns1.digitalocean.com
ns2.digitalocean.com
ns3.digitalocean.com
```

!!! Custom Name Servers image !!!

Make sure to click the radio button ```[Use custom name servers]``` and click ```[Save]```.

# Digital Ocean DNS

Now we are going to link our domain name to the IP address of our JupyterHub server on Digital Ocean.

Log into Digital Ocean and in the upper right select [Create] → [Domains/DNS]

!!! DO Domains page image !!!

In the [Add a domain] field, type in the domain name without http, but including .com (or .edu/.org/.net) such as mydomain.org, then click [Add Domain].

!!! A domains image !!!

This brings up a panel where we can add a DNS record.

Enter ```@``` in the text field labeled [Enter @ or hostname]. Then selected the Droplet (our JupyterHub server) that the web address will route to.

!!! Routing Page Image !!!

I also entered ```www``` in the text field [Enter @ or hostname], then selected the JupyterHub droplet like before. This way ```www.mydomain.org``` will route to our JupyterHub server as well.

After completing this step, there will be a couple of new DNS records on the Digital Ocean dashboard. The results will look something like the screen capture below:

!!! DNS Records Listing Image !!!

It takes a couple minutes for the DNS switchover to complete. 

!!! Note
  https://www.whatsmydns.net can be used to check the NS and A records of your domain and see if the domain name is getting through.

# Start JupyterHub and test the domain name

Now our DNS routing is complete, let's check to see the process worked. Log onto the server, activate the ```(jupyterhubenv)``` virtual environment, and start JupyterHub.

```text
$ pwd
/home/peter
$ source .bashrc
$ conda activate jupyterhubenv
(jupyterhubenv)$ jupyterhub --no-ssl
```

Point a web browser to the domain name followed by ```:8000```. If the process doesn't work, it is possible that the ufw server isn't allowing port 8000 through. To open port 8000, type the commands below.

```text
$ sudo ufw allow 8000
```

The running JupyterHub login screen should look something like the screen capture below.

!!! JupyterHub Login Screen Image

After you confirm the login screen comes up and the DNS routing is complete, make sure to close port 8000 on the ufw firewall.

```
$ sudo ufw deny 8000
```

# Next steps

The next in our JupyterHub deployment is to obtain an SSL certificate so we can add SSL security and use https instead of http when we login and use JupyterHub.
