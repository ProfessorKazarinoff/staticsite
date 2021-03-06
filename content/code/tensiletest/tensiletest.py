# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:39:04 2017

@author: peter.kazarinoff
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',',header=None,skiprows=1)
#print(df)


#plt.plot(df[1], df[2])
#plt.show()

delta_L = np.array(df[1])*1000  #delta_L in 2nd column of csv
#print(delta_L)
force = np.array(df[2])  #force in 3rd column of csv
#print(force)

# sample parameters
d = 1.778     # diameter of sample in mm
A0 = np.pi*(d/2)**2 # original cross-sectional area of sample in mm^2
L0 = 18.002   # original gauge length of sample (lenth of narrowest section)

# calcuate stress and strain
stress = (force/A0)
strain = delta_L/L0

# calculate the tensile strength (TS)
TS = max(stress) # Tensile Strength (TS)
TS = round(TS,1) # round to 3 sig figs
print('TS =', TS, 'MPa')

# plot the stress strain curve
plt.plot(strain,stress)
plt.xlabel('Strain (mm/mm)')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curve of Al6061 - T6')
plt.axis([0, 1.4, 0, 60])
plt.grid(True)
textstr = r'$TS=%.1f \ MPa$'%(TS)
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
plt.text(1.0, 20, textstr, fontsize=14, bbox=bbox_props)

# this is the inset axes over the main axes
a = plt.axes([0.2, 0.2, .3, .3], facecolor='w')
plt.plot(strain, stress)
plt.title('Inset of Elastic Region')
plt.xlim(0, 0.05)
plt.ylim(0, 40)

#elastic_stress = stress[stress.any(stress<26.2 and stress>0.01)]
elastic
print(elastic_stress)


plt.show()
 


