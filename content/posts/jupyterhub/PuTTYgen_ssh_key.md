Title: Create an SSH Key with PuTTYgen
Date: 2018-05-19 12:40
Modified: 2018-05-19 12:40
Status: published
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: ssh-keys-with-putty
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 2
Summary: This is the second part of a multi-part series on how to set up Jupyter Hub for a class. This is my first time setting up a Jupyter Hub server. I am primarily writing to my future self as I may need to set up Jupyter Hub again for another class. In this post, we are going to create an SSH key on a Windows 10 machine using PuTTYgen.

This is the second part of a multi-part series on how to set up Jupyter Hub for a class. This is my first time setting up a Jupyter Hub server. I am primarily writing to my future self as I may need to set up Jupyter Hub again for another class. In this post, we are going to create an SSH key on a Windows 10 machine using PuTTYgen.

### Posts in this series

1. [Why Jupyter Hub?]({filename}/posts/jupyterhub/why_jupyter_hub.md) 
2. **Create ssh key, save to documents/ssh-keys** (this post)
3. Create a new Digital Ocean Droplet with a non-root sudo user
4. Install Jupyter Hub on the server
5. Apply SSL, link a domain name to the server and configure nginx
6. Connect OAuth to Jupyter Hub
7. Connect to Jupyter Hub as student

### Steps in this post

1. Download PuTTY for Windows
2. Start PuTTYgen and create SSH key
3. Save SSH public and private keys to Documents folder
4. Copy the public key to clipboard

### Why SSH keys, PuTTYgen and why do this first?

When I set up the server on Digital Ocean the first time, one of the initial server setup steps was to add SSH keys so the server has them when it initialized. 

I tried to create and save the keys to the Digital Ocean dashboard so the SSH keys would be on the server when it first started. But I goofed up somehow and the server started without any SSH keys. It was a BIG PAIN adding SSH keys after the server started for the first time. 

I ended up copying the public key into pastebin.com, logging onto the server with the Digital Ocean console and using ```wget``` to bring a textfile of the SSH key from pastebin.com onto the server and then ```mv``` to copy the key name into the right location.

I'm pretty sure that pasting a public SSH key into pastebin.com is not the best way to initially set up a server. So to make sure that doesn't happen again, I am going to generate the SSH keys first and set up the server second. 

SSH keys are needed to use PuTTY (regular PuTTY not PuTTYgen) to log into the server. Since I'm working on Windows, using PuTTYgen (a program that comes with PuTTY that generates SSH keys) seems like the easiest solution. 

#### 1. Download PuTTY

I already have PuTTY installed on my Windows 10 machines at home and at work. The download link is below:

[Download PuTTY](https://www.putty.org/)

PuTTY seems to want you to install lots of extra stuff when you run the installer. I didn't install any of the "offers" that popped up during installation.


#### 2. Start PuTTYgen and create SSH key

I went through this tutorial to about setting SSH key on Windows for Digital Ocean when I created the first SSH key:

[How To Use SSH Keys with PuTTY on DigitalOcean Droplets (Windows users)](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-putty-on-digitalocean-droplets-windows-users)

Using the Windows start menu, open PuTTYgen (not regular PuTTY):

![PuTTYgen in Windows Start Menu](/posts/jupyterhub/puttygen_in_start_menu.png)

![Putty in Windows Start Menu](/posts/jupyterhub/puttygen_key_generator.png)

Use the following parameters

 * Type of key to generate: RSA
 * Number of bits in generated key: 2048

Then click [generate]

![PuTTYgen generate](/posts/jupyterhub/puttygen_generate.png)

This will bring up a dialog to move the mouse around the empty area to generate some randomness. This is my favorite part. Just move the mouse around the dialog box until the progress bar ends. Fun.

![PuTTYgen key generator](/posts/jupyterhub/puttygen_key_generator.png)

When the next screen pops up, right-click and copy the contents of the Public Key. We'll need the public key contents available to paste into the server's SSH ```authorized_keys``` file. Include the rsa line in the text copied to the clipboard.

#### 3. Save SSH public and private keys to Documents folder

In the [Actions] section click [Save public key] and click [Save private key]

![PuTTYgen save public and private keys](/posts/jupyterhub/puttygen_save_public_private_key.png)

Make sure to save both the public and the private keys. Save these keys to an accessible folder. The first time I generated SSH keys, I saved the keys in the default location and couldn't access them later. The second time I created SSH keys, I created a folder in the Documents folder called ssh-keys and saved the public and private keys in Documents/ssh-keys. I saved the public key with the name: ```public_key_jupyter_hub.txt```. The Digital Ocean documentation recommends a .txt file extension for the public key (so you can open it and copy the contents). The private key should have a .ppk file extension.

![PuTTYgen save public key name](/posts/jupyterhub/puttygen_public_key_save_name.png)

#### 4. Copy the public key to clipboard

Before closing PuTTYgen, make sure to copy the contents of the Public Key to the clipboard. We'll need this when we create the server. Copy all of the contents including the rsa line. 

### Results

After completing these steps, we have a public and private SSH key pair saved in Documents/ssh-keys. We also have the contents of the public SSH key saved to the clipboard.

### Next Steps

Next, we'll create a new server on Digital Ocean (called a _droplet_). Then we'll use the SSH keys we just created to log into the server and create a non-root sudo user.