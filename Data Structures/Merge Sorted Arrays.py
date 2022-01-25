def merge(a,b):
    if len(a)==0 or len(b)==0:
        return a+b
    new_arr = []
    fidx, sidx = 0,0

    while fidx < len(a) and sidx < len(b):
        if a[fidx] <= b[sidx]:
            new_arr.append(a[fidx])
            fidx += 1
        else:
            new_arr.append(b[sidx])
            sidx += 1

    return new_arr+a[fidx:]+b[sidx:]

a = [1,3,5,7,10]
b = [2,4,6,8,10,12]
print(merge(a,b))

    




