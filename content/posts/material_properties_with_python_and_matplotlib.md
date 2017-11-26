Title: Adding Material Properties to Stress Strain Curves with Python and matplotlib
Date: 2017-10-03 16:01
Modified: 2017-10-03 16:01
Status: Draft
Category: matplotlib
Tags: python, matplotlib, engineering, materials science
Slug: python-matplotlib-stress-strain-properties
Authors: Peter Kazarinoff
Series: stress-strain curves in python 
series_index: 2
Summary:

Plotting stress strain curves is a useful skill in mechanical engineering because it allows us to derive mechanical properties of materials such as tensile strength, elastic modulus, yield strength and ductility. 

In the previous post, we plotted the stress-strain curve for Al 6061 - T6. The resulting plot is below

![simple line plot]({filename}/images/stress_strain_curve3.png)

Now we will then derive mechanical properties from the plot, tensile strength (TS), yield strength (YS), elastic modulus (E), and ductility (%EL). In order to do this, we need to have a couple things in place:

1. python (to run the program) 
2. conda and a conda prompt (to create a virtual environment and install pip)
3. pip (to download and install matplotlib and pandas)
4. matplotlib and pandas (to plot the stress strain curve and read the .csv data file)
5. data.csv (the data collected from a mechanical test frame that we will plot)
6. ***tensiletest.py*** script from the previous post

To get going, first we will enter into our  ````(tensiletest)``` virtual environment. I'm using **conda** to create the virtual environment. Select **Anaconda Prompt** from the windows start menu.

![conda prompt on windows start menu]({filename}/images/conda_in_windows_start_menu.png)


Once you have the conda prompt open, type the following command:

```
(C:\Users\peter.kazarinoff\AppData\Local\Continuum\Anaconda3) C:\Users\peter.kazarinoff>activate tensiletest
(tensiletest) C:\Users\peter.kazarinoff>

```

No we need to start editing our ***tensiletest.py*** file. This is the script we built in the last post.
