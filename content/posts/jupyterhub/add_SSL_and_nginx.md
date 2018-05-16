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
2. Use let's encrypt to generate SSL keys
3. Create jupyterhub_config.py and modify
4. Install nginx and modify nginx_conf
5. Start restart nginx and start jupyterhub. See if we can log in.
6. Create another system user on the server. Restart jupyterhub and log in as new user.

### Summary

### Next Steps

