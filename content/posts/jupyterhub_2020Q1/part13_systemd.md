Title: JupyterHub Deployment Part 13: Run JupyterHub as a System Service
Date: 2009-12-19 12:40
Modified: 2019-12-19 12:40
Status: draft
Category: jupyterhub
Tags: jupyter, jupyterhub, jupyter notebooks, python, cloud server
Slug: jupyterhub-depolyment-systemd
Authors: Peter D. Kazarinoff
Series: JupyterHub Deployment
Series_index: 13
This is the 13th part of a multi-part series about how to deploy JupyterHub on Digital Ocean. In this post, we'll run JupyterHub as a system service, instead of running JupyterHub from the commandline. Running JupyerHub as a system service allows JupyterHub to run continously even if we aren't logged into the server. It also keeps JupyterHub running while when we log into the server and make any changes.

[TOC]

## Create a jupyterhub.service file

To run JupyterHub as a system service (according to [this wiki](https://github.com/jupyterhub/jupyterhub/wiki/Run-jupyterhub-as-a-system-service)
), we need to create a service file in the ```/etc/systemd/system``` directory. ```cd``` into the directory and have a look around. We see a couple files that end in ```.service```

```text
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

Create a new ```.service``` file called ```jupyterhub.service```

```text
$ sudo nano jupyterhub.service
```

In the ```jupyterhub.service``` file, add the following. Note that as part of the ```PATH``` environment variable ```/opt/miniconda3/envs/jupyterhubenv/bin/``` is included. This is the path to our virtual environment. As part of the ```ExecStart=``` section, include a flag for our JupyterHub config file located at  ```/etc/jupyterhub/jupyterhub_config.py```. 

```text
[Unit]
Description=JupyterHub
After=syslog.target network.target

[Service]
User=root
Environment="PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/miniconda3/envs/jupyterhubenv/bin/"
ExecStart=/opt/miniconda3/envs/jupyterhubenv/bin/jupyterhub -f /etc/jupyterhub/jupyterhub_config.py

[Install]
WantedBy=multi-user.target
```

Save and exit the nano text editor with [Ctrl-x] + [Enter]. 

## Reload the systemd daemon and start the system service

Now we need to reload the system daemon and run JupyterHub as a system service using the command: ```sudo systemctl <start|stop|status> jupyterhub```

```text
$ sudo systemctl daemon-reload
$ sudo systemctl start jupyterhub
```

We can see if JupyterHub is running with:

```
$ sudo systemctl status jupyterhub

 Loaded: loaded (/etc/systemd/system/jupyterhub.service; 
 Active: active (running)
```

<br>

## Test local OAuth

Now we can go to the server and log in as our non-root user ```peter```.

![JupyterHub PAM Login](images/jupyterhub_no_ssl_login.png)

 > A couple times I thought that JupyterHub was running after using ```systemctl start jupyterhub```, but the JupyterHub wasn't working when I went to the server's web address. It turned out that JupyterHub wasn't running when I keyed in ```systemctl status jupyterhub```. Most times looking for an error and tracking down the the error worked, but one time it seemed to be a problem with the http-configurable-proxy. 

The following command shuts down the proxy if you get stuck like I did (insert the number corresponding to the configurable-http-proxy process after the ```kill``` command):

```text
$ ps aux | grep configurable-http-proxy
$ kill #### 
```

## Next Steps

The next step is to have JupyterHub accept Google usernames and passwords. This allows students with college email accounts to log into JupyterHub and means we don't have to deal with creating new users and sending people usernames and passwords.

<br>
