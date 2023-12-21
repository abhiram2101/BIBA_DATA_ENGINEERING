
"""

# while condition

count = 0
while count <5 :
    print(count)
    count += 1
    

#palindrome program 
    
# if the input is integer

n = int(input())
reverse_num = 0
num = n
while n!=0 :
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n = n//10
if num == reverse_num :
    print(num, " is palindrome")
else :
    print(num, "is not palindrome")    
    

    
#Display multiplication table for a given number 

n= int(input())
counter = 1
while counter<=10 :
    print(n, "*", counter, "=", n*counter)
    counter += 1


"""

# reverse an input 

n = int(input())
reverse_num = 0
num = n
while n!=0 :
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n = n//10
print(reverse_num)
