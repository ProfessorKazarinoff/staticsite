Title: Adding SSL and a domain name to Jupyter Hub
Date: 2018-05-16 12:40
Modified: 2018-05-16 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: add-ssl-and-domain-name-to-jupyterhub
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 4
Summary: This is the fourth part of a multi-part series that shows how to set up Jupyter Hub for a college class. In this post, we are going to add SSL security, link a domain name to our server IP address and configure nginx to run as a proxy in between users and jupyterhub. Then we'll run jupyterhub over https using the SSL security we created.

This is the fourth part of a multi-part series that shows how to set up Jupyter Hub for a college class. In this post, we are going to add SSL security, link a domain name to our server IP address and configure nginx to run as a proxy in between users and jupyterhub. Then we'll run jupyterhub over https using the SSL security we created.

### Posts in this series

1. Why Jupyter Hub? 
2. Create ssh key, save to documents/ssh-keys
3. Create a new Digital Ocean Droplet with a non-root sudo user
4. Install Jupyter Hub on the server
5. Apply SSL, link a domain name to the server and configure nginx (this post)
6. Connect OAuth to Jupyter Hub
7. Connect to Jupyter Hub as student

### The last post

In the last post, we installed Anaconda on the server using a shell script. Then we installed some extra python packages such as pint and pyserial to our base conda environment. Next we installed jupyterhub, opened up port 8000 and ran jupyterhub for the first time! And remember we **shut down jupyter hub very quickly** because we ran it without any SSL security.

### Steps in this post:

1. Link domain name to server IP address
2. Install nginx
3. Use cirtbox to generate SSL certificates
4. Create jupyterhub_config.py and modify
5. modify nginx_conf
6. Start restart nginx and start jupyterhub. See if we can log in.
7. Create another system user on the server. Restart jupyterhub and log in as new user.

### 1. Link domain name to server IP address

Go to digital ocean dns control pannel. Add domain name. Link domain name to droplet.

It takes a couple minutes of waiting until the dns switchover happens. [https://www.whatsmydns.net](https://www.whatsmydns.net) can be used to check the NS and A records of your domain and see if they are getting through. The first time I set it up, I added the custom dns servers to google domains but I neglected to select the custom dns servers radio box. So it looked like the domain was going to digital ocean, but actually it was just staying with google. Once I clicked the radio box and waited a coulple minutes, the change over happened. It did take a bit though. Not hours, but a few minutes.

### 2. Install nginx and modify ufw and nginx_conf

Following [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04) from Digital Ocean

Install nginx

```
$ sudo apt-get update
$ sudo apt-get install nginx
```

Check out which apps the ufw firewall is working with. 

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

### 3. Obtain ssl certificates with certbot

From [this presentation](https://www.slideshare.net/willingc/jupyterhub-tutorial-at-jupytercon)

Install certbot

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

Since we installed nginx earlier, and we confirmed that it's running, that means that port 80 is currently in use by nginx. We need to open up port 80 to certbot by temporarily shutting down nginx. Once nginx is stopped, we can run cirtbot and get our SSL certificate. We'll have to restart nginx, but that can wait until we change the nginx configuration file.

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

### 4. Generate jupyterhub_config.py and modify

```
$ cd ~
$ jupyterhub --generate-config
```

### 5. Modify nginx config



### 6. Restart nginx and start jupyterhub, see if we can login

### 7. Create an new user and restart jupyterhub. See if new user can log in.

### Summary




### Next Steps

