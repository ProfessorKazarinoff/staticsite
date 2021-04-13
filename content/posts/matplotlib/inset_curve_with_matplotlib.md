Title: Adding an Inset Curve with Python and matplotlib
Date: 2019-02-16 09:01
Modified: 2019-02-16 09:01
Status: Draft
Category: matplotlib
Tags: python, matplotlib, engineering, materials science
Slug: inset-on-stress-strain-curve-with-matplotlib
Authors: Peter D. Kazarinoff
Summary: Plotting stress strain curves is a useful skill in mechanical engineering because it allows Engineers to derive mechanical properties of materials such as tensile strength, elastic modulus, yield strength and ductility. Plotting stress strain curves can be accomplished with Excel and MATLAB, but what about plotting stress strain curves with Python? Follow along to find out.

Plotting stress strain curves is a useful skill in mechanical engineering because it allows Engineers to derive mechanical properties of materials such as tensile strength, elastic modulus, yield strength and ductility. Plotting stress strain curves can be accomplished with Excel and MATLAB, but what about plotting stress strain curves with Python? Follow along to find out.

In a previous post we built a stress strain curve using Python and Matplotlib. In this post, we are going to add an inset curve to the stress strain curve to show the elastic region. 

In order to add an inset curve on a Matplotlib plot, we need to make sure we have a couple things in place.

1. Python (to run the program) 
2. A virtual environment with Matplotlib, NumPy and Pandas installed
3. data.csv (the data collected from a mechanical test frame that we will plot)

To get going, let's log into our virutal environment using the Anaconda Prompt.

![conda prompt on windows start menu]({static}/images/conda_in_windows_start_menu.png)


Once you have the Anaconda Prompt open, type the following command to log into your virtual environment:

```text
(C:\Users\peter.kazarinoff\AppData\Local\Continuum\Anaconda3) C:\Users\peter.kazarinoff>activate tensiletest

(tensiletest) C:\Users\peter.kazarinoff>

```
To make sure that ```numpy``` and ```matplotlib``` and ```pandas``` are installed in our ```tensiletest``` virtual environemnt, type:

```
(tensiletest) C:\Users\Peter\Documents\staticsite\content\code\tensiletest>pip freeze
certifi==2017.7.27.1
chardet==3.0.4
cycler==0.10.0
idna==2.6
matplotlib==2.0.2
numpy==1.13.3
pandas==0.20.3
pyparsing==2.2.0
python-dateutil==2.6.1
pytz==2017.2
requests==2.18.4
six==1.11.0
urllib3==1.22
wincertstore==0.2
```

Next, let's run our previous script and to see the plot we have constructed so far. The full script that builds a stress strain curve is below:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in the data
df=pd.read_csv('data.csv', sep=',',header=None,skiprows=1)
delta_L = np.array(df[1])*1000  
force = np.array(df[2])

# sample parameters
d = 1.778     # diameter of sample in mm
A0 = np.pi*(d/2)**2 # original cross-sectional area of sample in mm^2
L0 = 18.002   # original gauge length of sample (lenth of narrowest section)

# calcuate stress and strain
stress = force/A0
strain = delta_L/L0

# plot the stress strain curve
plt.plot(strain,stress)
plt.xlabel('Strain (mm/mm)')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curve of Al6061 - T6')
plt.axis([0, 1.4, 0, 60])
plt.grid(True)
plt.show()
```

![stress strain curve]({static}/images/stress_strain_curve3.png)

Let's zoom into the linear elastic region, that's the region on the left-hand side of the curve where the plot is linear. In this region there is a direct relationship between stress and strain. The constant that relates stress and strain (the change in stress over the change in strain in the linear elastic region) is the elastic modulus E. The equation below shows the relationship:

E = delta_Stress / delta_Strain

![linear elastic region]({static}/images/linear_elastic_region.png)

To add this plot onto our main plot, we need to add the following to our **_tensiletest.py_** script:

```python
# this is the inset axes over the main axes
a = plt.axes([0.2, 0.2, .3, .3], facecolor='w')
plt.plot(strain, stress)
plt.title('Inset of Elastic Region')
plt.xlim(0, 0.05)
plt.ylim(0, 40)
```

This outputs the plot below:
![linear elastic region]({static}/posts/matplotlib/images/stress_strain_with_inset.png)

The entire Python script including the section to add the inset curve is below.

```python
# read in the data
df=pd.read_csv('data.csv', sep=',',header=None,skiprows=1)
delta_L = np.array(df[1])*1000  
force = np.array(df[2])

# sample parameters
d = 1.778     # diameter of sample in mm
A0 = np.pi*(d/2)**2 # original cross-sectional area of sample in mm^2
L0 = 18.002   # original gauge length of sample (lenth of narrowest section)

# calcuate stress and strain
stress = (force/A0)
strain = delta_L/L0

# plot the stress strain curve
plt.plot(strain,stress)
plt.xlabel('Strain (mm/mm)')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curve of Al6061 - T6')
plt.axis([0, 1.4, 0, 60])
plt.grid(True)

# inset axes overlayed on the main axes
a = plt.axes([0.2, 0.2, .3, .3], facecolor='w')
plt.plot(strain, stress)
plt.title('Inset of Elastic Region')
plt.xlim(0, 0.05)
plt.ylim(0, 40)

plt.show()
```
