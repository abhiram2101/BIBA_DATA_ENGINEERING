num = int(input())
sum_num = 0
while num > 0 :
    n = num %  10
    num = num // 10
    sum_num = sum_num + n
print("The sum of the digits is : ", sum_num)