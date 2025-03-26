# plottask.py
# Week 8 task
# Write a program called plottask.py that on the one set of axes displays: (Some marks will be given for making the plot look nice (legend etc).Please put a copy of the image of the plot (.png file) into the repository)
    # a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
    # and a plot of the function  h(x)=x3 in the range 0 to 10, 
# author: Kyra Menai Hamilton

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# First create the values for the normal distribution. Requirements are 1000 values, mean of 5 and standard deviation of 2.
mean = 5
std_dev = 2
rdm_values = np.random.normal(mean, std_dev, 1000)

# The initial values had a LOT of decimal places, so I used the round() function to round the values to 2 decimal places.
values = np.round(rdm_values, 2)

# Check that is works by printing the values as a list [].
# print(values)

# Now to plot the histogram of the normal distribution. Making sure to include labelling and legends.add_subplot(111) is used to create a single plot.

plt.hist(values, bins=30, color='c', edgecolor='black', alpha=0.7, label='Normal Distribution Values')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of a Normal Distribution of 1000 random values \n(Mean = 5, Standard Deviation = 2)')
plt.legend()
plt.show()

# Plot output showin in: week8task_figure_1_normaldis1000.png for histogram of normal distribution of 1000 values.

# Now to plot the function h(x)=x^3 in the range 0 to 10.
# Create the range of values from 0 to 10.
x = np.linspace(0, 10, 100)
y = x**3

# Plot the function h(x)=x^3 in the range 0 to 10.
plt.plot(x, y, color='m', label='h(x)=x^3')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.title('Plot of the function h(x)=x^3 in the range 0 to 10.')
plt.legend()
plt.show()

# References:
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# https://numpy.org/doc/stable/reference/generated/numpy.round_.html
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# https://matplotlib.org/stable/tutorials/colors/colors.html
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html

# END