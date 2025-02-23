
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists


f=open("./Python-basics/input.txt","r")  # r is used for reading the file
f=open("./Python-basics/input.txt","a")  # a is used for appending the file

f.write("I am writing in this file for learning file handling in python")
f.close()

import os
if os.path.exists("./Python-basics/input.txt"):
    os.remove("./Python-basics/input.txt")
else:
    print("The file does not exist")

# To delete an entire folder, use the os.rmdir() method:


