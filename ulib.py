#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print ('status: %s %s'% (f.status,f.reason))
    for k,v in f.getheaders():
        print ('%s:%s'%(k,v))
    print ('data:%s'%data.decode('utf-8'))
    with open('douban.json','w') as n:
        n.write(data.decode('utf-8'))