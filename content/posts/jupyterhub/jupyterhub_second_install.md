Title: Installing Jupyterhub
Date: 2018-10-29 12:40
Modified: 2018-10-29 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: installing-jupyter-hub-the-second-time
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Summary: This is the second time that I've set up JupyterHub to run for a college class. This time, I am making a couple of chnages to the deployment. This post is a record of those changes. To see how to set up JupyterHub for your ownn college class, see my previous series on JupyterHub starting with [Why Jupyter Hub?]({filename}/posts/jupyterhub/why_jupyter_hub.md) 

This is the second time that I've set up JupyterHub to run for a college class. This time, I am making a couple of chnages to the deployment. This post is a record of those changes. To see how to set up JupyterHub for your ownn college class, see my previous series on JupyterHub starting with [Why Jupyter Hub?]({filename}/posts/jupyterhub/why_jupyter_hub.md) 

### Posts in the JupyterHub installation series

1. [Why Jupyter Hub?]({filename}/posts/jupyterhub/why_jupyter_hub.md) 
2. [Create SSH keys, save to documents/ssh-keys]({filename}/posts/jupyterhub/PuTTYgen_ssh_key.md)
3. [Create a new Digital Ocean Droplet with a non-root sudo user]({filename}/posts/jupyterhub/new_DO_droplet.md)
4. **Install Jupyter Hub on the server** (this post)
5. Apply SSL, link a domain name to the server and configure nginx
6. Connect OAuth to Jupyter Hub
7. Connect to Jupyter Hub as student

### The last JupyterHub deployment

In the last jupyter hub deployment went great.

### Changes for this JupyterHub deployment

There are a couple changes I want to make for the current JupyterHub deployment:

 * install Anaconda (and therefore Python) in the ```/opt``` directory
 * 
 * 

### Anaconda installed in /opt

For this JupyterHub deployment, I want to have Anaconda and Python installed in /opt instead of in a user directory.

During the Anaconda install, we need to specify following installation directory:

```text
/opt/anaconda3/
```

Now we need to deal with some permission issues. Since I am running as the user ```peter``` on the Digital Ocean server, I need to make sure that the user ```peter``` has read, write, and execute permissions on the enitre ```/opt/anaconda3/``` directory. We can give our ```peter``` user permissions with ```chmod``` and ```chown```.

```text
$ cd /opt
$ ls
anaconda3
$ ls -la
total 12
drwxr-xr-x  3 root  root  4096 Oct 29 18:06 .
drwxr-xr-x 23 root  root  4096 Oct 29 17:49 ..
drwxr-xr-x 23 root  root  4096 Oct 29 18:44 anaconda3
```

So right now the owner of the ```anaconda3``` directory is ```root``` and the group is ```root```. The owner ```root``` has read, write, execute privaleges (```rwx```) and the group ```root``` has read, execute privaleges (```r-x```), but now write prvialeges.

Let's modify the read, write, execute privaleges so that the grou ```root``` can read, write, and execute (```rwx```).

```text
$ sudo chmod -R g+w anaconda3/
$ ls -la
drwxr-xr-x  3 root  root  4096 Oct 29 18:06 .
drwxr-xr-x 23 root  root  4096 Oct 29 17:49 ..
drwxrwxr-x 23 root  root  4096 Oct 29 18:44 anaconda3
```

OK, now let's change the group corresponding to the anaconda3 directory from ```root``` to ```peter```.

```text
$ sudo chown -R root:peter anaconda3/
$ ls -la
drwxr-xr-x  3 root root  4096 Oct 29 18:06 .
drwxr-xr-x 23 root root  4096 Oct 29 17:49 ..
drwxrwxr-x 23 root peter 4096 Oct 29 19:38 anaconda3
```

Now the user ```peter``` should be able to install packages using pip and conda to the Anaconda3 installation in the /opt directory.


 
### Summary

In this post we installed **Anaconda** on the server using a shell script. We added **conda** to our path and reloaded our .bashrc file. Then we installed some extra **Python** packages such as **pint** and **pyserial**. Finally we installed **jupyterhub**, opened up port 8000 and ran **jupyterhub** for the first time! Remember we **shut down jupyter hub very quickly** because we ran it without any SSL security.

<br>

### Next Steps

In the next post we will build SSL security into our Jupyter Hub deployment and connect the server to domain name. Plus we'll customize the **jupyterhub** config file and install and use nginx as a proxy server.

