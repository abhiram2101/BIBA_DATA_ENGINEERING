"""
   if n in [2, 3]:
       return True
   if (n == 1) or (n % 2 == 0):
       return False
   r = 3
   while r * r <= n:
       if n % r == 0:
           return False
       r += 2
   return True
print(is_prime(78), is_prime(79))

"""

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