#if the input is string
"""
inp = input()

out = inp[::-1]

if inp == out :
    print("{} is palindrome".format(inp))
else:
    print("{} is not a palindrome".format(inp))

"""
# if the input is integer

n = int(input())
reverse_num = 0
num = n
while n>0 :
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n = n//10
if num == reverse_num :
    print(num, " is palindrome")
else :
    print(num, "is not palindrome")    
