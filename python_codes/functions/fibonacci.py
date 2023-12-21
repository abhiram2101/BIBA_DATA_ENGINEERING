def fibonacci():
    range_num = 10
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