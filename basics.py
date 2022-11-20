import numpy as np

a = np.array([1,2,3]) 
#print(a)
b = np.array([[1.1,2.2,3.3],[4.4,5.5,6.6]])
#print(b)
c = np.array([1,2,3,4,5], dtype='int16') #set datatype of array

#get dimentions of an array
print(a.ndim)
print(a.shape)
print(b.ndim)
print(b.shape)

#get type of array
print(a.dtype)
print(b.dtype)
print(c.dtype)

#get size of each element in an array
print(a.itemsize) #int is 8 bytes
print(b.itemsize) #float is 8 bytes
print(c.itemsize) #short is 2 bytes

#get total size of array
#one method is to multiply itemsize with number of items
print(a.nbytes) 
print(b.nbytes) 
print(c.nbytes) 


