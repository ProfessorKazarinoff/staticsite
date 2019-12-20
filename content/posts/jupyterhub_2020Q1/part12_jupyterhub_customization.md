Title: JupyterHub Deployment Part 12: JupyterHub Configuration
Date: 2009-12-19 12:40
Modified: 2019-12-19 12:40
Status: draft
Category: jupyterhub
Tags: jupyter, jupyterhub, jupyter notebooks, python, cloud server
Slug: jupyterhub-depolyment-jupyerhub-config
Authors: Peter D. Kazarinoff
Series: JupyterHub Deployment
Series_index: 12
This is the 12th part of a multi-part series that shows how to deploy JupyterHub on Digital Ocean. In this post, we'll create and modify the JupyterHub configuration file ```jupyerhub_config.py```. In the config file, we'll specify the locations of our cookie secret and proxy auth token as well as give ourself admin privaleges so we can monitor user's servers when they log into JuypyterHub.

[TOC]

## Create jupyterhub_config.py

We'll create the JupyterHub config file in the ```/etc/jupyterhub``` directory. After the directory is created, we need to modify the directory permissions. Then ```cd``` into it create the config file with ```jupyterhub --generate-config```. Make sure you are in the ```(jupyterhubenv)``` virtual environment when you run the ```--generate-config``` command.  

```text
$ cd /etc
$ sudo mkdir jupyterhub
$ sudo chown -R root:peter jupyterhub/
$ sudo chmod -R g+rwx jupyterhub/
$ cd jupyterhub
$ conda activate jupyterhubenv
(jupyterhubenv)$ jupyterhub --generate-config
Writing default config to: jupyterhub_config.py
$ ls
jupyterhub_config.py
```

## Modify jupyterhub_config.py

Now we'll modify the ```jupyterhub_config.py``` file to allow local spawners and include our user ```peter``` as an admin user:

```text
$ nano jupyterhub_config.py
```

There will be a lot of commented out text in the ```jupyterhub_config.py``` file. At the top of the file, add the following:

```python
# /etc/jupyterhub/jupyterhub_config.py

c = get_config()
c.JupyterHub.log_level = 10

# Cookie Secret Files
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'
c.ConfigurableHTTPProxy.auth_token = '/srv/jupyterhub/proxy_auth_token'

c.Authenticator.whitelist = {'peter'}
c.Authenticator.admin_users = {'peter'}

```

<br>

## Restart nginx and start JupyterHub, see if we can login

Now we'll restart Nginx and start JupyterHub. Note that this time when we start JupyterHub we don't need to use the ```--no-ssl``` flag. This is because we have SSL running on Nginx. 

If it seems like Nginx isn't working, try ```sudo systemctl status nginx``` and see if Nginx really started. If it didn't, try the command ```nginx -t```. This command prints out any error messages if Nginx failed to start. I had to troubleshoot Nginx for a while before I got Nginx and JupyterHub working together properly.

```text
$ sudo systemctl stop nginx
$ sudo systemctl start nginx
$ sudo systemctl status nginx
# [ctrl-c] to exit
```

Once Nginx is running, restart JupyterHub without the ```--no-ssl``` flag. Make sure the ```(jupyterhubenv)``` virtual environment is active before running the ```jupyterhub``` command.

```text
$ cd /etc/jupyterhub
$ conda activate jupyterhubenv
(jupyterhubenv)$ jupyterhub
```

If you encounter an error that has something to do with the ```juyterhub_cookie_secret``` or ```proxy_auth_token``` files, this is because the permissions of these files doesn't all the ```peter``` user to read them. The commands below temporarily modify the permissions. This should allow JupyterHub to start. Just remember to change the permissions back to ```600``` as stated in the JupyterHub docs.

```text
$ cd /srv/jupyterhub
$ ls -la
$ sudo chown :peter jupyterhub_cookie_secret 
$ sudo chmod g+r jupyterhub_cookie_secret 
$ sudo chown :peter proxy_auth_token 
$ sudo chmod g+r proxy_auth_token 
$ ls -la
```

Now, try going back to the ```/etc/jupyterhub``` directory and starting JupyterHub back up again. Make sure the ```(jupyterhubenv)``` is activate before you run the comand.

```text
(jupyterhubenv)$ cd /etc/jupyterhub
(jupyterhubenv)$ jupyterhub
```

Log in to JupyterHub with the non-root sudo username (```peter```) and password (same user that's running the PuTTY session). 

![Jupyterhub login screen](images/jupyterhub_pam_spawner_login.png)

Now we can browse to our domain and see JupyterHub running in its full SSL glory.

![Jupyterhub login screen](images/nb_file_browser_new_notebook.png)

Now back at the server, if you shut down JupyterHub with ```[Ctrl-c]``, you should see the notebook you just created.

```text
# [Ctrl-c] to exit
(jupyterhubeve)$ cd ~
(jupyterhubeve)$ ls
test_notbook.ipynb
```

## Create an new user, restart JupyterHub and Login.

OK, it's all well and good that we can log in. But the purpose of setting up JupyterHub is for multiple people to be able to log on an run Python code. To test if multiple people can run Python code on JupyterHub at the same time, we need to create another user on the server.

If JupyterHub is still running, stop it with [Ctrl] + [c].  Let's create a new user and see if we can log in as her.

```text
$ sudo adduser gabby
```

Go through the prompts and remember the UNIX password. Now we'll modify ```jupyterhub_conf.py``` to include our new user ```gabby``` and add ```peter``` (our non-root sudo user) as an administrator:

```text
(jupyterhubenv)$ pwd
# should be in /etc/jupyterhub
(jupyterhub)$ nano jupyterhub_config.py
```

Using the Nano text editor add the new user to the authenticator whitelist.

```text
# /etc/jupyterhub/jupyterhub_config.py
...

c.Authenticator.whitelist = {'peter','gabby'}
c.Authenticator.admin_users = {'peter'}

```

Restart JupyterHub and try and login as ```gabby```

```
(jupyterhubenv)$ jupyterhub
```

![login as gabby](images/jh_sign_in_gabby.png)

After we confirm two different users can log into JupyterHub, we need to make sure that we re-set the permissions of the ```jupyterhub_cookie_secret``` and ```proxy_auth_token``` files.

```text
# [Ctrl-c] to stop jupyterhub
(jupyterhubenv)$ conda deactivate
$ cd /srv/jupyterhub
$ ls -la
$ sudo chmod 600 proxy_auth_token
$ sudo chmod 600 jupyterhub_cookie_secret
$ ls -la
```

## Next Steps

The next step is to run JupyterHub as a system service. This allows JupyterHub to run continuously even if we aren't logged into the server. It also allows us to work on our JupyterHub deployment while it is still running.

<br>
