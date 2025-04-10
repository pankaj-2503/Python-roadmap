# import variables as var
# var.myfunc()

import datetime as d

# Loop
for x in range(6):
    if x==3:
        pass
    else:
        print(x)
    
x=[1,2,3]
y=[5,3]
for i in x:
    for j in y:
        if i==j:
            pass
        else:
            print(i*j)


# Function
def my_function():
    print("Hello from a function")
my_function()

def my_function(fname,lname):
    print("hello from function "+fname +" "+lname)
my_function("Pankaj","Singh")


def my_function(*kids):
    print("The youngest child is "+kids[2])
my_function("Raju","Dholu","Bholu")


x= lambda a: a+10
print(x(5))

def func(n):
    return lambda a: a*n

mydoubler=func(2)
print(mydoubler(11))
print(mydoubler(23))


# Class -> class is a blueprint for creating objects which has properties(variables) and methods(functions)
# Object -> Object is an instance of a class

class MyClass:
    x=5
p1=MyClass()
print(p1.x)

# All classes have a function called __init__(), which is always executed when the class is being initiated. It is nothing but constructor
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        # return "Name is "+self.name+"and age is "+str(self.age) this is also correct
        return f"Name is {self.name} and age is {self.age}"
    def myfunc(self):
        print("Hello my name is"+self.name)

# The __str__() function controls what should be returned when the class object is represented as a string.
p1=Person("Pankaj",22)
print(p1.name)
print(p1)


# self keyword could be called anything you like, but it has to be the first parameter of any function in the class
del p1.age

# if you want class to be empty you pass keyword

# Inheritance

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

x=Person("Pankaj","Singh")
x.printname()

class Student(Person):  # student class is inherited from person class
    def __init__(self,fname,lname,year):  # this would no longer inherit parent class constructor
        super().__init__(fname,lname) # this would inherit parent class constructor also we could use Person.__init__(self,fname,lname)
        self.graduationyear=year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")


x=Student("Pankaj","Singh",2025)
print(x.graduationyear)
x.welcome()

# Iterator

mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# Polymorphism -> Polymorphism means "many forms", it refers to method/functins/operators with same name that can execute on many object or classes

# Function polymorphism eg is len() function
# Class polymorphism eg is method overriding

class Car:
   def __init__(self,brand,model):
      self.brand=brand
      self.model=model
   def move(self):
      print("Drive")

class Boat:
   def __init__(self,brand,model):
      self.brand=brand
      self.model=model
   def move(self):
      print("Sail")


car=Car("BMW","X5")
boat=Boat("Yamaha","F300")

for x in (car,boat):
   x.move()


# Scope

x = 300 # global scope

def myfunc():
  x = 200  # local scope
  print(x)

myfunc()

print(x)

# -------------------
# The nonlocal keyword makes the variable belong to the outer function. It is used in nested functions.

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


# ------------------- DATE TIME -------------------

x=d.datetime.now()
y=d.datetime(2025,2,15)
y.strftime("%c")
print(x)
print(y)

# ------------------- Math -------------------
import math
from decimal import Decimal,getcontext
x=10
y=2
print(min(x,y),max(x,y),abs(x-y),pow(x,y))

print(math.sqrt(5),math.ceil(5.5),math.floor(5.5),math.pi)

def divideWithPrecision(a,b,precision):
   getcontext().prec=precision+1
   return Decimal(a)/Decimal(b)

x=divideWithPrecision(10,3,5)
print(x)


# ------------------- JSON -------------------
# converting json from python 
import json
x='{"name":"Pankaj","age":22,"city":"Delhi"}'

y=json.loads(x)
print(y["name"])

# converting python from json
x={
   "name":"Pankaj",
   "age":22,
   "city":"Delhi"
}
y=json.dumps(x)
print(y)



