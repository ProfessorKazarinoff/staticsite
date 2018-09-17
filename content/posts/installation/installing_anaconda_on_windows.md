Title: Installing Anaconda on Windows
Date: 2017-11-14 09:20
Modified: 2017-11-14 09:21
Category: Orientation
Tags: python, anaconda, miniconda, conda, windows
Slug: installing-anaconda-on-windows
Authors: Peter D. Kazarinoff
Summary: In this post, we will run through installing the [Anaconda distribution](https://www.anaconda.com/what-is-anaconda/) of Python on Windows 10. I think the Anaconda distribution of Python is the the best option for undergraduate engineers who want to use Python. Anaconda is free (although the download is large which can take time) and can be installed on school or work computers where you don't have administrator access or the ability to install new programs.

In this post, we will run through installing the [Anaconda distribution](https://www.anaconda.com/what-is-anaconda/) of Python on Windows 10. I think the Anaconda distribution of Python is the the best option for undergraduate engineers who want to use Python. Anaconda is free (although the download is large which can take time) and can be installed on school or work computers where you don't have administrator access or the ability to install new programs.

#### Steps:

1. Visit [Anaconda.com/downloads](https://www.anaconda.com/download/)

2. Select Windows

3. Download the **_.exe_** installer

4. Open and run the **_.exe_** installer

5. Open the **Anaconda Prompt** and run some Python code

 <br />


#### 1. Visit the Anaconda downloads page

Go to the following link: [Anaconda.com/downloads](https://www.anaconda.com/download/)

The Anaconda Downloads Page will look something like this:

![anaconda download page](images/anaconda_download_page.png)


 <br />

#### 2. Select the Windows

Select Windows where the three opperating systems are listed.

![anaconda select Windows](images/anaconda_select_windows.png)


 <br />

#### 3. Download

Download the Python 3.6 distribution. Python 2.7 is legacy Python. For undergraduate engineers, select the Python 3.6 version. If you are unsure about a 32-bit version vs a 64-bit version, most Windows installations are 64-bit. 

![anaconda select python 3.6](images/anaconda_python3_or_python2.png)

You may be prompted to enter your email. You can still download Anaconda if you click **[No Thanks]** and don't enter your Work Email address.

![anaconda](images/anaconda_enter_email.png)

The download is quite large (over 500 MB) so it may take a while for the download to complete.

![anaconda downloading](images/anaconda_downloading.png)


 <br />

#### 4. Open and run the installer

Once the download completes, open and run the **_.exe_** installer

![anaconda installer](images/anaconda_run_installer.png)

At the beginning of the install you will need to click **[Next]** to confirm the installation,

![anaconda installer click next](images/anaconda_installer_click_next.png)

and agree to the license.

![anaconda license](images/anaconda_agree_to_license.png)

At the Advanced Installation Options screen, I recommend that you **do not check** "Add Anaconda to my PATH environment variable"

![anaconda path variable](images/anaconda_path2.png)


 <br />

#### 5. Open the Anaconda Prompt from the Windows start menu

After the Anaconda install is complete, you can go to the Windows start menu and select the Anaconda Prompt

![anaconda in start menu](images/anaconda_from_start_menu.png)

This will open up the Anaconda Prompt, which is often called the **Conda prompt**. Anaconda is the Python distribution and the Conda prompt is a command line tool (a program where you type in your commands instead of using a mouse). It doesn't look like much, but it is really helpful for an undergraduate engineer using Python.

![anaconda prompt](images/anaconda_window.png)

At the Anaconda Prompt, type ```python```. This will start the Python interperater. 

![conda prompt type python](images/conda_prompt_type_python.png)

Note the Python version. You should see something like ```Python 3.6.1```.  With the interperter running, you will see a set of greater-than symbols ```>>>``` before the cursor. 

![anaconda prompt](images/conda_type_python.png)

Now you can type Python commands. Try typing ```import this```. You should see the **_Zen of Python_** by Tim Peters

![anaconda_import_this](images/conda_import_this_output.png)

To close the Python interperater, type ```exit()``` at the interperator prompt ```>>>```.  Note the double parenthesis at the end of the command. The ```()``` is needed to stop the Python interperator and get back out to the Conda prompt.

To close the Conda prompt, you can either close the window with the mouse, or type ```exit```.


 <br />
 
#### Congratulations! You installed the Anaconda distribution on your Windows computer!

When you want to use the Python interperater again, just click the Windows Start button and select the **Anaconda Prompt** and type ```python```.