import numpy as np         #imports required libraries
from numpy import random
import matplotlib.pyplot as plt
x=list(range(1,1001,1))            #forms a list in the range of 1 to 1000 (we write 1001 as it stops before the end value)
y=random.normal(size=1000)              #numpy function to generate a normal distribution of size 1000
plt.scatter(x,y)              #matplotlib code for make a scatter plot mentioning x and y axises
plt.xlabel("index of the values")                   #x label
plt.ylabel("normal distribution random values")      #y label
plt.title("scatter plot of 1000 normal distribution values")       #plot title
plt.show()                      #prints the plot
