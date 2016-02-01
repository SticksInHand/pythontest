import math
def is_odd(s):
    return s % 2 == 0

def is_empty(s):
    return s and s.strip()

def is_prime(n):
    list_num = []
    for i in range(2, n):
        for num in range(2, int(math.sqrt(n))+1):
            if i % num == 0 and i != num:
                break
            elif i % num != 0 and num == (int(math.sqrt(n))):
                list_num.append(n)
    return list_num

print is_prime(3)

m = filter(is_odd , [0,1,2,3,4,5,6,7,8,9])
n = filter(is_empty,['','nihao','hello'])
print m
print n