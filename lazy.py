def lazySum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n

        return ax
    return sum

def count():
    fs = []
    for n in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(n))

    return fs

f1,f2,f3 = count()

print f1()
print f2()
print f3()

m = lazySum(1,2,3,4,5,6)
n = m()

print m
print n