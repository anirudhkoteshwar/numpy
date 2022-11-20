import numpy as np

a = np.array([1,2,3]) 
#print(a)
b = np.array([[1.1,2.2,3.3],[4.4,5.5,6.6]])
#print(b)
c = np.array([1,2,3,4,5], dtype='int16') #set specific type of array

#get dimentions of an array
print(a.ndim)
print(a.shape)
print(b.ndim)
print(b.shape)

#get type of array
print(a.dtype)
print(b.dtype)
print(c.dtype)
#get size of an array
