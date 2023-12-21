"""
# read : it returns all the data from the file 

f = open("file.txt","r")
print(f.read())



# readline() : It returns single line from the file

f = open("file.txt","r")
print(f.readline())





# writing into file

f = open("file.txt","a")
f.write(" We are still training")
f.close()

f = open("file.txt","r")
print(f.read())



# using create and write 
f = open("file2.txt","x")
f.write("This is file 2")
f.close()

f = open("file2.txt","r")
print(f.read())



f = open("file.txt","r")
for ele in f:
    print(ele)
    
"""
import os
if os.path.exists("file.txt") :
    print("yes available")
else:
    print("not availbale")