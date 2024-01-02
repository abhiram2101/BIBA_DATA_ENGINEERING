"""
# using modules 

import math
from math import *

print("square root is :",math.sqrt(25)) 

math_pi = round((math.pi),2)

print("pi value is ",math_pi) 

print("sin angle is: ",math.sin(2))

print("cos angle is: ",math.cos(1))

print("tan value is : ",math.tan(0.23)) 

print("factorial is: ",math.factorial(5))



# renaming a module

import math as m 

print(m.sqrt(81))




# hands on pandas module

import pandas as pd



marks_data = {
  "subjects": ["maths","science","social"],
  "marks": [50, 40, 45]
}

myvar = pd.DataFrame(marks_data)

print(myvar)



import pandas as pd

data = pd.read_csv("Marks_data.csv")
print(data)




#reading column names

print(data.columns,"\n")

name_col = data.Name
print("data in column are: \n",name_col)



# handas on numpy module.

import numpy as np



lis1 = [1,2,3,4]

array = np.array(lis1)

print(array)
print(array[0:3])



# generating the arrays of zeros
import numpy as np

zero_array = np.zeros((3,6))
print("The zero array is: \n",zero_array,"\n")



import numpy as np

one_array = np.ones((2,3))
print("The ones array is: \n",one_array,"\n")



import numpy as np

range_Array = np.arange(0,100,15)

print(range_Array)



import numpy as np

line_array = np.linspace(0,10,15)
print(line_array)





import numpy as np

lis3 = [[1,2,3,],[4,5,6]]
array3 = np.array(lis3)
print("2D array : \n",array3)

print(type(array3))
print(array3.flatten())
print(array3.ndim)
print(array3.shape)
print(array3.dtype)
print(array3.size)

"""

# importing modules

import operations as op

print(op.add(5,8))
print(op.sub(10,8))
print(op.mul(5,2))





