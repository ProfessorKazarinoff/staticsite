Title: Create a new virtual environment with Conda
Date: 2017-11-17 20:20
Modified: 2017-11-17 20:20
Status: published
Category: Orientation
Tags: python, conda, virtualenv, anaconda, anaconda prompt
Slug: new-virtual-environment-with-conda
Authors: Peter D. Kazarinoff

To start a new Python project, it is best practice to create a new virtual environment. I have the **Anaconda** distribution of Python installed on my Windows 10 machine at work. When you [install **Anaconda**]({filename}installing_anaconda_on_windows.md), it comes with the very useful **Anaconda Prompt**. Using the **Anaconda Prompt** is a bit like using the terminal on a Mac OSX or Linux. To start the **Anaconda Prompt** on Windows 10, go to the Windows start button on the lower left and select **Anaconda Prompt**. 

![anaconda in start menu](images/anaconda_from_start_menu.png)

To create the new environment, we need to issue the following command at the prompt:

```terminal
conda create --name webscrape python=3.6
```

The ```conda create``` command builds the new virtual environment. The ```--name webscrape``` flag gives our new virtual environment the name ```webscrape```.  I like to name my virtual environments the same name as the project that I will use that environment for, or after the name of the package that will be used the most.  Including ```python=3.6``` ensures that your virtual environment has an up to date version of python. 

Conda will tell us:

```terminal
The following NEW packages will be INSTALLED:

    certifi:        2016.2.28-py36_0
    pip:            9.0.1-py36_1
    python:         3.6.2-0
    setuptools:     36.4.0-py36_0
    vs2015_runtime: 14.0.25420-0
    wheel:          0.29.0-py36_0
    wincertstore:   0.2-py36_0

Proceed ([y]/n)? y
```

Type ```y``` to confirm that you want to create the new virtual environment. To use the new virtual environment ```webscrape``` you need to _activate_ it by typing:

```terminal
activate webscrape
```

You know you are in your virtual environment ```webscrape``` when ```(webscrape)``` is in parenthesis at the start of the prompt:

```terminal
(webscrape) tribilium@Den-PC:~$
```

To deactivate an active environment, use:

```terminal
deactivate
```

<br />

For power-users using the terminal on Mac or Linux, you must use ```source activate``` to enter into the virtual environment.


```terminal
source activate webscrape
```

and

```terminal
source deactivate webscrape
```

<br />


If you see the ```(webscrape)``` in parenthesis before the command prompt, that means you set up the new virtual environment and are now using it. You can view a list of your virtual environments using the ```conda info --envs``` or ```conda env list``` command.

```terminal
conda info --envs

# conda environments:
#
matplotlib               /home/tribilium/anaconda3/envs/matplotlib
webscrape              * /home/tribilium/anaconda3/envs/pelican
root                     /home/tribilium/anaconda3
```

Notice the ``` * ``` asterisk on the line with ```webscrape```. The virtual environment with the ``` * ``` is currently active. 

To exit the virtual environment, use the command ```deactivate```. If you run ```conda env list``` again, you'll see there is no ```*``` in front of ```webscrape```. That's because you are not currently in that virtual environment.

```terminal
conda env list

# conda environments:
#
matplotlib               /home/tribilium/anaconda3/envs/matplotlib
webscrape                /home/tribilium/anaconda3/envs/pelican
root                  *  /home/tribilium/anaconda3
```

We can spin up the virtual environment again with the ```activate``` command.