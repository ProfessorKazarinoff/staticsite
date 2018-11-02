Title: Installing JupyterHub the Second Time - Part 2
Date: 2018-10-31 12:40
Modified: 2018-10-31 12:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: installing-jupyter-hub-the-second-time-part2
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Summary: This is the second time that I've set up JupyterHub to run for a college class. This time, I am making a couple of chnages to the deployment. This post is a record of those changes of running JupyterHub in a college class for the second time. To see how to set up JupyterHub for your ownn college class, see my previous series on JupyterHub starting with [Why Jupyter Hub?]({filename}/posts/jupyterhub/why_jupyter_hub.md) 

## Google OAuth

Log into Google API console

Credentials --> Create Credentials --> OAuth client ID

Need to set the Javascript Origins to mydomain.org

Need to set the OAuth callback URL to mydomain.org/hub/oauth_callback

I had trouble this second time getting Google OAuth to work. Local PAM OAuth worked, but I couldn't get Google logins to work. So I took a break and tried GitHub OAuth and GitHub logins. This worked just fine, so after a day, I tried Google OAuth again. The second time, I noticed an error in the jupyterhub_config file, the oauth_callback_ulr (sp?!) parameter was spelled incorrectly. When I changed it to oauth_callback_url, the system worked. 

## Summary

In this post we installed **Anaconda** on the server using a shell script. We added **conda** to our path and reloaded our .bashrc file. Then we installed some extra **Python** packages such as **pint** and **pyserial**. Finally we installed **jupyterhub**, opened up port 8000 and ran **jupyterhub** for the first time! Remember we **shut down jupyter hub very quickly** because we ran it without any SSL security.

<br>

### Next Steps

In the next post we will build SSL security into our Jupyter Hub deployment and connect the server to domain name. Plus we'll customize the **jupyterhub** config file and install and use nginx as a proxy server.

