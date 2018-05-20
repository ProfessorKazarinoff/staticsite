Title: Installing Jupyterhub
Date: 2018-05-21 12:40
Modified: 2018-05-21 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: installing-jupyter-hub
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 4
Summary: This is the third part of a multi-part series that shows how to set up Jupyter Hub for a college class. The goal is to have a running version of Jupyter Hub that students in the class can log into when given a simple web link. In this post, we'll get to the fun stuff: installing Jupyter Hub on the server, installing Python packages and spinning up Jupyter Hub for the first time.

This is the third part of a multi-part series that shows how to set up Jupyter Hub for a college class. The goal is to have a running version of Jupyter Hub that students in the class can log into when given a simple web link. In this post, we'll get to the fun stuff: installing Jupyter Hub on the server, installing Python packages and spinning up Jupyter Hub for the first time.

### Posts in this series

1. [Why Jupyter Hub?]({filename}/posts/jupyterhub/why_jupyter_hub.md) 
2. [Create ssh key, save to documents/ssh-keys]({filename}/posts/jupyterhub/PuTTYgen_ssh_key.md)
3. [Create a new Digital Ocean Droplet with a non-root sudo user]({filename}/posts/jupyterhub/new_DO_droplet.md)
4. **Install Jupyter Hub on the server** (this post)
5. Apply SSL, link a domain name to the server and configure nginx
6. Connect OAuth to Jupyter Hub
7. Connect to Jupyter Hub as student

### The last post

In the last post we created a new server on Digital Ocean (called a _droplet_) and made sure to add our public SSH key to the setup options. Then we logged into the server as ```root```  with our private SSH key. As ```root```, we set up a new user with sudo privileges (our new user was called ```peter```) and added our public SSH key to the new users profile. Then we logged into the server as the new user and checked the new user's home directory.


### This post

1. Update packages on the server
2. Install **Anaconda**
3. Install **Python** packages and **jupyterhub** 
4. Run very unsecure instance of Jupyter Hub just to see if it works
5. Shut down Jupyter Hub very quickly because of no SSL security



#### 1. Update Packages

It is probably best to update the packages installed on the server in case there are changes and updates to the operating system since the server was created. This is probably a reflex for those that use Linux a lot. Open PuTTY and log into the server as the non-root sudo user we created in the last post. Then update the system:

```
$ sudo apt-get update
```


#### 2. Install Anaconda

Next we'll install **Anaconda**. When I install Anaconda on Windows10 I used an msi installer, but for installation on the cloud server we'll use a shell script. The second time I set up Jupyter Hub, I installed Anaconda in the ```/opt``` directory. I don't think this is the best setup. When I installed Anaconda in ```/opt```, I ended up with all sorts of permission problems when I tried to run **conda** and **jupyterhub**. It is probably better to install it in the users home directory. The users home directory is also the default Anaconda3 installation location.

I'm following [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04) from Digital Ocean.

Go to [https://repo.continuum.io/archive/](https://repo.continuum.io/archive/) and look down the list of installs for the newest installer that corresponds to:

 * Anaconda 3 (not Anaconda 2, we don't want legacy Python version 2.7)
 * Linux
 * x86
 * 64 (bit)
 * .sh (linux shell script)

While I write this post, the shell script is:

```
Anaconda3-5.1.0-Linux-x86_64.sh
```

We'll ```cd``` into the ```/tmp``` directory and download the script. Then we run the script and follow the prompts.

```
$ cd /tmp
$ curl -O https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
$ bash Anaconda3-5.1.0-Linux-x86_64.sh
```

We want to be able to run **conda** from the command line. So make sure to allow **Anaconda** to append your PATH during the installation. After installation, we need to reload the ```.bashrc``` file because Anaconda made changes to ```.bashrc``` during the install (when it added conda to our PATH).

```
$ source ~/.bashrc
```

Now we should be able to run **conda**. Try:

```
$ conda --version
```

If you see output, that means conda was installed and can be run by the user.

We have a full installation of Anaconda which includes a lot of useful packages for engineers including: numpy, pandas, matplotlib, scipy, sympy, bokeh and holoviews. Anaconda also includes other useful packages such as requests, beautiful soup and attrs. And for student who want to go further, the Anaconda distribution contains django, flask, tk, tornado and scikit-learn.

There are a couple other packages I want to install in addition to the standard Anaconda packages. First are some extra packages useful for engineers: pint, pyserial and schemdraw.

```
$ conda install -c conda-forge pint
$ conda install -c anaconda pyserial
$ pip install SchemDraw
```

Now we'll install Jupyter Hub! Since we are using conda to install jupyterhub (rather than pip), we don't need to install node and configurable-http-proxy separably. Conda installs the non-python dependances (like node and configurable-http-proxy) that jupyter hub relies upon.

```
$ conda install -c conda-forge jupyterhub
$ conda install notebook
```

OK let's give it a whirl. Start jupyterhub for the first time. Note the ```--no-ssl``` flag at the end. This needs to be included or you won't be able to browse to the server.

```
$ jupyterhub --no-ssl
```

You should see some output in the PuTTY window. The last line should be something like ```JupyterHub is now running at http://:8000/```. The first time I set up Jupyter Hub, I wasn't able to see the site using a web browser. Nothing would come up and the connection would time out.

![anaconda in start menu](/posts/jupyterhub/site_can't_be_reached.png)

Why? It turns out Digital Ocean installs a firewall called ufw by default and turns the ufw firewall on. When the server was created, ufw was configured to only allow incoming connections on ports 22, 80 and 433. This output is shown when we first log into the server:

```
"ufw" has been enabled. All ports except 22 (SSH), 80 (http) and 443 (https)
have been blocked by default.
```

But **jupyterhub runs on port 8000**. So we need to tell ufw to allow connections on port 8000 (at least for now, just to see if jupyterhub works). To allow communication on port 8000 and restart jupyterhub, type:

```
$ sudo ufw allow 8000
$ jupyterhub --no-ssl
```

Now we can browse to the server IP address appended with ```:8000```. The web address should look something like: http://165.228.68.178:8000. You can find the IP address of the server by going into the digital ocean dashboard. We should see:

![jupyter hub no ssl login](/posts/jupyterhub/jupyterhub_no_ssl_login.png)

Awesome! Quick log into **jupyterhub** using the username and password for the non-root sudo user (in my case ```peter```) that we set up and are using in our current PuTTY session. You should see the typical notebook file browser with all the files you can see when you run ```ls ~/```. This shows the contents of the user's home directory. Try creating and running a new notebook. Should work just like a **jupyter notebook running locally**.

### Quick! Log out and shut down jupyterhub

**Quick! Log out and shut down jupyterhub**. The site is running without any ssl security over regular HTTP not HTTPS. Key in [Ctrl] + [c] to stop jupyterhub.

<div class="alert alert-warning" role="alert">
  <strong>Warning!</strong>You should not run JupyterHub without SSL encryption on a public network.
</div>

 
### Summary

In this post we installed Anaconda on the server using a shell script. We added conda to our path and reloaded our .bashrc file. Then we installed some extra python packages such as pint and pyserial. Finally we installed jupyterhub, opened up port 8000 and ran jupyterhub for the first time! Remember we **shut down jupyter hub very quickly** because we ran it without any SSL security.

### Next Steps

In the next post we will build SSL security into our Jupyterhub deployment and connect the server to domain name. Plus we'll customize the jupyter hub config file.

