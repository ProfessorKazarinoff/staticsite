Title: Creating a new Digital Ocean Droplet
Date: 2018-05-20 12:40
Modified: 2018-05-20 12:40
Status: published
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: new-digital-ocean-droplet
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 3
Summary: This is the third part of a multi-part series on how to set up Jupyter Hub for a class.  My goal is to have a running version of Jupyter Hub that students can access using a simple web link. I am primarily writing to my future self as I may need to set up Jupyter Hub again for a future class. In this post, we are going to create a new Digital Ocean server (called a _droplet_) and create a non-root user with sudo privileges. Then we'll SSH into the droplet with PuTTY as the non-root user.

This is the third part of a multi-part series on how to set up Jupyter Hub for a class.  My goal is to have a running version of Jupyter Hub that students can access using a simple web link. I am primarily writing to my future self as I may need to set up Jupyter Hub again for a future class. In this post, we are going to create a new Digital Ocean server (called a _droplet_) and create a non-root user with sudo privileges. Then we'll SSH into the droplet with PuTTY as the non-root user.


### Posts in this series

1. [Why Jupyter Hub?]({filename}/posts/jupyterhub/why_jupyter_hub.md) 
2. [Create ssh key, save to documents/ssh-keys]({filename}/posts/jupyterhub/PuTTYgen_ssh_key.md)
3. **Create a new Digital Ocean Droplet with a non-root sudo user** (this post)
4. Install Jupyter Hub on the server
5. Apply SSL, link a domain name to the server and configure nginx
6. Connect OAuth to Jupyter Hub
7. Connect to Jupyter Hub as student

### The last post

In the [previous post]({filename}/posts/jupyterhub/PuTTYgen_ssh_key.md), we created a public/private SSH key pair using PuTTYgen. We saved the SSH keys in the Documents/ssh-keys directory. We also copied contents of the public SSH key to the clipboard.

### Steps in this post

1. Sign up for a Digital Ocean Account
2. Create a new Digital Ocean Droplet (will be called _the server_ from here on out)
3. Log into the server as root over SSH using PuTTY. 
4. Create a non-root sudo user
5. Log into to the server as the non-root sudo user using PuTTY



### 1. Sign up for a Digital Ocean Account

Digital Ocean is a cloud service provider like Amazon Web Services (AWS), Google Cloud, Microsoft Azure and Linode. Digital Ocean provides virtual private servers (called _droplets_ in Digital Ocean-speak) and online storage of static files (called _spaces_ in Digital Ocean-speak). We are going to run the Jupyter Hub server on a Digital Ocean _droplet_. I like Digital Ocean's prices and web interface. The documentation on Digital Ocean is pretty good too. I already have a Digital Ocean account. I don't remember exactly how I did it, but going to this link:

[https://www.digitalocean.com/](https://www.digitalocean.com/)

and selecting [Create Account -->] should work.

### 2. Create a new Digital Ocean Droplet

To create a new Digtial Ocean Droplet (a new server), log in here:

[https://cloud.digitalocean.com/login](https://cloud.digitalocean.com/login)

![Digital Ocean Login](/posts/jupyterhub/digital_ocean_login.png)

After logging in, I got a verify screen and had to go to my email and retrive a six digit code. Ah... the joys of two-factor authentication.

![Digital Ocean Verify](/posts/jupyterhub/digital_ocean_verify.png)

The welcome screen looks like this. To create a new server select [Create Droplet]

![Digital Ocean Create Droplet](/posts/jupyterhub/digital_ocean_create_droplet.png)

There are a number of choices to make. These are the ones I selected:

 * Image: Ubuntu 16.04.4 x64
 * Size: 1 GB Memory 25GB SSD $5/month
 * Datacenter: San Fransisco 2
 * Add your SSH keys: New SSH Key
 * Finalize: 1 Droplet, Hostname: jupyter-hub

![Digital Droplet Choices](/posts/jupyterhub/digital_ocean_create_droplets_choices.png)

![Digital Droplet Choices](/posts/jupyterhub/digital_ocean_droplet_size_choices.png)

![Digital Droplet Choices](/posts/jupyterhub/digital_ocean_droplet_data_center_choices.png)

![Digital Droplet Choices](/posts/jupyterhub/digital_ocean_droplet_ssh_key__choices.png)

#### Add an SSH Key

<div class="alert alert-warning" role="alert">
  <strong>Important!</strong> You need to add the public SSH key BEFORE creating the droplet
</div>

The public SSH key we created needs to be shown on the list of keys and the radio box beside it needs to be checked. If the SSH key isn't listed or the SSH key box left  unchecked, the SSH key will not be added to the server when the server is first created (and then we won't be able to log in with PuTTY). We need to add our public SSH key and check the key box so we can log onto the server with PuTTY.

Under [Add your SSH keys], click [New SSH Key]. A dialog window pops up:

![Digital Droplet Choices](/posts/jupyterhub/digital_ocean_droplet_new_ssh_key_dialog.png)

Paste the contents of the public SSH key into the [New SSH Key] dialog box.

![Putty in Windows Start Menu](/posts/jupyterhub/digital_ocean_droplet_enter_ssh_key__details.png)

Enter a name for the SSH key that will be saved on Digital Ocean. I choose the name ```jupyter-hub-ssh-key```. Then click [Add SSH Key]

![Putty in Windows Start Menu](/posts/jupyterhub/digital_ocean_droplet_ssh_key_name_and_add.png)

Then you should see the new SSH Key in the [Add your SSH Keys?] region of the new droplets page. Make sure that the radio box for the SSH key we just added is checked. 

A problem I had when I set up my first _droplet_ was that I did not have the SSH Key was radio button selected. Therefore, when the server was created, no SSH keys were installed. I ended up going through this long process of copying the public SSH key into pastbin.com (which is definitely **not a safe thing to do**), and using ```wget``` to past the raw contents from the pastebin into the server file system, then using ```cp``` to copy the publish SSH key into the correct file name. This required using the Digital Ocean console, which is sort of like a bash terminal that pops up in a web browser. I couldn't figure out a way to copy and paste into the Digital Ocean console and the console is slow and laggy. 

It is _way easier_ to insert SSH keys into the server when the server is created. It is _way harder_ to add an SSH key after the server is created.

![Putty in Windows Start Menu](/posts/jupyterhub/digital_ocean_see_new_ssh_key.png)

OK, I think it's time to actually create the _droplet_. Click the long green [Create] button at the bottom of the page.

![Putty in Windows Start Menu](/posts/jupyterhub/digital_ocean_droplet_create.png)

This will bring you back the the Digital Ocean main dashboard and you should see your new droplet under [Resources] --> [Droplets]

![Putty in Windows Start Menu](/posts/jupyterhub/digital_ocean_droplets_1.png)

Note the IP address of the new droplet. We need to IP address to log into our server with PuTTY.

### 3. Log into the server as root over SSH using PuTTY.

Open PuTTY from the Windows start menu. A couple other parameters need to be set before we log onto the server.

| parameter | value |
| --- | --- |
| IP Address | IP of _droplet_ ex: 168.97.14.19 |
| Port | 22 |
| Connection --> SSH --> Auth --> Private key file | private SSH key |
| Connection --> Data --> Auto-login username | root |

![Putty in Windows Start Menu](/posts/jupyterhub/putty_in_start_menu.png)

Under Connect --> SSH --> Auth --> Private key file for authentication:, click [Browse]. 

![PuTTY Auth SSH private key](/posts/jupyterhub/putty_Auth_SSH_private_key.png)

Navigate to the SSH private key in Documents/ssh-keys. The private key ends in a .ppk extension. I had trouble finding the key when I first set up PuTTY. It turned out that when the key was saved in Programfiles/PuTTY. The key was not visible in the Windows file browser because I don't have administrator permissions on my machine at work. I ended up having to create a new SSH key and save the new key in Documents/ssh-key (I can access Documents/ssh-key without administrator privaleges).

![PuTTY browse to private SSH key](/posts/jupyterhub/putty_browse_private_ssh_key.png)

Under Connection --> Data --> Auto-login username: ```root```

![Putty login details](/posts/jupyterhub/putty_login_details.png)

Back in [Sessions] (the top-most menu item or main page), add the IP address and Port = 22, click [Open]

![Putty IP address and Port](/posts/jupyterhub/puTTY_IP_and_Port.png)

This should bring up a new window that is a terminal for our server:

![PyTTY SSH window open](/posts/jupyterhub/putty_ssh_window_open.png)

### 4. Create a non-root sudo user

Digital Ocean recommends that the servers are run by non-root user that have sudo access. So one of the first things we'll do on our server is create a non-root sudo user. First though, let's make sure everything is up to date:

```
$ sudo apt-get update
$ sudo apt-get upgrade
```

I followed [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart) at Digital Ocean to create a non-root sudo user.

Create the new user with the ```adduser``` command. I called my new user ```peter```.
  
```
$ adduser <username>
```

Set a new password and confirm:

```
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```

The user details can be skipped by pressing [Enter]. Then [Y] to complete the new user setup.

```
Changing the user information for username
Enter the new value, or press ENTER for the default
    Full Name []:
    Room Number []:
    Work Phone []:
    Home Phone []:
    Other []:
Is the information correct? [Y/n]
```

Now let's give our new user sudo privaleges:

```
$ usermod -aG sudo <username>
```

The new user account is created and the new user has sudo privalges. We can switch accounts and become the new user with:

```
$ sudo su - <username>
```

The new user should have ```sudo``` privileges. That means when acting as ```<username>``` we should be able to look in the ```/root``` directory.

```
$ sudo ls -la /root
```

If you can see the contents of ```/root``` then the new user is set up with sudo access.

To exit out of the the new sudo user, and get back to using the root profile, type ```exit``` at the prompt

```
$ exit
```

#### Add SSH keys to new user's profile

Before we log off, we need to add our SSH keys to our new user's profile on the server. The second time I set up JupyterHub, I had trouble logging in as the non-root user using PuTTY. I could log in as ```root``` just fine, but I couldn't log in as the newly created user ```peter```.

 When Digital Ocean created the server, the SSH keys (specified on the creation page) were added to the ```root``` profile. The new user ```peter``` didn't exist when the server was created. The only user on the server at creation time was ```root```. Therefore, no SSH keys were added to the ```peter``` profile at server creation time- because the user ```peter``` didn't exist yet. 
 
 Since we want to log into our server as the new non-root user ```peter```, we need to add the same SSH keys saved in the ```root``` profile to the ```peter``` profile. The SSH keys belong in a file located at ```/home/peter/.ssh/authorized_keys```. 

This little line will copy the ssh keys from the root profile to the new user's profile. The line comes from [this tutorial](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04) by Digital Ocean.

```
$ rsync --archive --chown=peter:peter ~/.ssh /home/peter
```

Next, we need to open the ufw firewall to OpenSSH trafic. We will communicate with the server over SSH and need the firewall to allow this type of communication through.

```
$ ufw allow OpenSSH
$ ufw enable
$ ufw status
```

Now we can exit out of the ```root``` profile. This will terminate the PuTTY session.

```
$ exit
```

### 4. Connect to the server as the non-root sudo user using PuTTY

Now that the non-root sudo user is set up and our ssh keys are in /home/<user>/.ssh/authorized_keys, let's start a new PuTTY session and log into the server as the new user. 

Like before, open PuTTY from the Windows Start menu and add the following settings, but this time the Auto-login user name is the name of our new non-root sudo user:

| parameter | value |
| --- | --- |
| IP Address | IP of _droplet_ ex: 168.97.14.19 |
| Port | 22 |
| Connection --> SSH --> Auth --> Private key file | private SSH key |
| Connection --> Data --> Auto-login username | peter |

I also saved the PuTTY session details at this point so that I wouldn't have to re-enter all of the parameters each time I want to log into the server. Enter a name into [Saved Sessions] and click [Save]. Once the parameters are saved in PuTTY, you can simply double-click the profile name and you will log into the server.

![PuTTY save profile](/posts/jupyterhub/putty_save_session.PNG)

Log into the server with Sessions --> [Open]
  
You should see the Digital Ocean login screen again. Note the command prompt will have the new user's name before the ```@``` symbol. 

![server terminal as peter](/posts/jupyterhub/putty_ssh_window_open_as_peter.png)

Check to see which directory you land in. It should be ```/home/<username>```

```
$ pwd
/home/<username>
```

We can see the non-root user's home directory. Let's make sure we can also see into the ```root``` user's home directory to ensure we have sudo privileges as the non-root user:


```
$ sudo ls -la /root
```

To log out of the server simply type ```exit```. This should close the PuTTY session.

```
$ exit
```


### Summary

In this post we created a new Digital Ocean server (called a _droplet_) and made sure to add our public SSH key to the setup options before we hit [Create]. Then we logged into the server as ```root```  with our private SSH key. As ```root```, we set up a new user with sudo privileges and added our public SSH key to the new user's profile in ```~/.ssh/authorized_keys```. Then we logged into the server as the new user and checked the new user's home directory and ensured the new user has sudo privileges.


### Next Steps

In the next post, we will get to the fun stuff: installing **Anaconda** and **jupyterhub** on our new server. Plus we'll start Jupyter Hub for the first time! (but only keep it open for a couple seconds because we don't have SSL set up yet).
