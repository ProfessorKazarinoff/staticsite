Title: Adding Material Properties to Stress Strain Curves with Python and matplotlib
Date: 2019-02-16 16:01
Modified: 2019-02-16 16:01
Status: Draft
Category: matplotlib
Tags: python, matplotlib, engineering, materials science
Slug: python-matplotlib-stress-strain-properties
Authors: Peter D. Kazarinoff

Plotting stress strain curves is a useful skill in mechanical engineering because it allows Engineers to derive mechanical properties of materials such as tensile strength, elastic modulus, yield strength and ductility. 

In a previous post, we plotted a stress-strain curve using Python and Matplotlib. The resulting stress strain curve is below.

![simple line plot]({static}/images/stress_strain_curve3.png)

In this post, we will derive mechanical properties from the stress strain curve. The mechanical properties we will derive are: tensile strength (TS), yield strength (YS), elastic modulus (E), and ductility (%EL). In order to do calculate these four material properties from a stress strain curve, we need to have a couple things in place:

1. Python (to run the program) 
2. the Anaconda Prompt (to create a virtual environment and install pip)
3. conda (to download and install NumPy, Pandas and Matplotlib)
4. Matplotlib, NumPy, and Pandas (to plot the stress strain curve and read the .csv data file)
5. data.csv (the data collected from a mechanical test frame that we will plot)
6. **_tensiletest.py_** script from the previous post

Let's get going. First, we will activate our  ````(tensiletest)``` virtual environment. I'm used **conda** to create the virtual environment. Select the **Anaconda Prompt** from the windows start menu.

![conda prompt on windows start menu]({static}/images/conda_in_windows_start_menu.png)


Once you have the Anaconda Prompt open, type the following command:

```text
> activate tensiletest
(tensiletest) >
```

No we need to start editing our **_tensiletest.py_** script. This is the script we built in the a previous post.
