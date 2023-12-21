def pri() :
    l1 = [1,2,4,6,8,7,15,9,10,3,4,5]
    l = l1[0]
    h = l1[len(l1) - 1]

    while l < h:
        if l > h :
            l,h = h,l
            l += 1
            h -= 1
        else:
            l += 1
            h -= 1
    return l1,h,l
print(pri())
        
