Title: Plotting Stress Strain Curves with Python and matplotlib
Date: 2017-10-03 09:01
Modified: 2017-10-03 09:01
Status: Draft
Category: matplotlib
Tags: python, matplotlib, engineering, materials science
Slug: python-matplotlib-stress-strain
Authors: Peter Kazarinoff
Series:
series_index:
Summary:

Plotting stress strain curves is a useful skill in mechanical engineering because it allows us to derive mechanical properties of materials such as tensile strength, elastic modulus, yield strength and ductility. Plotting stress strain curves can be accomplished with Excel and MATLAB, but what about plotting stress strain curves with Python? Follow along to find out.

What we are going to do in the following series of blog posts is plot the stress strain curve of Aluminum 6061 - T6. We will then derive mechanical properties from the plot, tensile strength (TS), yield strength (YS), elastic modulus (E), and ductility (%EL). In order to do this, we need to have a couple things in place:

1. Python (to run the program) 
2. Anaconda and the Anaconda Prompt (to create a virtual environment and install pip)
3. conda (to download and install matplotlib, numpy and pandas)
4. matplotlib, numpy and pandas (to plot the stress strain curve and read the .csv data file)
5. data.csv (the data collected from a mechanical test frame)

To get going, first we should create a up a new virtual environment, let's call it tensiletest. I'm using **conda** to create the virtual environment. Select **Anaconda Prompt** from the windows start menu.

![conda prompt on windows start menu]({filename}/images/conda_in_windows_start_menu.png)


Once you have the Anaconda Prompt open, type the following command:

```
conda create -m tensiletest
```

Now we need to activate our ```(tensiletest)``` virtual environment using ```conda activate```. Note that once the virtual environment is activated, we see ```(tesiletest)``` before the Anaconda prompt.

```
conda activate tensiletest
```

Now we need to install three Python packages using the Anaconda Prompt. The first is ```numpy```. We will use ```numpy``` to run some calculations on our data. The second package we need to install is ```matplotlib```. We will use ```matplotlib``` to plot the data. Both are installed with ```conda``` at the Anaconda prompt. Again, make sure you are in your ```(tensiletest)``` virtual environment:

```
(tensiletest)$ conda install numpy
(tensiletest)$ conda install matplotlib
```


The last python package we will install is ```pandas```. We will use ```pandas``` to import our ***data.csv*** file and pull out the columns we need to make the stress strain curve

```
(tensiletest)$ conda install pandas
```


To make sure that ```numpy``` and ```matplotlib``` and ```pandas``` are installed in our ```tensiletest``` virtual environemnt, type:

```
(tensiletest) $ conda list
```

The output should look something like below. Note that ```matplotlib```, ```numpy``` and ```pandas``` are all installed.

```
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

Great! Now it is time to start coding. Make a new python file using your favorite editor called ***tensiletest.py***. Make sure that the data set ***data.csv*** is in the same directory as your ***tensiletest.py*** file. At the start of the script, we need to import our three packages:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Now we need to read in our data from the ***data.csv*** data file. To do this we will use ```pd.read_csv()``` method from ```pandas``` to do this. We set ```sep=','``` because our ***data.csv*** file uses commas ```,``` to seperate columns. We use ```header=0``` to use the headers from our ***data.csv*** file as the headers in our pandas dataframe. We can also print out the data using the ```print()``` function

```python
df=pd.read_csv('data.csv', sep=',',header=0)
print(df.head())
```

Now let's see if we can run our ***tensiletest.py*** script from the conda command line. Make sure that you are still in your ```tensiletest``` virtual environment. 

```
(tensiletest) C:\Users\peter.kazarinoff\Documents\staticsite\content\code\tensiletest>python tensiletest.py
hello world
     Time (s)  Position (m)  Force (N)  Speed (mm/min)
0         0.0      0.000000          0             NaN
1         0.2      0.000000          0            0.00
2         0.4      0.000000          0            0.00
3         0.6      0.000000          0            0.00
4         0.8      0.000000          0            0.00
5         1.0      0.000000          0            0.00
6         1.2      0.000000          0            0.00
7         1.4      0.000000          0            0.00
8         1.6      0.000000          0            0.00
9         1.8      0.000000          0            0.00
10        2.0      0.000000          0            0.00
11        2.2      0.000000          0            1.71
12        2.4      0.000011          0            8.57
13        2.6      0.000057          0           16.95
14        2.8      0.000124          6           24.10
15        3.0      0.000218         19           31.62
16        3.2      0.000335         35           34.58
17        3.4      0.000448         52           30.67
18        3.6      0.000540         65           28.67
19        3.8      0.000639         66           28.29
20        4.0      0.000728         69           27.53
21        4.2      0.000823         72           28.29
22        4.4      0.000917         77           27.81
23        4.6      0.001010         82           28.38
24        4.8      0.001110         88           30.58
25        5.0      0.001210         95           29.91
26        5.2      0.001310        100           30.96
27        5.4      0.001420        102           30.96
28        5.6      0.001510        101           26.96
29        5.8      0.001600         99           28.58
..        ...           ...        ...             ...
154      30.8      0.021900        126           48.58
155      31.0      0.022100        128           60.29
156      31.2      0.022310        130           60.01
157      31.4      0.022500        130           55.53
158      31.6      0.022680        130           61.34
159      31.8      0.022910        133           64.39
160      32.0      0.023100        132           55.91
161      32.2      0.023280        132           51.15
162      32.4      0.023450         79           56.96
163      32.6      0.023660          0           52.20
164      32.8      0.023790          0           22.38
165      33.0      0.023810          0            4.95
166      33.2      0.023830          0            5.62
167      33.4      0.023850          0            5.62
168      33.6      0.023860          0            5.43
169      33.8      0.023880          0            5.33
170      34.0      0.023900          0            6.19
171      34.2      0.023920          0            7.81
172      34.4      0.023950          0            9.53
173      34.6      0.023990          0            6.57
174      34.8      0.024000          0            1.24
175      35.0      0.024000          1            0.00
176      35.2      0.024000          0            0.00
177      35.4      0.024000          0            0.00
178      35.6      0.024000          0            0.00
179      35.8      0.024000          0            0.00
180      36.0      0.024000          0            0.00
181      36.2      0.024000          0            0.00
182      36.4      0.024000          0            0.00
183      36.6      0.024000          0             NaN

[184 rows x 4 columns]

(tensiletest) C:\Users\peter.kazarinoff\Documents\staticsite\content\code\tensiletest>
```

Great! Python and pandas are able to read in our ***data.csv*** file and save it to a pandas dataframe Let's try a simple plot just using matplotlib, but just to make sure it works. In ***tensiletest.py*** file add:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',',header=None,skiprows=1)
print(df)


plt.plot(df[1], df[2])
plt.show()
```

If everything works correctly, you should see a plot that looks something like the follwoing:
![simple line plot]({filename}/images/simple_plot.png)

OK, now we need to do some manipulation. The ```df[1]``` column in our data set is the **extension** or **change in length**. The ```df[2]``` column in our data set is **force**. We need to convert the **change in length** to strain and the **force** to stress. To do this we need to define some sample parameters:

```python
# sample parameters
d = 1.778     # diameter of sample in mm
A0 = np.pi*(d/2)**2 # original cross-sectional area of sample in mm^2
L0 = 18.002   # original gauge length of sample (lenth of narrowest section)
```

Stress strain curves have **strain** on the x-axis, not **change in length**, so we need to convert our **change in length** to **strain**. The equation to use is 

$$\epsilon = \frac{\Delta L}{L_0}$$

Where $\epsilon$ is strain, $\Delta L$ is the change in length or extension, and $L_0$ is the original length. 

Stress strain curves have **stress** on the y-axis, not **force**, so we also need to convert our **force** to **stress**. The equation to use is 

$$\sigma = \frac{F}{A_0}$$

Where $\sigma$ is stress, $F$ is force and $A_0$ is the original cross-sectional area of the sample. We need to code these opperations into our ***tensiletest.py*** file. 

```python
# calculate stress and strain
stress = (force/A0)
strain = delta_L/L0
```

Now let's plot the stress-stain curve with matplotlib. We'll put strain on the x-axis and stress on the y-axis.

```python
# Plot the stress-strain curve
plt.plot(strain,stress)
plt.show()
```

If we run our ***tensiletest.py*** script, you should see the stress strain curve below:
![simple line plot]({filename}/images/stress_strain_curve1.png)

That looks pretty good. But we need to add some axis labels with units using matplotlibs ```plt.ylabel()``` and ```plt.xlabel()``` methods. Let's also add a title with the ```plt.title()``` method. Ensure these are in btween the ```plt.plot()``` and the ```plt.show()```, otherwise your title and axis labels won't show up on the plot.

```python
# plot the stress strain curve
plt.plot(strain,stress)
plt.xlabel('Strain (mm/mm)')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curve of Al6061 - T6')
plt.show()
```

You should see a plot that looks like the one below with axis labels and a title
![simple line plot]({filename}/images/stress_strain_curve2.png)

Lastly, we are going to make some changes to our axis limits. Notice how the plot doesn't start at **strain=0** or **stress=0**. We can change the axis limits using ```plt.axis([Xmin, Xmax, Ymin, Ymax])``` where ```Xmin``` and ```Xmax``` are our x-axis limits and ```Ymin``` and ```Ymax``` are our y-axis limits. We are also going to add a grid by setting ```plt.axis()``` to ```True```.

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

The final plot is shown below. The next post will detail how to calculate tensile strength, yield strength, elastic modulus and ductility from the stress strain curve. The complete ***tensiletest.py*** script is below the plot.

![simple line plot]({filename}/images/stress_strain_curve3.png)

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
