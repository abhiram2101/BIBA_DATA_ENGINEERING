# reading entire file
import pandas as pd

# data = pd.read_csv("Salary_Data.csv")
# print(data)

# # reading column names

# #print(data.columns)

# salary_col = data.Salary
# print(salary_col)



# import pandas as pd 

# # Creating Dictionary 
# dict = { 
#     'series': ['Friends', 'Money Heist', 'Marvel'], 
#     'episodes': [200, 50, 45], 
#     'actors': [' David Crane', 'Alvaro', 'Stan Lee'] 
# } 

# # Creating Dataframe 
# df = pd.DataFrame(dict) 
# print(df)

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
print(myvar.loc[1]) # loc will find and return the specified row from the data frame
 
myvar = pd.DataFrame(data,index = ['a','b','c'])

print(myvar)