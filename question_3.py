import numpy as np          #importing the required python libraries
from numpy import random
x=np.array([[23, 34, 83, 17, 4],                #creates a nested 5x5 matrix
            [55, 49, 12, 37, 33],
            [85, 63, 77, 25, 91],
            [38, 46, 25, 42, 51],
            [94, 3, 54, 61, 38]], dtype=float)
y=np.max(x)           #built in function for finding maximum
z=np.min(x)         ##built in function for finding minimum
a=np.mean(x)           ##built in function for finding mean

print(x)
print("Mean is",a)
print("Maximum is",y)
print("Minimum is",z)

normal=(x-x.min()) / (x.max() - x.min())        #equation for normalizing the data entries between 0 and 1
print(normal.tolist())

flat=normal.reshape(-1)                  #reshapes the array and flattens it into a 1D array
print(flat)
print(np.sort(flat))
