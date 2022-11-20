import numpy as np

a = np.array([[1,2,3,4,5,6,7,8,9,10],[10,20,30,40,50,60,70,80,90,100]])
#print(a.shape) #confirm dimentions of array

# get specific element using [r,c]
print(a[0,5]) #6

# get a row
print(a[0,:])