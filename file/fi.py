#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

d = dict(name='bob',age=10,score=90)

with open('test.txt','wb') as f:
    pickle.dump(d,f)

