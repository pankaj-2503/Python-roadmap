# Pandas in python library used for data cleaning
# Pandas is a Python library used for working with data sets.
# It has functions for analyzing, cleaning, exploring, and manipulating data.


# loading csv file into dataframe

import pandas as pd
print(pd.options.display.max_rows)  # You can check your system's maximum rows with the pd.options.display.max_rows statement.

df=pd.read_csv('./python-basics/pandas/data.csv')
# df = pd.read_json('data.json')  # used to read json file which is key value pair

print(df.info())   # gives more info about the file/data , it also return no. of missing values in table
print(df.to_string())
print("Next line")
print(df.head(5))   # returns header with specified no. of rows ,similarly tail return from bottom
print(df.tail(3))


mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar=pd.DataFrame(mydataset)  # it creates table with rows and columns
print(myvar)


# Series is like column in a table , it is one dimensional array holding data of any type
a=[1,2,3]
x=pd.Series(a)
print(x)

print(a[0])

y=pd.Series(a,index=["x","y","z"])  # assigning labels to index of array a
print(y["y"])


# key values objects as series
calories={"day1":420,"day2":300,"day3":550}
z=pd.Series(calories)
print(z)

z=pd.Series(calories,index=["day1","day2","day3"])
print(z)


# Dataframe are multidimensional table
data={
  "calories":[42,34,230],
  "duration":[50,40,32]
}
x=pd.DataFrame(data)
print(x)

print(x.loc[0])     # print row 0
print(x.loc[[0,1]]) # print row 0 and 1 by passing list of indexes , iloc is also used to locate element based on index only
print(x.iloc[1])

y=pd.DataFrame(data,index=["Row1","Row2","Row3"])  # marking indexes of rows and row1,row2 etc.
print(y)



# Data Cleaning -> data could be empty,duplicates,wrong format,wrong data

# one way to deal with empty values is remove row,replace empty values with may mean,median or mode,

df=pd.read_csv('./python-basics/pandas/data.csv')
newdf=df.dropna() # this method returns new dataframe and will not change origianl one , if we want to change the origianl one we use inplace=True inside this method
print(newdf.to_string())  # in our data.csv we have last row empty it has dropped it now


df.fillna(130,inplace=True)  # fill missing values with specified no.
x=df["Calories"].mean() # or we also could do median() or mode()[0]
print(x)
df["Calories"].fillna(x,inplace=True) # this method fills specific col missing value , 
print(df.to_string())




# to deal with wrong format

df['Maxpulse']=pd.to_numeric(df['Maxpulse'],errors='coerce') # Invalid parsing will be set as NaN
# errors='ignore': Invalid parsing will return the original input.
# errors='raise': If parsing fails, an exception will be raised.
print(df)

df.dropna(subset=['Maxpulse'],inplace=True)  # drops the null values

print(df.to_string())


# how to deal with wrong data
df.loc[7, 'Duration'] = 45  # directly put values

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)



# how to deal with duplicates
print(df.duplicated())  # checks if duplicates or not
df.drop_duplicates(inplace=True)
print(df)

# correlation
print(df.corr())  # it basically find it 2 columns have relationship or not it varies bw -1 to 1


# Plotting
import matplotlib.pyplot as plt
# df.plot()
# plt.show()

df.plot(kind='scatter',x='Duration',y='Calories')  # here we could use 'hist' for historgram
plt.show()