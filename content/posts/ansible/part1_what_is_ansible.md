Title: Automating JupyterHub Deployment: Part 1 - What is Ansible?
Date: 2019-10-10 19:36
Modified: 2019-10-10 19:50
Status: Draft
Category: Python
Tags: python, jupyterhub, ansible, automation 
Slug: what-is-ansible
Authors: Peter D. Kazarinoff
Series: Automating JupyterHub Deployment
series_index: 1

![conductor]({static}/posts/ansible/images/conductor.png)

Ansible is an orchestration tool that can be used to configure cloud servers. In this post, I'll try and solidify my knowlege of what Ansible is, what Ansible is not and demistify the vocabulary used to describe what Ansible does.

## Ansible is an IT Orchestration Tool

Ansible is a tool to automate IT orchestration. What does IT orchestration mean?

![conductor]({static}/posts/ansible/images/robot_factory.jpg)

In the purposes of this project: Automating a JupyerHub Deployment, Ansible is a tool to automate setting up the cloud server that runs JupyerHub. So my IT orchestration is setting up JupyerHub to run on a cloud server with all my custom configuration and settings.

## Ansible is a run-time that executes automation tasks

![runtime]({static}/posts/ansible/images/runtime.png)

Ansible is a program that runs on a desktop, laptop or cloud server that executes automation tasks. The Ansible run-time executes the actions specified by a set of user-defined rules.

## Ansible is a language used to automate IT tasks

![document icon]({static}/posts/ansible/images/document_icon.png)

The steps Ansile goes through to create, configure and customize cloud servers is specified by valid Ansile syntax. The files a user creates and runs using Ansible must conform to this syntax or they will not be executed.

## What does Ansible run on?

![operating systems]({static}/posts/ansible/images/operating_systems.png)

Ansible runs on MacOS, Ubuntu or other Linux distros. Ansible can be run on a local desktop or laptop and also run on a cloud server. It's my understanding that Ansible does not have to be installed on the cloud server that Ansible is configuring. In my case, that means that Ansible does not run on the JupyterHub server. Ansible runs on a laptop, desktop, or cloud server that configures the JupyterHub server. 

Ansible does not run on Windows. I tried to install Ansible using both **pip** and **conda** on a Windows 10 machine. The result was unsuccessful.

```text
(ansible) C:\Users\student\staticsite>pip install ansible
(ansible) C:\Users\student\staticsite>ansible --version
Traceback (most recent call last):
  File "C:\Users\student\AppData\Local\conda\conda\envs\ansible\Scripts\ansible-script.py", line 44, in <module>
    from ansible.utils.display import Display
  File "C:\Users\student\AppData\Local\conda\conda\envs\ansible\lib\site-packages\ansible\utils\display.py", line 21, in <module>
    import fcntl
ImportError: No module named fcntl
```

![ubuntu WSL]({static}/posts/ansible/images/ubuntu_wsl.png)

However, I did get Ansible to successfully install on WSL (Windows Subsystem for Linux). The installation procceeded error-free using the following commands.

```text
sudo apt-get update
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible
```

After Ansible was installed on WSL, the ```--version``` attribute returned the output below:

```text
peter@DESKTOP-TJDVNOC:~$ ansible --version
ansible 2.5.1
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/peter/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.15+ (default, Oct  7 2019, 17:39:04) [GCC 7.4.0]
```

## Ansible Vocabulary

![ubuntu WSL]({static}/posts/ansible/images/dictionary.png)

There are a number of words that mean specific things when applied to Ansible. These words include:

 * **control node**
 * **managed node**
 * **playbook**
 * **play**
 * **module**
 * **task**
 * **handler**
 * **inventory**

### Control node

A control node is a computer with Ansible installed that runs Ansible playbooks and orchestrates cloud servers. In my case the control node will be a laptop or desktop running Windows10 and Windows Subsystem for Linux. The control node needs to have Ansible installed on it and it must have access to the internet. 

### Managed node

A managed node is a cloud server that is created, configured and customized by a control node and a set of pre-defined rules. In my case, the managed node is the cloud server running JupyterHub. In the past I have run Digital Ocean Cloud servers, so that's probably what I'll use when working with Ansible. 

### Playbooks

An Ansible playbook is a yaml file that contains human and machine readable commands to run IT orchestration tasks. Playbooks are saved and run on control nodes.

### Play

Ansible playbooks contain plays. A play is a section of commands in a playbook. A playbook can contain one play or many plays.

### Tasks

Tasks are groups of commands. A play can contain one or many tasks. Tasks in a play run sequentially.


### Modules

Tasks contain modules. A module is one command or a several commands that run as part of a task. There are modules for installing packages, running bash commands and dealing with git on managed nodes.

### Handlers

Handlers are triggered by tasks and are run once at the end of a play. A completed play can have one handler or many handlers.

#### Playbook

   * Play1
     * Task1
       * Module1
       * Module2
   * --> Handler 

   * Play2
     * Task1
       * Module1
     * Task2
       * Module1
       * Module1
   * --> Handler

### Inventory

An inventory is a list of servers (a list of manged nodes) that Ansible is going to set up. The inventory can contain one server or many servers. In my case, the inventory will just contain one server, the Digital Ocean cloud server running JupyterHub.

## Summary of Ansible Vocabulary

How about a couple sentences to bring all these words together:

> Ansible runs playbooks on a control node that configures managed nodes in your inventory. Playbooks are made up of plays. Plays are made up of tasks. Tasks contain modules. At the end of an executed play, a handler is run.
