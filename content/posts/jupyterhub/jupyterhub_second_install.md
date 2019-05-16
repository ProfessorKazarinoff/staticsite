Title: Installing Jupyterhub
Date: 2018-10-29 12:40
Modified: 2018-10-29 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: installing-jupyter-hub-the-second-time
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Summary: This is the second time that I've set up JupyterHub to run for a college class. This time, I am making a couple of chnages to the deployment. This post is a record of those changes. To see how to set up JupyterHub for your ownn college class, see my previous series on JupyterHub starting with [Why Jupyter Hub?]({static}/posts/jupyterhub/why_jupyter_hub.md) 

This is the second time that I've set up JupyterHub to run for a college class. This time, I am making a couple of chnages to the deployment. This post is a record of those changes. To see how to set up JupyterHub for your ownn college class, see my previous series on JupyterHub starting with [Why Jupyter Hub?]({static}/posts/jupyterhub/why_jupyter_hub.md) 

### Posts in the JupyterHub installation series

1. [Why Jupyter Hub?]({static}/posts/jupyterhub/why_jupyter_hub.md) 
2. [Create SSH keys, save to documents/ssh-keys]({static}/posts/jupyterhub/PuTTYgen_ssh_key.md)
3. [Create a new Digital Ocean Droplet with a non-root sudo user]({static}/posts/jupyterhub/new_DO_droplet.md)
4. **Install Jupyter Hub on the server** (this post)
5. Apply SSL, link a domain name to the server and configure nginx
6. Connect OAuth to Jupyter Hub
7. Connect to Jupyter Hub as student

### The last JupyterHub deployment

In the last JupyterHub deployment went great.

### Changes for this JupyterHub deployment

There are a couple changes I want to make for the current JupyterHub deployment:

 * Use a virtual env instead the base conda environment
 * Becuase a virtual env is used, only need to install Miniconda not the whole Anaconda install
 * install Miniconda (and therefore Python) in the ```/opt``` directory
 * Set permissions of Miniconda installation
 * Create a conda env with the packages used in the course 

### Miniconda installed in /opt

For this JupyterHub deployment, I want to have Miniconda and Python installed in /opt instead of in a user directory.

The URL of the latest Miniconda install for Linux will look something like:

```text
https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

So the ```curl``` command and bash installer command are:

```text
$ cd /tmp
$ curl -O $ https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ sudo bash Miniconda3-latest-Linux-x86_64.sh
```

During the Miniconda install, we need to specify following installation directory:

```text
/opt/miniconda3/
```

Now we need to deal with some permission issues. Since I am running as the user ```peter``` on the Digital Ocean server, I need to make sure that the user ```peter``` has read, write, and execute permissions on the enitre ```/opt/miniconda3/``` directory. We can give our ```peter``` user permissions with ```chmod``` and ```chown```.

```text
$ cd /opt
$ ls
miniconda3
$ ls -la
total 12
drwxr-xr-x  3 root root 4096 Oct 30 04:47 .
drwxr-xr-x 23 root root 4096 Oct 29 17:49 ..
drwxr-xr-x 13 root root 4096 Oct 30 04:47 miniconda3
```

So right now the owner of the ```miniconda3``` directory is ```root``` and the group is ```root```. The owner ```root``` has read, write, execute privaleges (```rwx```) and the group ```root``` has read, execute privaleges (```r-x```), but now write prvialeges.

Let's modify the read, write, execute privaleges so that the group ```root``` can read, write, and execute (```rwx```).

```text
$ sudo chmod -R g+w miniconda3/
$ ls -la
total 12
drwxr-xr-x  3 root root 4096 Oct 30 04:47 .
drwxr-xr-x 23 root root 4096 Oct 29 17:49 ..
drwxrwxr-x 13 root root 4096 Oct 30 04:47 miniconda3
```

OK, now let's change the group corresponding to the miniconda3 directory from ```root``` to ```peter```.

```text
$ sudo chown -R root:peter miniconda3/
$ ls -la
total 12
drwxr-xr-x  3 root root  4096 Oct 30 04:47 .
drwxr-xr-x 23 root root  4096 Oct 29 17:49 ..
drwxrwxr-x 13 root peter 4096 Oct 30 04:47 miniconda3
```

Now the user ```peter``` should be able to install packages using pip and conda to the miniconda3 installation in the ```/opt``` directory.

## Conda env and packages

For this JupyterHub install, we are going to create a conda environment and install packages into the environment. I had trouble with conda hanging during the JupterHub install and I wondered if it had something to do with the Anaconda installation being so large. Or it might also have something to do with Python 3.7. When I tried to make a Python 3.7 conda env and install JupyterHub into it, conda downgraded Python from 3.7 to 3.6. So I think that the conda env should have Python 3.6. Also don't forget to install **xlrd**, this package is needed for pandas to read .xlsx files. 

```text
$ conda create -n jupyerhubenv python=3.6
$ conda activate jupyterhubenv
(jupyterhubenv)$ conda install numpy matplotlib pandas scipy sympy seaborn bokeh holoviews pyserial xlrd jupyter notebook 
(jupyterhubenv)$ conda install -c conda-forge pint altair
(jupyterhubenv)$ conda install -c conda-forge jupyterhub
```

See if it will work for just a second. Don't run anything import in the ```--no-ssl``` mode. 

```text
(jupyterhub)$ jupyterhub --no-ssl
 ```

Install nginix

```
$ sudo apt-get install nginx
```

Next install certbot and run it to obtain an SSL cirt

```
$ cd ~
$ mkdir cirtbot
$ 
```

After installing certbot we need to let nginx use the SSL cirts.

## Summary

In this post we installed **Anaconda** on the server using a shell script. We added **conda** to our path and reloaded our .bashrc file. Then we installed some extra **Python** packages such as **pint** and **pyserial**. Finally we installed **jupyterhub**, opened up port 8000 and ran **jupyterhub** for the first time! Remember we **shut down jupyter hub very quickly** because we ran it without any SSL security.

<br>

### Next Steps

In the next post we will build SSL security into our Jupyter Hub deployment and connect the server to domain name. Plus we'll customize the **jupyterhub** config file and install and use nginx as a proxy server.

