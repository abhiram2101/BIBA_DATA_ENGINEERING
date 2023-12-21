"""
#factorial using for loop time complexity: O(n)
n  = int(input("enter number : "))
res = 1
for ele in range(1,n+1):
    res *= ele
print(res)
"""
#factorial using recursive approach

def factorial(n):
    if n == 0 :
        return 1
    elif n == 1:
        return 1
    elif n>1:
        return n*factorial(n-1)
n = int(input("enter a number: "))
print(factorial(n))
