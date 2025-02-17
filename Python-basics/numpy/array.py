# NumPy stands for numerical python and it is the core library for numeric and scientific computing in Python.
# It provides high-performance multidimensional array object and tools for working with these arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# It makes working with arrays faster than lists bcz of use of continuous memory locations 

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

print(np.__version__)

print(type(arr))

a=np.array(4)
b=np.array([1,2,4,5])
c=np.array([[1,2,3],[4,5,2]])
print(a.ndim)
print(b.ndim)
print(c.ndim)

arr1=np.array([1,2,3,4],ndmin=5)  # ndmin is used to define the dimension of the array , it would give output like [[[[[1 2 3 4]]]]]
print(arr1)

print(arr[0]+arr[1])

arr=np.array([[1,2,3,4],[5,6,7,8]])
print('First row 4th element is',arr[0,3])
print('second row 3rd element is',arr[1,2])

# accessing 3rd element of 2nd row of 1st matrix
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

print(arr[1,-1]) # last element of last row of 2nd matrix


arr=np.array([1,2,3,4,5,6,7,8,9,10])

print(arr[0:5:2]) # start from 0st index and go till 5th index with step of 2

print(arr[5:])
print(arr[:7])
print(arr[-3:-1])
print(arr[::2]) # start from 0th index and go till end with step of 2

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4]) # 1st row and 1 to 4th column

print(arr[0:2,2]) # from both elements return index 2
print(arr[0:2, 1:4])  # from both rows of array select col 1 to 4 

# data types in python
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

arr=np.array([1,2,3],dtype='f')  # if we use decimal values in array then we get float64 as default while in this case we are getting float32
print(arr[0].dtype)

newarr=arr.astype('f')
print(newarr)

x=arr.copy()
print(x)


# view vs copy , changes made to original array will reflect in view but not in copy
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
y = arr.copy()
arr[0] = 42

print(arr)
print(x)
print(y)

# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.

print(x.base)
print(y.base)


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)  # shape return the shape of array basically the number of elements in each dimension

newarr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(newarr.reshape(4,3))  # converting 1d array to 2d array

print(newarr.reshape(6,2))  # converting 1d array to 2d array

# reshape to 3d array
print(newarr.reshape(2,3,2))

print( newarr.reshape(2, 2, -1)) # -1 is used to automatically calculate the dimension, we cannot use -1 for more than 1 dimension

# flattening the array
newarr.reshape(-1)
print(newarr)


arr = np.array([[1, 2, 3], [4, 5, 6]])
# it will print whole array seperated by new line based on their dimension
for x in arr:
  print(x)


# iterating 3d array
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in arr:
    print("x is 2d array")
    print(x)

# nditer() is function to iterate through n-dimensional arrays
for x in np.nditer(arr):
    print(x)





arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:,::2]):   # it is used the iterate through the array with step of 2
    print(x)

for idx, x in np.ndenumerate(arr): # ndenumerate() is used to iterate through n-dimensional arrays
  print(idx, x)   # it will print the index of each element in array along with the element


arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr3=np.concat((arr1,arr2))
print(arr3)
arr4=np.vstack((arr1,arr2)) # to stack along columns
print(arr4)
arr5=np.stack((arr1,arr2),axis=1) # to stack along axis
print(arr5)

arr3=np.hstack((arr1,arr2))  # to stack along row
print(arr3)

arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr)
newarr=np.array_split(arr,4) # if elements are not enough for split it would adjust automatically
print(newarr)


arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3) # splits array column wise

print(newarr)


# search
arr=np.array([1,2,4,3,4,5,4])
x=np.where(arr==4)
print(x)     

# find where index are even
x=np.where(arr%2==0)
print(x)

x=np.searchsorted(arr,3,side='left')  # it performs binary search and return index if element is present if not present returns size of array,from left side or right
print(x)

# find index where these values to be inserted
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)


# sort array
arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

# filter array

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]
newarr = arr[x]  # based on true values it return elements from arr
print(newarr)


filter_arr=arr>42
newarr=arr[filter_arr]
print(newarr)
print(filter_arr)


arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = arr%2==0
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)


