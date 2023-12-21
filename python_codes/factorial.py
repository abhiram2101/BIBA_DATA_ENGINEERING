"""
#factorial using for loop time complexity: O(n)
n  = int(input("enter number : "))
res = 1
for ele in range(1,n+1):
    res *= ele
print(res)

#factorial using recursive approach

def recursive(n):
    if n == 0 :
        return 1
    elif n == 1:
        return 1
    elif n>1:
        return n*recursive(n-1)
n = int(input("enter a number: "))
print(recursive(n))


#prime number program

n = int(input("enter a num:"))

def isprime(n):
    flag = False
    if n == 1:
        return "{} is neither prime nor composite".format(n)
    elif n == 2 :
        return "{} is a prime ".format(n)    
    elif n>2:
        if n % 2 == 0 :
            flag = True
        else:
            flag = False
    if flag == False:
        return "{} num is prime".format(n)
    else:
        return "{} num is not prime".format(n)

    
print(isprime(n))




# even or odd

n = int(input("enter a number: "))

def isevenodd(n):
    if n % 2 == 0 :
        return "{} is even".format(n)
    else:
        return "{} is odd".format(n)
print(isevenodd(n))




# fibonacci 


def fibonacci():
    range_num = int(input("enter range : "))
    num1 = 0
    num2 = 1
    print(num1,end=" ")
    print(num2,end=" ")
    for i in range(2,range_num) :
        res = num1 + num2
        num1 = num2
        num2 = res
        print(res,end=" ")
    print()
fibonacci()




# largest among three

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c :
    print(a)
elif b > a and b>c :
    print(b)
else:
    print(c)
    

"""

# list sorting

lis = [1,5,8,7,9,12,2,24,56,100,3,11]

lis2 = sorted(lis)
print(lis2)

