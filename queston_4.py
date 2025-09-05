import numpy as np
x=np.array([[23, 34, 83, 17, 4],          #forms a nested 5x5 array
            [55, 49, 12, 37, 33],
            [85, 63, 77, 25, 91],
            [38, 46, 25, 42, 51],
            [94, 3, 54, 61, 38]])
print(x[1:4, 1:4])          #slices the array and gives us the central 3x3 array
y=x[0,:]                       #slices the array to give us the first row
z=x[:,4]                   #slices the array to give us the last column
print(y)
print(z)
print(np.dot(y,z))          #built in function for finding dot product of two 1D arrays
