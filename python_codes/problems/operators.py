
"""

a = int(input())
b = int(input())

#arithmetic operators *

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)






#comparision operators
a = 10
b = 5
c = 20
d = 6
e = 15
f = 30

print(a == b)
print(c!=d)
print(e<b)
print(f>b )
print(d<=b)
print(a>=e)



#logical operators


x = 20
y = 15
print(x < 0 and y < 0)
print(x < 0 or y > 0)
print(not(x > 3 and x < 10))


# membership operators

l1 = ["a", "b", "c", "d"]
a = "b"
c = "z"
if a in l1:
    print(a, "is present in the list")
if c not in l1:
    print(c, " is not in the list" )
    
"""

# bitwise operators

print(5 & 7)
print(2 | 9)
print( 3 ^ 6)
print(8 >> 2)
print(3 << 2)