
# ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.
# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

import numpy as np

x=np.array([1,2,3,4])
y=np.array([5,7,6,9])
z=np.add(x,y)
print(z)

# to create own ufunc
# The frompyfunc() method takes the following arguments:

# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.

def myadd(x,y):
    return x+y

myadd=np.frompyfunc(myadd,2,1)
print(myadd([1,2,3,4],[6,7,8,9]))


# simple arithmetic

arr1=np.array([2,3,4,5])
arr2=np.array([5,8,9,2])

newarr=np.add(arr1,arr2)
print("Addition: ",newarr)

newarr=np.subtract(arr1,arr2)
print("Subtraction: ",newarr)

newarr=np.multiply(arr1,arr2)
print("Multiply: ",newarr)

newarr=np.divide(arr1,arr2)
print("Divide: ",newarr)

arr=np.array([-1,2,-3,-6,8])
print(abs(arr))

newarr=np.mod(arr1,arr2)
print("Mod:",newarr)

newarr=np.divmod(arr1,arr2)
print("divison and Mod both",newarr)

# removes decimal and closest to zero by trunc and fix ,around is used to increment  preceding digit or decimal >=5 , there are function like ceil,floor
arr = np.trunc([-3.1666, 3.6667])
print(arr)
arr=np.fix([-23.0032,-2.234])
print(arr)

arr=np.around([2.55,2.4])
print(arr)

# log -> log2,loge,log10
# arr=np.arange(1,10)
# print(np.log2(arr))


from math import log
import numpy as np

nplog=np.frompyfunc(log,2,1)  # log with any base ,here log with 2 input and  1 output
print(nplog(100,15))

arr1=np.array([1,2,3])
arr2=np.array([1,2,3])

newarr=np.add(arr1,arr2)  # here it returns sum of array values at corresponding indexes
print(newarr)

nr=np.sum([arr1,arr2])  # here it returns sum of all elements
print(nr)

arr1=np.array([1,2,3])  # cumsum prints the sum as 1,1+2,1+2+3

print(np.cumsum(arr1))
print(np.prod(arr1))

x=np.prod([arr1,arr2])

print(x)

newarr=np.cumprod(arr1) # cumprod prints the prod as 1,1*2,1*2*3
print(newarr)

arr=np.diff(arr1)
print(arr)

arr=np.diff(arr1,2) # computes diff array with 2 iterations finds diff again and again
print(arr)

x=2
y=4

num=np.lcm(x,y)
print(num)

num=np.gcd(x,y)
print(num)

arr=np.array([1,3,6,21])  
x=np.lcm.reduce(arr)      # it basically gives the lowest common multiple of all 4 numbers
print(x)


x=np.gcd.reduce(arr)  # highest common factor in arr
print(x)