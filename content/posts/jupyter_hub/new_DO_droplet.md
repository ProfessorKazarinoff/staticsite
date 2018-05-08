Title: Creating a new Digital Ocean Droplet?
Date: 2018-05-07 12:40
Modified: 2018-05-07 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: why-jupyter-hub
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 2
Summary: This is the second part of a multi-part series that show how to set up Jupyter Hub for a class. This will be the first time setting up a Jupyter Hub server for me, I am primarily writing to my future self as I may need to do this again in the future. In this post, I am going to try and create a new Digital Ocean droplet and create a non-root sudo user and SSH in with my machine at work.

This is the second part of a multi-part series that show how to set up Jupyter Hub for a class. This will be the first time setting up a Jupyter Hub server for me, I am primarily writing to my future self as I may need to do this again in the future. In this post, I am going to try and create a new Digital Ocean droplet and create a non-root sudo user and SSH in with my machine at work.

### List of all steps

1. Sign up for a Digital Ocean Account (already done)
2. Create a new Digital Ocean Droplet (will be called _the server_ from here on out)
3. Connect to the server over SSH and set up SSH keys
4. Create a non-root sudo user
5. Get a public url, hook up the server DNS record to the public URL
6. Install Anaconda on the server
7. Install the other packages on the server like jupyter hub, npm, pyserial, pint
8. Symlinks and permissions of files on the server
9. Create and implement SSL certificates on server
10. Run Jupyter Hub as non-root sudo user
11. Connect OAuth to Jupyter Hub
12. Connect to Server as student

### This post

1. Sign up for a Digital Ocean Account (already done)
2. Create a new Digital Ocean Droplet (will be called _the server_ from here on out)
3. Connect to the server over SSH using PuTTY
4. Create a non-root sudo user

#### 1. Sign up for a Digital Ocean Account (already done)

I already have a Digital Ocean account. I don't remember exactly how I did it, but going to this link:

[https://www.digitalocean.com/](https://www.digitalocean.com/)

and selecting [Create Account -->] should work.

#### 2. Create a new Digital Ocean Droplet

To create a new droplet, I need to log into Digital Ocean here:

[https://cloud.digitalocean.com/login](https://cloud.digitalocean.com/login)

![Digital Ocean Login](/posts/jupyter_hub/digital_ocean_login.png)

After I logged in, I got a verify screen and had to go to my email and get a six digit code:

![Digital Ocean Verify](/posts/jupyter_hub/digital_ocean_verify.png)

The welcome screen after loggin in, looks like this. Select [Create Droplet]

![Digital Ocean Create Droplet](/posts/jupyter_hub/digital_ocean_create_droplet.png)

There are a number of choices to make:

 * Image: Ubuntu 16.04.4 x64
 * Size: 1 GB Memory 25GB SSD $5/month
 * Datacenter: San Fransisco 2
 * Add your SSH keys: New SSH Key
 * Finalize: 1 Droplet, Hostname: jupyter-hub

![Digital Droplet Choices](/posts/jupyter_hub/digital_ocean_create_droplets_choices.png)

![Digital Droplet Choices](/posts/jupyter_hub/digital_ocean_droplet_size_choices.png)

![Digital Droplet Choices](/posts/jupyter_hub/digital_ocean_droplet_data_center_choices.png)

![Digital Droplet Choices](/posts/jupyter_hub/digital_ocean_droplet_ssh_key__choices.png)

![Digital Droplet Choices](/posts/jupyter_hub/digital_ocean_droplet_finalize_and__create.png)

#### Add an SSH Key

Under Add your SSH keys, when I click [New SSH Key] a dialog window pops up.

![Digital Droplet Choices](/posts/jupyter_hub/digital_ocean_droplet_new_ssh_key_dialog.png)

I went through this tutorial to set up an SSH key on Windows:

[How To Use SSH Keys with PuTTY on DigitalOcean Droplets (Windows users)](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-putty-on-digitalocean-droplets-windows-users)

Using the Windows start menu, open PuTTYgen (not regular PuTTY):

![Putty in Windows Start Menu](/posts/jupyter_hub/puttygen_in_start_menu.png)

![Putty in Windows Start Menu](/posts/jupyter_hub/puttygen_key_generator.png)

Use the following parameters

 * Type of key to generate: RSA
 * Number of bits in generated key: 2048

Then click [generate]

![Putty in Windows Start Menu](/posts/jupyter_hub/puttygen_generate.png)

This will bring up a dialog to move the mouse around the empty area to generate some randomness. This is my favorite part. Just move the mouse around the dialog box until the progress bar ends. Fun.

When the next screen pops up. Right-click and copy the contents of the Public Key for pasting into Open SSH authorized_keys files. Include the rsa line in the copy to clipboard.

In the Actions section click [Save Public Key] and click [Save Public Key]

![Putty in Windows Start Menu](/posts/jupyter_hub/puttygen_save_public_private_key.png)

I saved the public key with the name: public_key_jupyter_hub.txt. The digital ocean documentation recommends a .txt file extension.

![Putty in Windows Start Menu](/posts/jupyter_hub/puttygen_public_key_save_name.png)

Now go back to the Digital Ocean Droplet create webpage and paste the contents of the SSH Key into the Add SSH Keys dialog box

![Putty in Windows Start Menu](/posts/jupyter_hub/digital_ocean_droplet_enter_ssh_key__details.png)

Enter a name for the SSH key that will be saved on Digital Ocean. I choose the name jupyter-hub-ssh-key. Then click [Add SSH Key]

![Putty in Windows Start Menu](/posts/jupyter_hub/digital_ocean_droplet_ssh_key_name_and_add.png)

You should then see the new SSH Key in the Add your SSH Keys? region of the create a new droplets page

![Putty in Windows Start Menu](/posts/jupyter_hub/digital_ocean_see_new_ssh_key.png)

I think it's time to actually create the droplet. Click the long green [Create] button at the bottom of the page.

![Putty in Windows Start Menu](/posts/jupyter_hub/digital_ocean_droplet_create.png)

This will bring you back the the Digital Ocean main dashboard and you should see your new droplet under Resources --> Droplets

![Putty in Windows Start Menu](/posts/jupyter_hub/digital_ocean_droplets_1.png)



As a goal, I would like to see the first programming lab of the quarter to
1. There is a pdf or google doc posted on a shared google drive folder with a link to Jupyter Hub
2. Students click the link and bring up the login page
3. Students log-in with their college usernames and passwords (or maybe Github usernames and passwords)
4. Students type ```import this``` [Shift-Enter] and their first code cell runs.


### This is theoretically possible with Jupyter Hub

Jupyter Hub can be installed on a Digital Ocean droplet. The version of Python running the notebooks can be the full Anaconda distribution plus some extras like **Pint** and **pyserial**. One Digital Ocean droplet will be able to run all of the notebooks at the same time. Student's work will be saved on the server under their user account. Students can download the .ipynb files and upload them to google drive. There can be folders and notebooks already in place that can be used as starting points in lab and as lab exersizes.

### What will it take to make Jupyter Hub a reality

This list will surely change as I go through the process of setting the server up. Below are the steps I expect to take and software/hardware needed at each step.

1. Sign up for a Digital Ocean Account (already done)
2. Create a new Digital Ocean Droplet (will be called _the server_ from here on out)
3. Connect to the server over SSH and set up SSH keys
4. Create a non-root sudo user
5. Get a public url, hook up the server DNS record to the public URL
6. Install Anaconda on the server
7. Install the other packages on the server like jupyter hub, npm, pyserial, pint
8. Symlinks and permissions of files on the server
9. Create and implement SSL certificates on server
10. Run Jupyter Hub as non-root sudo user
11. Connect OAuth to Jupyter Hub
12. Connect to Server as student

### Will this work? How much time will it take?

Will this work? I hope so. Other people have done it. There was a jupytercon talk about it. They did it at UCBerlkey. I don't really know how long it will take. The only real step that takes time is the DNS connection. The rest of the steps are in the minute time frame. I'm just going to try and do a step a day or a step a week and see if I can get the server going by the end of the quarter.

### Next Steps:

The next steps are really the first steps:

1. Sign up for a digital Ocean account

2. Create a new Digital Ocean Droplet

3. Create a non-root sudo user