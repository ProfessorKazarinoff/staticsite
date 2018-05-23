Title: Adding Google OAuth and system service to a Jupyter Hub server
Date: 2018-05-22 12:40
Modified: 2018-05-22 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: add-google-oauth-and-system-service-to-jupyterhub
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 6
Summary: This is the sixth part of a multi-part series that shows how to set up Jupyter Hub for a college class. In this post, we will add an authentication system so that users can log into our Jupyter Hub server using their college usernames and passwords. We will also set **jupyterhub** to run as a system service in the background which will allow us to work on the server and run **jupyterhub** at the same time.

This is the sixth part of a multi-part series that shows how to set up Jupyter Hub for a college class. In this post, we will add an authentication system so that users can log into our Jupyter Hub server using their college usernames and passwords. We will also set **jupyterhub** to run as a system service in the background which will allow us to work on the server and run **jupyterhub** at the same time.

### Posts in this series

1. [Why Jupyter Hub?]({filename}/posts/jupyterhub/why_jupyter_hub.md) 
2. [Create ssh key, save to documents/ssh-keys]({filename}/posts/jupyterhub/PuTTYgen_ssh_key.md)
3. [Create a new Digital Ocean Droplet with a non-root sudo user]({filename}/posts/jupyterhub/new_DO_droplet.md)
4. [Install Jupyter Hub on the server]({filename}/posts/jupyterhub/installing_jupyterhub.md)
5. [Apply SSL, link a domain name to the server and configure nginx]({filename}/posts/jupyterhub/SSL_and_nginx_with_jupyterhub.md)
6. **Connect OAuth to Jupyter Hub** (this post)
7. Connect to Jupyter Hub as student

### Last time

In the last post, we succceed in getting jupyterhub to run on https and use SSL cirtificuts. We created SSL cirtifuicuts, modified the nginx config and modified the jupyterhub config. At the end of it we were able to get a working version of jupyter hub running SSL security.

### Steps in this post:

1. Run **jupterhub** as a system service
2. Test local OAuth
3. Aquire google OAuth credentials
4. Modify jupyterhub_config.py to use google OAuth.
5. Start restart nginx and start jupyterhub. See if we can log in using google credentials.


### 1. Run **jupterhub** as a system service

Working off of [this wiki](https://github.com/jupyterhub/jupyterhub/wiki/Run-jupyterhub-as-a-system-service)

To run jupyterhub as a system service, we need to create a service file in the ```/etc/systemd/system``` directory. ```cd``` into the directory and have a look around. You should see a couple files that end in ```.service```

```
$ cd /etc/systemd/system
$ ls
cloud-init.target.wants                network-online.target.wants
dbus-org.freedesktop.thermald.service  paths.target.wants
default.target.wants                   sockets.target.wants
final.target.wants                     sshd.service
getty.target.wants                     sysinit.target.wants
graphical.target.wants                 syslog.service
iscsi.service                          timers.target.wants
multi-user.target.wants
```

Next we'll create a new ```.service``` file called ```jupyterhub.service```

```
$ sudo nano jupyterhub.service
```

In the file, add the following:

```
[Unit]
Description=Jupyterhub
After=syslog.target network.target

[Service]
User=root
Environment="PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/home/peter/anaconda3/bin"
ExecStart=/home/peter/anaconda3/bin/jupyterhub -f /home/peter/jupyterhub_config.py

[Install]
WantedBy=multi-user.target
```

Save and exit with [Ctrl-c] + [y]. Now we need to reload the system daemon and run jupyterhub as a system process using the command: ```sudo systemctl <start|stop|status> jupyterhub```

```
$ sudo systemctl daemon-reload
$ sudo systemctl start jupyterhub
```

We can see if jupyterhub is running with:

```
$ sudo systemctl status jupyterhub

 Loaded: loaded (/etc/systemd/system/jupyterhub.service; 
 Active: active (running)
```

Now we can go to the server and log in as our non-root user, and log in as the other user we created ```kendra```

A problem is that if we go to the admin page on jupyter hub, we can't add new users. The users have to be added to the server using PuTTY first and then can be added to jupyterhub with the admin pannel. This is OK for a small team or a couple users, but for a college class, creating a new user on the server for each student, then emailing out passwords... That will end up a mess. So we need to give jupyterhub the authority to create new users from the admin panel and we need a way to have users login with a user name and password that they already have.



Something similar to this in jupyterhub_config.py

```
#jupyterhub_config.py

c.LocalGoogleOAuthenticator.create_system_users = True
```

### 2. Github Authenticator

One of the ways that students could log into Jupyter Hub is using their github credentials. This would force each student to set up a github account, but that might be worth it to give them the exposure to git as a tool. So let's give the github authenticator a whirl. It is an authenticator that is pretty well documented for Jupyter Hub.

First we need to install **oauthenticator**. I couldn't find oauthenticator on conda-forge. If it is on conda-forge, I would install it from there rather than PyPI. But for this one, I used pip

```
pip install conda install oauthenticator
```

Edit the ```jupyterhub_config.py``` file to include the following lines:

```
from oauthenticator.github import LocalGitHubOAuthenticator
c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator

c.LocalGitHubOAuthenticator.oauth_callback_url = 'https://notebooks.problemsolvingwithpython.com/hub/oauth_callback'
c.LocalGitHubOAuthenticator.client_id = 'xxxxxxxxxxxxxxxxxxxxxx'
c.LocalGitHubOAuthenticator.client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

c.LocalGitHubOAuthenticator.create_system_users = True
#c.Authenticator.whitelist = {'peter','mnk1','kendra','holly'}
#c.Authenticator.admin_users = {'peter'}

```


### Summary
Up next will add an authentication system so that users can log into our Jupyter Hub server using their college usernames and passwords. We will also set **jupyterhub** to run as a system service in the background which will allow us to work on the server and run **jupyterhub** at the same time.



### Next Steps
Up next will add an authentication system so that users can log into our Jupyter Hub server using their college usernames and passwords. We will also set **jupyterhub** to run as a system service in the background which will allow us to work on the server and run **jupyterhub** at the same time.

