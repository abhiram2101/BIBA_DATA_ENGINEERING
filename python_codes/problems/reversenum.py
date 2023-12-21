n = int(input())
reverse_num = 0
num = n
while n!=0 :
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n = n//10
print(reverse_num)