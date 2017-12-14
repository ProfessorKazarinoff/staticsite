### Script calculates probability as area under a normal gaussian curve,
### given inputs of x1, x2, mu (mean), sigma(std. dev.) and computes
### the probabability using the integral function and the gaussian curve.
from math import sqrt,erf
## If plotting as well
#import matplotlib.pyplot as plt
#import numpy as np
### *** Change the following inputs *** ###
mu= 979.8 # mean of the sample
sigma= 73.1 # standard deviation of the sample
x1= 900 # lower x, use -float('inf') for negative infinity
x2= 1100 # upper x, use float('inf') for infinity
############################################

# Probability from 0 to upper
double_prob = erf( (x1-mu) / (sigma*sqrt(2)) )
Plower = double_prob/2
#print('\n' + str(Plower))
# Probability from lower to 0
double_prob = erf( (x2-mu) / (sigma*sqrt(2)) )
Pupper = double_prob/2
#print('\n'+ str(Pupper))

Pin=Pupper-Plower
print('\n')
print('mean = %.2f    std dev = %.2f \n' % (mu,sigma))
print('Calculating probability of occuring between %.4f <--> %.4f \n' % (x1,x2))
print('inside interval Pin = %.2f%% \n' % (Pin*100))
print('outside interval Pout = %.2f%% \n' % ((1-Pin)*100))
print('\n')