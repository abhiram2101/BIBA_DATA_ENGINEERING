#for statement

# ind = 5 
# for i in range(0,ind) :
#     print("hi")
    
# word count
strings = "abhi"
count = 0
for ch in strings:
    if ch.isalpha() == True :
        count += 1
    else :
        continue
print("total no of letters in the word are",count)