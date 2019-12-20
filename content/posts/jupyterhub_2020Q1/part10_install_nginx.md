Title: JupyterHub Deployment Part 10: Install Nginx
Date: 2009-12-19 12:40
Modified: 2019-12-19 12:40
Status: draft
Category: jupyterhub
Tags: jupyter, jupyterhub, jupyter notebooks, python, cloud server
Slug: jupyterhub-depolyment-nginx-install
Authors: Peter D. Kazarinoff
Series: JupyterHub Deployment
Series_index: 10
This is the 10th part of a multi-part series that shows how to deploy JupyterHub on Digital Ocean. In this post, we will install Nginx. We'll use Nginx as a reverse proxy to sit in front of JupyterHub when requests come in from client machines.

In previous steps of this series, we accomplished the following:

 * A domain name is set to route to our JupyterHub server
 * We produced an SSL certificut with certbot
 * We created the three security files
 
The next step is to install and configure Nginx.

[TOC]

## What is Nginx?

Nginx is an open-source web server that can handle many concurrent web connections at the same time. For the Nginx installation, I followed [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04) from Digital Ocean.

## Update and install Nginx

Log into the server, update the system, and install Nginx with the apt package manager.

```text
$ sudo apt-get -y update && sudo apt-get -y upgrade
$ sudo apt-get install nginx
```

Digital Ocean installs a firewall application called **ufw**. Depending on which steps you followed before, ufw may be blocking some ports and keeping other ports open. You can see which ports are open with the command below:

```text
$ sudo ufw status
```

The results may look something like the listing below. It depends on if the ports opened in the previous steps were closed after the step was completed.

```text
Status: active

To                         Action      From
--                         ------      ----
8000                       DENY        Anywhere                  
OpenSSH                    ALLOW       Anywhere                  
80                         DENY        Anywhere                  
8000 (v6)                  DENY        Anywhere (v6)             
OpenSSH (v6)               ALLOW       Anywhere (v6)             
80 (v6)                    ALLOW       Anywhere (v6)             
```

You can check out which apps the ufw firewall can work by typing the command:

```text
$ sudo ufw app list
```

We see the list of available ufw configurations include Nginx:

```text
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
```

We want to allow in both http and https requests. Once a http request comes in, we'll use Nginx to convert the http connection to a https connection. 

Select ```Nginx full```. Note the **C**apitalization in the command and the quoation marks ```' '```:

```text
$ sudo ufw allow 'Nginx Full'
```

We can check out which ports ufw is allowing through after the added Nginx with the ```status``` command:

```text
$ sudo ufw status
```

Note the output shows ufw allows ```Nginx Full``` and requests over port 8000. We opened port 8000 earlier, so we could see how JupyterHub works without a domain name or SSL.  If port 80 is still open, now is a good time to close it.

```text
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere
8000                       DENY        Anywhere
80                         ALLOW       Anywhere
Nginx Full                 ALLOW       Anywhere
OpenSSH (v6)               ALLOW       Anywhere (v6)
8000 (v6)                  DENY        Anywhere (v6)
80 (v6)                    ALLOW       Anywhere (v6)
Nginx Full (v6)            ALLOW       Anywhere (v6)
```

Nginx will start running as soon at it is installed. We can see the Nginx's status with:

```text
$ sudo systemctl status nginx
```

In the output, we should see something like below. This means Nginx is running. Key in [ctrl-c] to exit the status dashboard.

```text
Active: active (running) since Thu 2018-05-17 04:51:16 UTC; 15min ago
Main PID: 17126 (nginx)
  CGroup: /system.slice/nginx.service
    ├── 17126 nginx: master process /usr/sbin/nginx -g daemon on; master_pr
    └── 17127 nginx: worker process
```

Now we can browse over to the domain (the domain we set up with Digital Ocean DNS dashboard and Google Domains) and see the Nginx start page.

![nginx welcome page](images/welcome_to_nginx.png)

## Next Steps

Now that Nginx is installed, the next step is to configure Nginx to use our SSL certificate and dhparm.pem file we created in a previoous step. Only a couple more steps before we can open up JupyterHub using https.

<br>
