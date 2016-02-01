import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call %s()' % func.__name__
        return func(*args,**kw)
    return wrapper

def log2(text):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s call %s()'%(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return deco

def log3(text):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            if(text):
                print text
            print 'call start'
            s = func(*args,**kw)
            print 'call end'
            return s
        return wrapper
    return deco

@log3
def new():
    print '2016-01-27'
@log3('zhanglei')
def sum(j):
    return j*j


new()
print new.__name__
print sum(5)
print sum.__name__
