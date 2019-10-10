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

Ansible is an orchestration tool that can be used to configure cloud servers. In this post, I'll try and solidify my knowlege of what Ansible is, what Ansible is not and what is the vocabulary used to describe what Ansible does.

## Ansible is an IT Orchestration Tool

Ansible is a tool to automate IT orchestration. What does IT orchestration mean?

In the purposes of this project: Automating JupyerHub Deployment, Ansible is a tool to automate setting up the cloud server that runs JupyerHub.

## Ansible is a run-time that executes automation tasks

## Ansible is a language used to automate IT tasks

## What does Ansible run on?

Ansible runs on MacOS, Ubuntu or other Linux distros. Ansible can be run on a local desktop or laptop. Ansible can also be run on a cloud server. It's my understanding that Ansible does not have to be installed on the cloud server that Ansible is configuring. In my case, that means that Ansible does not run on the JupyterHub server. Ansible runs on a laptop, desktop, or cloud server that configures the JupyterHub server. 

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

## Ansible Vocabulary

There are a number of words that mean specific things when applied to Ansible. These words include:

 * playbook
 * play
 * module
 * task
 * handler
 * inventory
 * host

### Playbooks

An Ansible playbook is a yaml file that contains human and machine readble commands to run IT orchestration tasks. 

### Play

Ansible playbooks contain plays. A play is a section of commands in a playbook. A playbook can contain one play or many plays. 

### Tasks

Tasks are groups of commands. A play can contain one or many tasks. Tasks in a play run sequentially.


### Modules

Tasks contain modules. A module is one command or a several commands that run as part of a task.

 * Playbook
    * Play1
      * Task1
        * Module1
        * Module2
    * Handler 

    * Play2
      * Task1
        * Module1
      * Task2
        * Module1
        * Module1
    * Handler

### Handlers

Handlers are triggered by tasks and are run once at the end of a play. A completed play can have one handler or many handlers.




### Inventory

An inventory is a list of servers that Ansible is going to set up. The inventory can contain one server or many servers.

### Hosts

A host is cloud server or local computer. Inventories are made up of one or more hosts. There is also a host running Ansible which is not part of the inventory, that's the Ansible host sending out orchestration commands.
