﻿Title: Adding SSL and a domain name to Jupyter Hub
Date: 2018-05-16 12:40
Modified: 2018-05-16 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: add-ssl-and-domain-name-to-jupyterhub
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 5
Summary: This is the fifth part of a multi-part series that shows how to set up Jupyter Hub for a college class. In this post, we are going to link a domain name to our server IP address, add SSL security and configure nginx to run as a proxy in between users and jupyterhub. Then we'll run jupyterhub over https using the SSL security we created.

This is the fifth part of a multi-part series that shows how to set up Jupyter Hub for a college class. In this post, we are going to link a domain name to our server IP address, add SSL security and configure nginx to run as a proxy in between users and jupyterhub. Then we'll run jupyterhub over https using the SSL security we created.

### Posts in this series

1. [Why Jupyter Hub?]({filename}/posts/jupyterhub/why_jupyter_hub.md) 
2. [Create ssh key, save to documents/ssh-keys]({filename}/posts/jupyterhub/PuTTYgen_ssh_key.md)
3. [Create a new Digital Ocean Droplet with a non-root sudo user]({filename}/posts/jupyterhub/new_DO_droplet.md)
4. [Install Jupyter Hub on the server]({filename}/posts/jupyterhub/installing_jupyterhub.md)
5. **Apply SSL, link a domain name to the server and configure nginx** (this post)
6. Connect OAuth to Jupyter Hub
7. Connect to Jupyter Hub as student

### Last time

In the last post, we installed **Anaconda** on the server using a shell script. Then we installed some extra **Python** packages such as **pint**, **pyserial** and **schemdraw** to our base conda environment. Next we installed **jupyterhub**, opened up port 8000 and ran jupyterhub for the first time! And remember **we shut down jupyter hub very quickly** because we ran it without any SSL security.

### Steps in this post:

1. Link domain name to server IP address
2. Install nginx
3. Use cirtbox to generate SSL certificates
4. Create jupyterhub_config.py and modify
5. modify nginx_conf
6. Start restart nginx and start jupyterhub. See if we can log in.
7. Create another system user on the server. Restart jupyterhub and log in as new user.

### 1. Link domain name to server IP address

When we started Jupyter Hub in the previous post, it ran, we could log in, and we could run Python code. What's not to like, right? Well, security is the big problem. 

In the initial setup, Jupyter Hub was running under regular http, not https. With a web application that has usernames and passwords, like Jupyter Hub, having https and SSL security is best. In order to use https, we need to get an SSL certificate. And that SSL certificate should correspond to the domain name linked to our server. So the first step is getting the domain name and pointing it at Digital Ocean. The next step is linking the domain name to our Jupyter Hub server.

#### Google Domains

I purchased the domain _problemsolvingwithpython.com_ from [google domains](https://domains.google.com). It costs $12/year which seems pretty reasonable and was easy to set up. After purchasing the domain, I added the Digital Ocean DNS servers as a set of custom name servers to my domain options on google domains.

![Google Domains Dashboard](/posts/jupyterhub/google_domains_list.png)

To add a set of custom name servers, click the the button with the two bars under the DNS header. This will bring up a page where you can enter in the Digital Ocean DNS servers. The name servers to add are:

```
ns1.digitalocean.com
ns2.digitalocean.com
ns3.digitalocean.com
```

![Google Domains Dashboard](/posts/jupyterhub/google_domains_dns_routing.png)

Make sure to click the radio button [Use custom name servers]

#### Digital Ocean DNS

Now we are going to set our domain _problemsolvingwithpython.com_ to link to the IP address of our server on Digital Ocean. Log into Digital Ocean and in the upper right select [Create] --> [Domains/DNS]

![DO Domains/DNS](/posts/jupyterhub/DO_manage_domains.png)

In the [Add a domain] field, type in the domain name without http, but including .com (or .edu/.org/.net) then click [Add Domain].

![DO Domains/DNS](/posts/jupyterhub/DO_add_domain.png)

This will bring us to a panel you can add a DNS record. I want the notebook server to have the web address _https://notebooks.problemsovlingwithpython.com_, so I entered ```notebooks``` in the text field. Then select the droplet (server) that you want the web address to route to.

![DO Domains/DNS](/posts/jupyterhub/DO_sub_domain.png)
 
 After completing this step, there will be a number of new DNS records. The ones I set up are below:
 
![DO Domains/DNS](/posts/jupyterhub/DO_domains_routed.png)

It takes a couple minutes for the DNS switchover to complete. [https://www.whatsmydns.net](https://www.whatsmydns.net) can be used to check the NS and A records of your domain and see if the domain name is getting through. The first time I set up DNS on Digital Ocean, I added the custom DNS servers to google domains but neglected to select the [use custom name servers] radio button. It looked like the domain was routing to Digital Ocean, but actually it was just staying with google. Once I clicked the [use custom name servers] radio button and waited a couple minutes, the change over happened. It did take a bit of time though; not hours, but more than a few minutes.

### 2. Install nginx and modify ufw and nginx_conf

Now that the domain name is set up,the next step is to install and configure nginx. Nginx is an open source web server that can handle many concurrent web connections all at the same time. For the installation, I followed [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04) from Digital Ocean

Use PuTTY to connect to the server with the non-root sudo user we set up before. My non-root user is called ```peter```. Once logged in, we can update the system and install nginx.

```
$ sudo apt-get update
$ sudo apt-get install nginx
```

Digital Ocean installs a firewall application called ufw. Check out which apps the ufw firewall is working with:

```
$ sudo ufw app list
```

We see a list of available ufw configurations to work with nginx. 

```
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
```

We want to allow in both http and https requests. Once a http request comes in, we will use nginx to convert it to an https connection. Select nginx full. Note the Capitalization in the command:

```
$ sudo ufw allow 'Nginx Full'
```

We can check out which ports ufw is allowing through with:

```
$ sudo ufw status
```

Note in the output how ufw is allowing nginx full and requests over port 8000. We opened port 8000 earlier, so we could see how jupyterhub works without a domain name or SSL.  Once we get nginx running and hooked up to jupyterhub, we need to remember to close off port 8000 in ufw.

```
Status: active

To                         Action      From
--                         ------      ----
22                         LIMIT       Anywhere
2375/tcp                   ALLOW       Anywhere
2376/tcp                   ALLOW       Anywhere
8000                       ALLOW       Anywhere
Nginx Full                 ALLOW       Anywhere
22 (v6)                    LIMIT       Anywhere (v6)
2375/tcp (v6)              ALLOW       Anywhere (v6)
2376/tcp (v6)              ALLOW       Anywhere (v6)
8000 (v6)                  ALLOW       Anywhere (v6)
Nginx Full (v6)            ALLOW       Anywhere (v6)
```

nginx will start running as soon at it is installed. We can see the status with:

```
$ sudo systemctl status nginx
```

In the output, we can see something like below. This mean nginx is running.

```
 Active: active (running) since Thu 2018-05-17 04:51:16 UTC; 15min ago
 Main PID: 17126 (nginx)
   CGroup: /system.slice/nginx.service
           ├─17126 nginx: master process /usr/sbin/nginx -g daemon on; master_pr
           └─17127 nginx: worker process
```

So we can browse over to the domain name (the domain we set up with Digital Ocean and google domains) and we should see the nginx start page.

![nginx welcome page](/posts/jupyterhub/welcome_to_nginx.png)

### 3. Obtain SSL certificates with certbot

With a domain name hooked up to our server, we are now able to obtain an SSL certificate. I followed [this presentation](https://www.slideshare.net/willingc/jupyterhub-tutorial-at-jupytercon) to install certbot, a program used to generate SSL certificates. 

```
$ cd ~
$ mkdir certbot
$ cd certbot
$ wget https://dl.eff.org/certbot-auto
$ chmod a+x certbot-auto
```

Before we can run certbot, we need to turn off nginx. When I first tried to run certbot, I got an error that read:

```
Problem binding to port 80: Could not bind to IPv4 or IPv6.
```

Since we installed nginx earlier, and we confirmed that it's running, that means that port 80 is currently in use by nginx. We need to open up port 80 to certbot by temporarily shutting down nginx. Once nginx is stopped, we can run cirtbot and get our SSL certificate. We'll have to restart nginx, but that can wait until we change the nginx configuration file. If you are following along, make sure to change ```notebooks.problemsolvingwithpython.com``` to your domain.

```
$ sudo systemctl stop nginx
$ sudo systemctl status nginx
# [Ctrl] + [c] to exit
$ ./certbot-auto certonly --standalone -d notebooks.problemsolvingwithpython.com
```

If it worked and we got our SSL certificate, the output will be something like:

```
IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/notebooks.problemsolvingwithpython.com/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/notebooks.problemsolvingwithpython.com/privkey.pem
   Your cert will expire on 2018-08-15. 
```

Note the location of the ```fullchain.pem``` and ```privkey.pem``` files. We'll need to put these locations into the nginx configuration.

### 4. Modify nginx config

The next step is to modify the nginx config file so that nginx uses our SSL certificates and routes requests on to jupyterhub.

### 5. Generate jupyterhub_config.py and modify

```
$ cd ~
$ jupyterhub --generate-config
```





### 6. Restart nginx and start jupyterhub, see if we can login

### 7. Create an new user and restart jupyterhub. See if new user can log in.

### Summary




### Next Steps
