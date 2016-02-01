import functools

print int('1000000' , base=2)

int2 = functools.partial(int,base=2)

print int2('1010101')