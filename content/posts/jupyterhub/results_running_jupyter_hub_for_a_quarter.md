Title: Results from Running Jupyter Hub in a College Class
Date: 2018-09-07 10:40
Modified: 2018-09-07 10:40
Status: draft
Category: jupyter
Tags: jupyter, jupyter hub, jupyter notebooks, python
Slug: results-from-running-jupyter-hub-for-a-quarter
Authors: Peter D. Kazarinoff
Series: Jupyter Hub
Series_index: 9
Summary: This is the ninth part of a multi-part series settting up Jupyter Hub for a college class. The Jupyter Hub Server was used by 21 students in an introductory college Engineering class! Students logged in, wrote and ran code, and completed their assignments. In this post, I'll share my thoughts about setting up and running Jupyter Hub in the wild of a college Engineering class.

This is the ninth part of a multi-part series settting up Jupyter Hub for a college class. The Jupyter Hub Server was used by 21 students in an introductory college Engineering class! Students logged in, wrote and ran code, and completed their assignments. In this post, I'll share my thoughts about setting up and running Jupyter Hub in the wild of a college Engineering class.

### Posts in this series

1. [Why Jupyter Hub?]({static}/posts/jupyterhub/why_jupyter_hub.md)
2. [Create ssh key, save to documents/ssh-keys]({static}/posts/jupyterhub/PuTTYgen_ssh_key.md)
3. [Create a new Digital Ocean Droplet with a non-root sudo user]({static}/posts/jupyterhub/new_DO_droplet.md)
4. [Install Jupyter Hub on the server]({static}/posts/jupyterhub/installing_jupyterhub.md)
5. [Apply SSL, link a domain name to the server and configure nginx]({static}/posts/jupyterhub/SSL_and_nginx_with_jupyterhub.md)
6. [Connect OAuth to Jupyter Hub]({static}/posts/jupyterhub/authentication_and_jupyterhub_as_a_system_service.md)
7. [Add a custom login page and assignments directory for each user on a Jupyter Hub server]({static}/posts/jupyterhub/assignments_dir_and_custom_login_page.md)
8. [Initial first impressions of running Jupyter Hub live with students]({static}/posts/jupyterhub/first_live_results_with_students.md)
9. **Results from Running Jupyter Hub in a College Class** (this post) 


### Last time

In the last post [Initial first impressions of running Jupyter Hub live with students]({static}/posts/jupyterhub/first_live_results_with_students.md), I talked about my worries running Jupyter Hub with a live class and how none of the things I was scared about happend.

### What the big deal was today

The big deal today was that during lab this morning, 17 students (plus me) logged onto Jupyter Hub together - all at the same time - for the first time!

![Jupyter Hub Start Page]({static}/posts/jupyterhub/start_my_server_button.png)

I've tested the Jupyter Hub server for a couple weeks. One student logged in to the server and ran some notebooks. Another faculty member tested the server out too. But this morning was the first time all the students in one lab logged and ran notebooks all at the same time. 

### What I was nervous about

Before this morning, I was nervous about a couple of things in regards to the Jupyter Hub server

 * students in the class will not be able to log in
 * only some of the students will be able to log in
 * the server will go down because everyone is logging in and using Jupyter Hub at the same time
 * notes and assignments up on GitHub won't populate students' directory
 * students won't be able to run notebooks at the same time because the server gets overloaded. 

![file_browser_with_notes_and_assignments.png]({static}/posts/jupyterhub/file_browser_with_notes_and_assignments.png)


### What happened

I'm pleased to report **none of those worries came to fruition**. What happened this morning was:

 * All 17 students in the lab (plus me) logged into Juypter Hub successfully
 * The Jupyter Hub server did not crash or run super slow when students logged in
 * Each student got the assignments and notes from GitHub in their directory
 * Students looked at notebooks and ran code cells at the same time
 * The Jupyter Hub server never crashed

![live_notes_notebook_running.png]({static}/posts/jupyterhub/live_notes_notebook_running.png)

### What's next?

Students have 3 labs using Jupyter Hub over the next 3 weeks. I'm interested to see (and really hope) we don't have any problems with the server in while students are completing their labs. Besides the server running, I'm also interested to see how the notes ([posted on Github](https://github.com/ProfessorKazarinoff/ENGR101/tree/master/notes)) and assignments ([posted on Github](https://github.com/ProfessorKazarinoff/ENGR101/tree/master/assignments)) worked. Thank-you for all of your hard work.

So far Jupyter Hub is working great! I want to say a big thank-you to Numfocus and the folks working on Project Jupyter. The Jupter Hub server is providing a diverse group of students an opportunity to learn Python programming without the hassle of any installation steps, administrator rights, PATH variables, virtual environments or complicated IDE's.
