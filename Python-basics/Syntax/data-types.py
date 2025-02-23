
# Built-in data types
# Text - str
# Numeric - int,float,complex
# Sequence - list,tuple,range
# Mapping - dict
# Set - set,frozenset
# Boolean - bool
# Binary - bytes,bytearray,memoryview
# None Type - NoneType

x="Pankaj"
print(type(x)) # str->built in data type

x=4
print(type(x)) # int

x=5.4
print(type(x)) # float

x=1j+3
print(type(x)) # complex

x=[1,2,"Pankaj"]
print(type(x)) # list->built in data type can contain elements of different types

x=(3,4,"Pankaj") # tuple->built in data type can contain elements of different types
print(type(x))

x=range(7)
print(x)
print(type(x))

x={"name":"Pankaj","age":21} # dict
print(type(x))

x={"apple","banana","cherry"}
print(type(x)) # set

x=frozenset({"apple","banana","cherry"})
print(type(x)) # frozenset

x=True
print(type(x)) # bool

x=b"Hello" 
print(x)
print(type(x)) # bytes

x=bytearray(5)
print(x) # bytearray

x=memoryview(bytes(5))
print(x)    # memoryview

x=None
print(type(x)) # NoneType

# int has unlimited length
# complex cannot be casted to another number

z=1+5j
# y=int(z) -> produces error
# print(y) -> produces error

import random
print(random.randrange(0,5))


print("It is all right")
print("Using double 'quotes' in single 'quotes'")
print('Using single "quotes" in double "quotes"')

a="Hello, world"
print(a[4],a[5],a[6],a[7],sep='')
print(a[7:12])

print(a[:5])   # used to print character from character to i-1
print(a[4:])   # used to print character from i to end of string
print(a[-10:]) # used to reverse order from -i to end of string
print(a[-10:-5]) # used to print character from -i to -j-1

a="Ryan Gosling"
print(len(a))
print('Ryan' in a)
print('Jack' not in a) 
for x in a:
    print(x,end='') # end is used to print on same line
print()

a=" Hello "
print(a.upper())
print(a.lower())

a=a.strip() # removes white spaces from start and end
print(a) 

a=a.replace('He','She') # replaces string with another string
print(a)

b="Panwan-Ganga-International"
print(b.split('-'))

c=a+" "+b
print(c)

text=f"This is text formatting {b}" # f-string   -> used to format string
print(text)

text=f"The price is {20*5}"
print(text)

price=21
text=f"The price is {price:.2f} dollars" # .2f is used to print 2 decimal places
print(text)

text="We are called \"Viking\" from the north" # escape character is used to for double quotes under double quotes
print(text)


# String methods
a="hello, world"
print(a.capitalize())   # capitalize the first character of string
print(a.find('o'))      # find the index of first occurence of character
print(a.count('o')) # count the number of times a character appears in string
print(a.center(20)) # center the string with total length of i here it is 20



# capitalize()	 -> Converts the first character to upper case
# casefold()     ->	Converts string into lower case
# center()	     -> Returns a centered string
# count()        ->	Returns the number of times a specified value occurs in a string
# encode()       ->	Returns an encoded version of the string
# endswith()     ->	Returns true if the string ends with the specified value
# expandtabs()   ->	Sets the tab size of the string
# find()         ->	Searches the string for a specified value and returns the position of where it was found
# format()       ->	Formats specified values in a string
# format_map()  ->	Formats specified values in a string
# index()	   -> Searches the string for a specified value and returns the position of where it was found
# isalnum()    ->	Returns True if all characters in the string are alphanumeric
# isalpha()    ->	Returns True if all characters in the string are in the alphabet
# isascii()    ->	Returns True if all characters in the string are ascii characters
# isdecimal()  ->	Returns True if all characters in the string are decimals
# isdigit()    ->	Returns True if all characters in the string are digits
# isidentifier() ->	Returns True if the string is an identifier
# islower()    ->	Returns True if all characters in the string are lower case
# isnumeric()  ->	Returns True if all characters in the string are numeric
# isprintable() ->	Returns True if all characters in the string are printable
# isspace()  ->	Returns True if all characters in the string are whitespaces
# istitle()  ->	Returns True if the string follows the rules of a title
# isupper()  ->	Returns True if all characters in the string are upper case
# join()    ->	Joins the elements of an iterable to the end of the string
# ljust()   ->	Returns a left justified version of the string
# lower()  ->	Converts a string into lower case
# lstrip()  ->	Returns a left trim version of the string
# maketrans() ->	Returns a translation table to be used in translations
# partition() ->	Returns a tuple where the string is parted into three parts
# replace()	-> Returns a string where a specified value is replaced with a specified value
# rfind()  ->	Searches the string for a specified value and returns the last position of where it was found
# rindex() ->	Searches the string for a specified value and returns the last position of where it was found
# rjust()  ->	Returns a right justified version of the string
# rpartition()	-> Returns a tuple where the string is parted into three parts
# rsplit() ->	Splits the string at the specified separator, and returns a list
# rstrip() ->	Returns a right trim version of the string
# split() ->	Splits the string at the specified separator, and returns a list
# splitlines() ->	Splits the string at line breaks and returns a list
# startswith() ->	Returns true if the string starts with the specified value
# strip() ->	Returns a trimmed version of the string
# swapcase() ->	Swaps cases, lower case becomes upper case and vice versa
# title() ->	Converts the first character of each word to upper case
# translate() ->	Returns a translated string
# upper()	-> Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning


# List
# List is a collection which is ordered and changeable. Allows duplicate members.
# List is defined by using square brackets
mylist=['apple','banana',4]
print(mylist)
print(mylist[2])
print("the length of list is:",len(mylist))
mylist[1]='cherry'
print(mylist)
print(mylist[-2:])
print(mylist[1:2])

if 'banana' in mylist:
    print("Yes, it is present")
else:
    print("It is not there")

mylist[0:2]=['orange','mango']
print(mylist)

mylist.append("kiwi")
mylist.insert(1,"papaya")
print(mylist)

list1=['apple','banana','cherry']
list2=['orange','mango','banana']
list1.extend(list2)
print(list1)

list1.remove('banana')
list1.pop(2)
print(list1)
del list1[0]
list1.clear()  # clear empties the content of list not the structure of list
del list1 # delete the list completely

for i in range(len(list2)):
    print(list2[i],end=' ')


print()

i=0
while i<len(list2):
    print(list2[i],end=' ')
    i+=1            # in python ++ / -- operator doesn't exist

print()

list3=[x for x in list2 if x=='mango']
print(list3)

list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)

def myfun(n):
    return abs(10-n)

list4=[1,2,3,4,5]
list4.sort(key=myfun)  # used for custom sort
print(list4)


# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# Tuple 
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# We cannot add or remove elements from tuple

mytuple=('apple','banana','cherry')
# mytuple[0]='orange'  -> produces error as tuple is not mutable
print(mytuple[0])

tuple1=tuple(('raj','mira','poonam'))
print(tuple1)
# tuple1.append('veer') -> error as immutable
print(tuple1)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(green,*tropic,red)=fruits # * is used to assign the rest of the values to the variable
print(green)
print(tropic)
print(red)

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


# Set 
# Set is a collection which is unordered and unindexed. No duplicate members.They are unchangeable but we can add or remove elements

myset={'apple','banana','cherry'}
print(myset)

# in set True and 1,False and 0 are considered same to they are not allowed to have in set
# myset={1,2,3,4,True,False} -> error

myset.add('orange') # add() is used to add element in set
print(myset)

thisset=set(('apple','banana','cherry'))  # set constructor
tropical={'mango','pineapple','papaya'}
thisset.update(tropical)  # update() is used to add multiple elements in set
print(thisset)

thisset.remove('banana') # remove() is used to remove element from set if element is not present it will produce error
thisset.discard('apple') # discard() is used to remove element from set if element is not present it will not produce error
print(thisset)

myset.clear() # clear() is used to empty the set
print(myset)

for x in thisset:
    print(x,end=' ')


# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1={1,2,3,4}
set2={3,4,5,6}
set3=set1.union(set2) # we can also use | operator to join two sets , union method allow to join set with other data types like list,tuple
print(set3)
print(set1.intersection(set2)) # we can also use & operator to find intersection of two sets and not with other data types
print(set1.difference(set2)) # we can also use - operator to find difference of two sets and not with other data types
print(set1.symmetric_difference(set2)) # we can also use ^ operator to find symmetric difference of two sets and not with other data types

# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not


# Dictionary -> key value pair, unordered, changeable and indexed , no duplicate keys

mydict={
    "name":"Pankaj",
    "age":21,
    "city":"Delhi"
}

x=mydict['name']
y=mydict.get('age')
z=mydict.keys()
print(x,y,end=' ')
print(z)

mydict['age']=22
x=mydict.values()
print(x)

y=mydict.items() # items method returns key value pair in list of tuples
print(y)
mydict.update({"city":"Mumbai"})
print(mydict)

# The pop() method removes the item with the specified key name, The popitem() method removes the last inserted item 
# The del keyword removes the item with the specified key name, The clear() method empties the dictionary

for x, y in mydict.items():
  print(x, y)

dict=mydict.copy()
print(dict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}  # nested dictionary