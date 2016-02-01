def cmp(x,y):
    if x>y:
        return -1
    elif x<y:
        return 1
    else:
        return 0
m = sorted([3,4,9,4,11,5,788,2],cmp)
print m