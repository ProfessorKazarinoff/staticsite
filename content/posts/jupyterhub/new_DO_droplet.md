Title: Creating a new Digital Ocean Droplet
Date: 2018-05-18 12:40
Modified: 2018-05-18 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: new-digital-ocean-droplet
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 3
Summary: This is the third part of a multi-part series that show how to set up Jupyter Hub for a college class. My goal is to have a running version of Jupyter Hub that students in the class can log into just using a simple web link. I am primarily writing to my future self as I may need to set up Jupyter Hub again for future classes. In this post, we are going to create a new Digital Ocean droplet and create a non-root user with sudo privaledges. Then we'll SSH into the droplet with PuTTY as the new non-root user.

This is the third part of a multi-part series that show how to set up Jupyter Hub for a college class. My goal is to have a running version of Jupyter Hub that students in the class can log into just using a simple web link. I am primarily writing to my future self as I may need to set up Jupyter Hub again for future classes. In this post, we are going to create a new Digital Ocean droplet and create a non-root user with sudo privaledges. Then we'll SSH into the droplet with PuTTY as the new non-root user.


### List of all steps

1. Create ssh key, save to documents/ssh-keys (complete)
2. Create a new Digital Ocean Droplet with a non-root sudo user (this post)
3. Get a public URL, hook up the server DNS record to the public URL
4. Install Anaconda on the server
5. Install the other packages on the server like jupyter hub, npm, pyserial, pint
6. Symlinks and permissions of files on the server
7. Create and implement SSL certificates on server
8. Run Jupyter Hub as non-root sudo user
9. Connect OAuth to Jupyter Hub
10. Connect to Server as student

### The last post

In the previous post, we created public and private SSH keys and saved them locally in Documents/ssh-keys. We also copied the public SSH key (including the ```rsa``` portion) to the clipboard. We'll need the public SSH key when we set up the Digital Ocean Droplet. We'll need the private SSH key to connect to the Dropet with PuTTY.

### This post

1. Sign up for a Digital Ocean Account
2. Create a new Digital Ocean Droplet (will be called _the server_ from here on out)
3. Connect to the server as root over SSH using PuTTY 
4. Create a non-root sudo user
5. Connect to the server as the non-root sudo user using PuTTY



### 1. Sign up for a Digital Ocean Account

Digital Ocean is a cloud service provider like Amazon Web Services (AWS), Google Cloud, Microsoft Azure and Linode. Digital Ocean provides virtual private servers (called Droplets in Digital Ocean-speak) and online storage of static files (called Spaces in Digital Ocean-speak). We are going to run the Jupyter Hub server on a Digital Ocean Droplet. I like Digital Ocean's prices and web interface. The documentation on Digital Ocean is pretty good too. I already have a Digital Ocean account. I don't remember exactly how I did it, but going to this link:

[https://www.digitalocean.com/](https://www.digitalocean.com/)

and selecting [Create Account -->] should work.

### 2. Create a new Digital Ocean Droplet

To create a new Digtial Ocean Droplet (a new server), you to log in here:

[https://cloud.digitalocean.com/login](https://cloud.digitalocean.com/login)

![Digital Ocean Login](/posts/jupyterhub/digital_ocean_login.png)

After logging in, I got a verify screen and had to go to my email and retrive a six digit code. Ah... the joys of two-factor authentication.

![Digital Ocean Verify](/posts/jupyterhub/digital_ocean_verify.png)

The welcome screen looks like this. To create a new server, select [Create Droplet]

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

![Digital Droplet Choices](/posts/jupyterhub/digital_ocean_droplet_finalize_and__create.png)

#### Add an SSH Key

If the SSH public key shown on the list of keys and the radio box beside it checked, that means the SSH key will not be added to the server when the server is first created. We need to add our SSH key so that we can log onto the server with PuTTY.

Under Add your SSH keys, click [New SSH Key]. A dialog window pops up:

![Digital Droplet Choices](/posts/jupyterhub/digital_ocean_droplet_new_ssh_key_dialog.png)

Paste the contents of the SSH public key into the Add SSH Keys dialog box.

![Putty in Windows Start Menu](/posts/jupyterhub/digital_ocean_droplet_enter_ssh_key__details.png)

Enter a name for the SSH key that will be saved on Digital Ocean. I choose the name jupyter-hub-ssh-key. Then click [Add SSH Key]

![Putty in Windows Start Menu](/posts/jupyterhub/digital_ocean_droplet_ssh_key_name_and_add.png)

You should then see the new SSH Key in the [Add your SSH Keys?] region of the new droplets page. Make sure that the radio box for the SSH key we just added is checked. A problem I had when I set up my first droplet was that I did not ensure the new SSH Key was selected to go onto the new server. When the server was created, no SSH keys were installed. I ended up going through this long process of copying the public SSH key into pastbin.com (which is definetly **not a safe thing to do**), and using ```wget``` to past the raw contents from the pastebin into the server file system, then using ```cp``` to copy the publish SSH key into the correct file name. This required using the Ditigal Ocean console, which is sort of like a bash terminal that pops up in a web browser. I couldn't figure out a way to copy and paste into the Digital Ocean console and the console is slow and laggy. It is _way easier_ to insert the SSH key into the server when the server is created. It is _way harder_ to add an SSH key after the server is created.

![Putty in Windows Start Menu](/posts/jupyterhub/digital_ocean_see_new_ssh_key.png)

I think it's time to actually create the droplet. Click the long green [Create] button at the bottom of the page.

![Putty in Windows Start Menu](/posts/jupyterhub/digital_ocean_droplet_create.png)

This will bring you back the the Digital Ocean main dashboard and you should see your new droplet under Resources --> Droplets

![Putty in Windows Start Menu](/posts/jupyterhub/digital_ocean_droplets_1.png)

Copy the IP address of the new droplet onto the clipboard. We need to IP address to log into the server with PuTTY.

### 3. Log into the server as root over SSH using PuTTY.

Open PuTTY from the Windows start menu. Then paste the IP address into the PuTTY main window. Set the Port = 22. A couple other parameters need to be set before we logon.

Under Connect --> SSH --> Auth --> Private key file for authentication, click [Browse]. 

Navigate to the SSH private key in Documents/ssh-keys. The private key ends in a .ppk extension. I had trouble finding the key when I first set up PuTTY. It turned out that when the key was saved in Programfiles/PuTTY. The key was not visible in the Windows file browser because I don't have administrator permissions on my machine at work. I ended up having to create a new SSH key and save the new key in Documents/ssh-key (I can access Documents/ssh-key without administrator privaleges).

Under Connection --> Data --> Auto-login username: ```root```

Back in [Sessions] (the top-most menue item or main page), click [Open]

### 4. Create a non-root sudo user

Digital Ocean recommends that the servers are run by non-root user that have sudo access. So one of the first things we'll do on our server is create a non-root sudo user. First though let's make sure everything is up to date:

```
$ sudo apt-get update
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
usermod -aG sudo <username>
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

Before we log off, we need to add our ssh keys to our new user's profile on the server. The second time I set up JupyterHub, I had trouble logging in as the non-root user using PuTTY. I could log in as ```root``` just fine, but I couldn't log in as the newly created user ```peter```. When Digital Ocean created the server, the ssh keys (specified on the creation page) were added to the ```root``` profile. The new user ```peter``` didn't exist when the server was created. The only user was ```root``` at creation time. Therefore no ssh keys were added to the ```peter``` profile at server creation time, because the user ```peter``` didn't exist yet. Since we want to log into our server as the new non-root user ```peter```, we need to add the same ssh keys saved in the ```root``` profile to the ```peter``` profile. The ssh keys belong in a file located at ```/home/peter/.ssh/authorized_keys```. I followed [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-create-ssh-keys-with-putty-to-connect-to-a-vps) from Digital Ocean.


```
$ mkdir ~/.ssh
$ chmod 0700 ~/.ssh
$ touch ~/.ssh/authorized_keys
$ chmod 0644 ~/.ssh/authorized_keys
$ nano /home/peter/.ssh/authorized_keys
```

Use the right mouse button to paste in the ssh-key from the clipboard. If the ssh key is not saved in the clipboard, then you can retrive it with PuTTYgen --> load or go to Digital Ocean, click in the upper right on the profile picture --> setttings --> security --> ssh-key --> edit dropdown --> edit. You can paste into the PuTTY window using the right mouse button. Use [Ctrl-x] and [Y] to save and exit. I tried to use ```cp``` to copy the ```authorized_keys``` file from ```/root/.ssh/``` to ```/home/peter/.ssh``` but there was a problem with permissions and write access to the ```authorized_keys``` file. I couldn't get PuTTY to login as ```peter``` until I removed the file, recreated an empty one and pasted in the SSH key. This is probably also possible with ```cat file1 >> file2```. Manually copying and pasting with the right mouse button was the way I got it to work. 

Now we can exit out of the ```peter``` profile

```
$ exit
```

This should bring you back to the ```root``` user. Restart the server to enact the changes with:

```
$ sudo shutdown -r now
```

You might need to wait a minute or two for the server to restart.

### 4. Connect to the server as the non-root sudo user using PuTTY

Now that the non-root sudo user is set up and our ssh keys are in /home/<user>/.ssh/authorized_keys, let's start a new PuTTY session and log into the server as the new user. Like before, open PuTTY from the Windows Start menu and add the following settings:

Hostname (or IP Address)           Digital Ocean Server IP Address (example 162.01.254.01)

Port                               22

Connection --> Data                Auto-login username: <username> (the new user you just set up)

Connection --> SSH --> Auth        Private Key file for identification, browse to Documents/SSH-keys and select private_key.ppk

Sessions --> [Open]
  
You should see the Digital Ocean login screen. Check to see which directory you land it. It should be ```/home/<username>```

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

In this post we created a new Digital Ocean server (called a _droplet_) and made sure to add our public SSH key to the setup options before we hit [Create]. Then we logged into the server as ```root```  with our private SSH key. As ```root```, we set up a new user with sudo privaleges and added our public SSH key to the new user's profile. Then we logged into the server as the new user and checked the new user's home directory and ensured the non-root user has sudo privileges.


### Next Steps

In the next post we will get to the fun stuff: installing Anaconda and Jupyter Hub on our new server and starting Jupyter Hub for the first time! (but only keep it open for a couple seconds because we don't have SSL set up yet).

