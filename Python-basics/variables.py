#variable declaration 
# There is not multi line comment in python instead we use hash symbol for each line 

x="Hello world"
print(x)
print([1,2,3]) # list->built in data type can contain elements of different types
print(1,2,3)


y=str(4) # type casting
print(y)
print(x+y)

if y==x:
    print("y is equal to x")
else:
    print("they are not equal")


# multi-line string
"""This is example of multi line string using triple quotes"""

# variable is mutable and can be re-assigned with different data type
# variable name should not start with number,it should not have special character except underscore,they are case sensitive
# name could be used with camelCase or snake_case or PascalCase 
x=4
print(type(x))
x="Pankaj"
print(type(x))

# assign multiple value
x,y,z=1,2,3
print(x,y,z)

x=y=z="Hello"
print(x,y,z)

fruits=["apple","banana","cherry"]
x,y,z=fruits

print(x,"\n",y,"\n",z,"\n")
print(x,"\n",y,"\n",z,"\n",sep='') # sep is used to separate the values

x=4
y=6
print(x+y,x-y,x*y,x/y,x%y,x**y,x//y) # ** is used for a^b and // is used for floor division

print('Hello','World') # python print argument by default separated by space



# global variable -> we can also declare global variable like global x

x = "awesome" # variable created outside function are global by default
y = "nice"

def myfunc():
  x = "fantastic"
  global y
  y = "good"
  print("Python is " + x) # local variable

myfunc()

print("Python is " + x)
print("Python is " + y)