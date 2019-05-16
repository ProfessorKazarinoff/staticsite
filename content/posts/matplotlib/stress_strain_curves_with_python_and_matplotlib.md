Title: Plotting Stress Strain Curves with Python and matplotlib
Date: 2019-02-16 09:01
Modified: 2016-02-16 09:01
Status: Draft
Category: matplotlib
Tags: python, matplotlib, engineering, materials science
Slug: python-matplotlib-stress-strain
Authors: Peter Kazarinoff

![stress strain curve 3]({static}/images/stress_strain_curve3.png)

Plotting stress strain curves is a useful skill in mechanical engineering because it allows Engineers to derive mechanical properties of materials such as tensile strength, elastic modulus, yield strength and ductility. Plotting stress strain curves can be accomplished with Excel and MATLAB, but what about plotting stress strain curves with Python? Follow along to find out.

In this post, we'll plot the stress strain curve of Aluminum 6061 - T6 from raw data stored in a .csv file. In order to build the stress strain curve, we need to have a couple things in place:

1. Python (to run the program). My choice is to install [Anaconda](https://anaconda.com/downloads) 
2. the Anaconda Prompt (to create a virtual environment and install the packages we need)
3. conda (to download and install matplotlib, numpy and pandas)
4. Matplotlib, Numpy and Pandas (to plot the stress strain curve and read the .csv data file)
5. data.csv (the data collected from a mechanical test frame)

As a first step, we should create a a new virtual environment. Python virtual environments are useful because they create an isolated environment that our Python script will run in. Let's call our virtual environment tensiletest. I'm using **conda** to create the virtual environment. Select **Anaconda Prompt** from the windows start menu.

![conda prompt on windows start menu]({static}/images/conda_in_windows_start_menu.png)

Once you have the Anaconda Prompt open, type the following command:

```text
conda create -m tensiletest python=3.7
```

Next, we need to activate our ```(tensiletest)``` virtual environment with the command ```conda activate```. Note that once the virtual environment is activate, we see ```(tesiletest)``` before the Anaconda prompt.

```text
conda activate tensiletest
```

Now that the virtual enviroment has been created and activated, we need to install three Python packages using the Anaconda Prompt. The first Python package is NumPy. We will use NumPy to run some calculations on our data. The second package we need to install is Matplotlib. We will use Matplotlib to plot the data. Both Python pacages are installed with ```conda``` at the Anaconda Prompt. Remember, make sure you are in your ```(tensiletest)``` virtual environment when you install these packages.

The commaned below installs NumPy and Matplotlib into the the ```(tensiletest)``` virtual environment.

```text
(tensiletest)$ conda install numpy
(tensiletest)$ conda install matplotlib
```

The last Python package we'll install is Pandas. We will use Pandas to import our **_data.csv_** file, and pull out the columns we need to make the stress strain curve. 

The commaned below installs Pandas into the the ```(tensiletest)``` virtual environment.

```text
(tensiletest)$ conda install pandas
```

To make sure that NumPy, Pandas, and Matplotlibare installed in our ```tensiletest``` virtual environemnt, type:

```text
(tensiletest) $ conda list
```

The output should look something like below. Note that ```matplotlib```, ```numpy``` and ```pandas``` are all installed.

```text
certifi==2017.7.27.1
chardet==3.0.4
cycler==0.10.0
idna==2.6
matplotlib==2.0.2
numpy==1.13.3
pandas==0.20.3
pyparsing==2.2.0
python-dateutil==2.6.1
...

```

Great! Now it is time to start coding. Create a new Python file using your favorite editor (I use Visual Studio Code) called **_tensiletest.py_**. Make sure that the **_data.csv_** file is in the same directory as your **_tensiletest.py_** file. 

At the start of the script, import NumPy, Pandas, and Matplotlib:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

In the next part of our **_tensiletest.py_** script, we need to read in the data from the ***data.csv*** data file. To read the .csv file, we will use Panda's ```pd.read_csv()``` method. We set ```sep=','``` because our **_data.csv_** file uses commas ```,``` to seperate columns. We use ```header=0``` to use the headers from our **_data.csv_** file as the headers in our Pandas dataframe. We can also print out the data using the ```print()``` function

```python
df=pd.read_csv('data.csv', sep=',',header=0)
print(df.head())
```

Now let's see if we can run our **_tensiletest.py_** script from the conda command line. Make sure that you are still in your ```tensiletest``` virtual environment. 

```text
(tensiletest) > tensiletest.py

     Time (s)  Position (m)  Force (N)  Speed (mm/min)
0         0.0      0.000000          0             NaN
1         0.2      0.000000          0            0.00
2         0.4      0.000000          0            0.00
3         0.6      0.000000          0            0.00
4         0.8      0.000000          0            0.00
5         1.0      0.000000          0            0.00

```

Great! Python and Pandas are able to read in our **_data.csv_** file and save it to a Pandas dataframe. Let's try a simple plot just using Matplotlib, but just to make sure it works. In **_tensiletest.py_** file add:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',',header=None,skiprows=1)
print(df)

plt.plot(df[1], df[2])
plt.show()
```

If everything works correctly, you should see a plot that looks something like the following:

![simple line plot]({static}/images/simple_plot.png)

OK, now we need to manipulate the data a little bit. The ```df[1]``` column in our data set is the **extension** or **change in length**. The ```df[2]``` column in our data set is **force**. We need to convert the **change in length** to strain and we need to convert the **force** to stress. We need to define some sample parameters to convert **extension** and **force** to strain and stress:

```python
# sample parameters
d = 1.778     # diameter of sample in mm
A0 = np.pi*(d/2)**2 # original cross-sectional area of sample in mm^2
L0 = 18.002   # original gauge length of sample (lenth of narrowest section)
```

Stress strain curves have **strain** on the x-axis, not **change in length**, so we need to convert our **change in length** to **strain**. The equation to use is below.

$$\epsilon = \frac{\Delta L}{L_0}$$

Where $\epsilon$ is strain, $\Delta L$ is the change in length or extension, and $L_0$ is the original length. 

Stress strain curves have **stress** on the y-axis, not **force**, so we also need to convert our **force** to **stress**. The equation to use is below.

$$\sigma = \frac{F}{A_0}$$

Where $\sigma$ is stress, $F$ is force and $A_0$ is the original cross-sectional area of the sample. We need to code the mathematical operations above into our **_tensiletest.py_** script. 

```python
# calculate stress and strain
stress = (force/A0)
strain = delta_L/L0
```

Now let's plot the stress-stain curve with Matplotlib. We'll put strain on the x-axis and stress on the y-axis.

```python
# Plot the stress-strain curve
plt.plot(strain,stress)
plt.show()
```

When you run the **_tensiletest.py_** script, you should see the stress strain curve below:

![simple line plot]({static}/images/stress_strain_curve1.png)

The stress-strain curve above looks pretty good. But we still need to add some axis labels with units using Matplotlib's ```plt.ylabel()``` and ```plt.xlabel()``` methods. Let's also add a title with the ```plt.title()``` method. Ensure the plot customization lines are in between the ```plt.plot()``` and the ```plt.show()``` lines, otherwise the title and axis labels won't show up on the plot.

```python
# plot the stress strain curve
plt.plot(strain,stress)
plt.xlabel('Strain (mm/mm)')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curve of Al6061 - T6')
plt.show()
```

When the script is run, you should see a plot that looks like the plot below that contains axis labels and a title.

![stress strain curve axis labels and title]({static}/images/stress_strain_curve2.png)

In this last step, we are going to make some changes to the axis limits of the plot. Notice how the plot doesn't start at **strain=0** or **stress=0**. We can change the axis limits using ```plt.axis([Xmin, Xmax, Ymin, Ymax])``` where ```Xmin``` and ```Xmax``` are our x-axis limits and ```Ymin``` and ```Ymax``` are our y-axis limits. We are also going to add a grid by setting ```plt.axis()``` to ```True```.

```python
# plot the stress strain curve
plt.plot(strain,stress)
plt.xlabel('Strain (mm/mm)')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curve of Al6061 - T6')
plt.axis([0, 1.4, 0, 60])
plt.grid(True)
plt.show()
```

The final plot produced by the **_tensiletest.py_** script is shown below.

![simple line plot]({static}/images/stress_strain_curve3.png)

The complete **_tensiletest.py_** script is below.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('data.csv', sep=',',header=None,skiprows=1)
print(df)

#plt.plot(df[1], df[2])
#plt.show()

delta_L = np.array(df[1])*1000  
print(delta_L)
force = np.array(df[2])
print(force)

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
plt.show()
```
