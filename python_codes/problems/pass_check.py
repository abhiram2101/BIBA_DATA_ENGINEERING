set_password = "abhi"
inp = input()

if set_password.casefold() == inp.casefold():
    print('Yes They are Matching')
else:
    print("Not matching")