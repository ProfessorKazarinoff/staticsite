Title: Automating JupyterHub Deployment with Ansible: Part 2 - Installing Ansible
Date: 2020-06-29 19:36
Modified: 2019-10-14 19:50
Status: Draft
Category: Python
Tags: python, jupyterhub, ansible, automation 
Slug: installing-ansible
Authors: Peter D. Kazarinoff
Series: Automating JupyterHub Deployment with Ansible
series_index: 2

![conductor]({static}/posts/ansible/images/dump_truck.jpg)

In this post, I'm going to review how to install Ansible on the computer or server that will run Ansible and act as the conductor setting up JupyterHub on a cloud server server.  JupyterHub will run on the cloud server, but that isn't the server that Ansible needs to be installed on. Ansible is installed on a seperate machine that sends commands to the JupyterHub server over SSH. 

## What can Ansible be installed on?

Ansible can be installed  on a MacOS or Linux computer or a Linux cloud server. Ansible can also be installed on Windows Subsystem for Linux (WSL). Ansible can not run on Windows 10. During my testing and exploration of Ansible, I've used both WSL and an Ubuntu cloud server to run Ansible.

## Anstalling Ansible

Ansible can be installed on the command line using both a Linux system package manager like **apt** or **yum**. Since Ansible is a Python package, Ansible can also be installed with a Python package manager like **pip** or **conda**. The Ansible docs state the install preference is to use a system package manager. So on both WSL and an Ubuntu cloud server, I installed Linux with **apt**, the Debian/Ubuntu package manager. 

Using a terminal, the commands below install Ansible an a Debian/Ubuntu system:

```text
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
```

Ansible should now be installed.

## Confirm the Ansible installation

After Ansible is successfully installed, the commands below print the Ansible version and indicate a successful installation.

```text
ansible --version
```

The output should include something like ```ansible 2.8.5```. Asible's command line documentation can be called with the command below.

```text
ansible --help
```

## Summary

In this post, we reviewed how to install Ansible on WSL or a Linux computer.

## Next post

In the next post, we will write and run our first Ansible playbook.
 