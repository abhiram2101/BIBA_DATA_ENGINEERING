year = int(input())
if year % 400 == 0 :
    if year % 100 == 0 :
        print(year,"is leap year")
    else :
        print(year,"is not a leap year")
elif year % 4 == 0 :
    print(year,"is leap year")
else : 
    print(year,"is not a leap year")
    
