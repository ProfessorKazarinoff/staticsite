Title: Installing Jupyterhub
Date: 2018-05-12 12:40
Modified: 2018-05-012 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: installing-jupyter-hub
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 4
Summary: This is the third part of a multi-part series that show how to set up Jupyter Hub for a college class. My goal is to having a running version of Jupyter Hub that students in the class can log into just using a simple web link. In this post, I am going to get to the fun stuff: installing Jupyter Hub on the server, installing Python packages and spinning up Jupyter Hub for the first time.

This is the third part of a multi-part series that show how to set up Jupyter Hub for a college class. My goal is to having a running version of Jupyter Hub that students in the class can log into just using a simple web link. In this post, I am going to get to the fun stuff: installing Jupyter Hub on the server, installing Python packages and spinning up Jupyter Hub for the first time.


### List of all steps

1. Create ssh key, save to documents/ssh-keys (complete)
2. Create a new Digital Ocean Droplet with a non-root sudo user (complete)
3. Install Jupyter Hub on Server (this post)
4. Secure a domain name and apply SSL
5. Install the other packages on the server like jupyter hub, npm, pyserial, pint
6. Symlinks and permissions of files on the server
7. Create and implement SSL certificates on server
8. Run Jupyter Hub as non-root sudo user
9. Connect OAuth to Jupyter Hub
10. Connect to Server as student

### The last post

In previous post, we created a new Digital Ocean cloud server. Then we logged in as ```root``` into the server with PuTTY and our private SSH key. As ```root``` we set up a new user with sudo privaleges. Then we logged into the server as the new user and checked the new user's home directory. 


### This post

1. Update packages
2. Install anaconda
3. Install Python Packages and JupyterHub 
4. Run very unsecure instance of Jupyter Hub just to see if it works
5. Shut down Jupyter Hub very quickly because of no SSL



#### 1. Update Packages

It is probably best to update the server in case there are changes to the operating system since the server was created. This is probably a reflex for those that use Linux a lot. Open PuTTY and log into the server as the non-root sudo user we created in the last post. Then update the system:

```
$ sudo apt-get update
$ sudo apt-get dist-upgrade
```


#### 2. Install Anaconda

Next we'll install **Anaconda**. When I install Anaconda on windows I use an msi installer, but for installation on the server, we'll use a shell script. The first time I set up Jupyter Hub, I installed anaconda in the non-root sudo user's home directory. I don't think this is the best setup. It is probably better to install it in a location that all users can access. The ```/opt``` directory is a location in the linux file system where 3rd party programs are often installed. So let's ```cd``` into there and find the proper shell script to run. 

I'm following [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04) from Digital Ocean.

Go to [https://repo.continuum.io/archive/](https://repo.continuum.io/archive/) and look down the list of installs for the newest installer that corresponds to:

 * Anaconda 3
 * Linux
 * x86
 * 64 (bit)
 * .sh (linux shell script)

Right now, that is:

```
Anaconda3-5.1.0-Linux-x86_64.sh
```
 
### Summary

In this post we created a new Digital Ocean server (called a Droplet) and made sure to add our public SSH key to the setup options before we hit [Create]. Then we logged in as ```root``` into the server with PuTTY and our private SSH key. As ```root``` we set up a new user with sudo privaleges. Then we logged into the server as the new user and checked the new user's home directory.

### Next Steps

In the next post we will get to the fun stuff: installing Anaconda and Jupyter Hub on our new server and starting Jupyter Hub for the first time! (but only keep it open for a couple seconds because we don't have SSL set up yet).

