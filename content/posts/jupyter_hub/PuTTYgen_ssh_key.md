Title: Create an SSH Key with PuTTYgen
Date: 2018-05-07 12:40
Modified: 2018-05-07 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: why-jupyter-hub
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 2
Summary: This is the second part of a multi-part series that show how to set up Jupyter Hub for a class. This will be the first time setting up a Jupyter Hub server for me, I am primarily writing to my future self as I may need to do this again in the future. In this post, I am going to create an SSH key on a Windows 10 machine using PuTTYgen.

This is the second part of a multi-part series that shows how to set up Jupyter Hub for a class. This will be the first time setting up a Jupyter Hub server for me, I am primarily writing to my future self as I may need to do this again in the future. In this post, I am going to create an SSH key on a Windows 10 machine using PuTTYgen.

### List of all steps

1. Create an SSH Key with PuTTYgen
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

### In this post

1. Download PuTTY for Windows
2. Start PuTTYgen and create SSH key
3. Save SSH public and private keys to Documents folder
4. Copy the public key to clipboard

### Why SSH keys, PuTTYgen and why do this first?

When I set up the server the first time, one of the initial server setup steps is to add SSH keys so the server has them when it initialized. 

![Digital Droplet Choices](/posts/jupyter_hub/digital_ocean_droplet_new_ssh_key_dialog.png)

I tried to create and save the keys to the Digital Ocean dashboard so they would be on the server when it first started, but I goofed up somehow and the server started without any SSH keys. It was a BIG pain adding SSH keys after the server started for the first time. I ended up copying the public key into pastebin.com, logging onto the server with the Digital Ocean console and using ```wget``` to bring a textfile of the key onto the server and then ```mv``` to copy the key name into the right location.

I'm pretty sure that pasting a public SSH key into pastebin.com is not the best way to initially set up a server. So to make sure that doesn't happen again, I am going to generate the SSH keys first and set up the server second. 

SSH keys are needed to use PuTTY (regular PuTTY not PuTTYgen) to log into the server. Since I'm working on Windows, usinging PuTTYgen (a program that comes with PuTTY that generates SSH keys) seems like the easiest solution. 

#### 1. Download PuTTY (already done)

I already have PuTTY installed on my Windows 10 Machine at home and at work. The download link is below:

![Download PuTTY](https://www.putty.org/)

PuTTY seems to want you to install lots of extra stuff when you run the installer. I didn't install any of the "offers" that popped up during installation.


#### 2. Start PuTTYgen and create SSH key

I went through this tutorial to about setting SSH key on Windows for Digital Ocean when I created the first SSH key:

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

#### 3. Save SSH public and private keys to Documents folder

In the Actions section click [Save Public Key] and click [Save Public Key]

![Putty in Windows Start Menu](/posts/jupyter_hub/puttygen_save_public_private_key.png)

Make sure to save both the public and the private keys. Save these keys to an accessible folder. I saved my first keys in the default location and later I couldn't get to them. I created a folder in the Documents folder called ssh-keys and saved the public and private keys in there. I saved the public key with the name: public_key_jupyter_hub.txt. Digital Ocean documentation recommends a .txt file extension for the public key. The private key should have a .ppk file extension.

![Putty in Windows Start Menu](/posts/jupyter_hub/puttygen_public_key_save_name.png)

#### 4. Copy the public key to clipboard

Before closing PuTTYgen, make sure to copy the contents of the Public Key to the clipboard. We'll need this when we create the server. Copy all of the contents including the rsa line. 

### Results

After completing these steps, we have a public and private SSH key saved in Documents/ssh-keys. We also have the contents of the publish SSH key saved to the clipboard.

### Next Steps

Next, we'll go to Digital Ocean and create a new droplet. We will set up the new droplet to contain our SSH keys.