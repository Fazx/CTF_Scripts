	#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: nothing -*-

a = 'szzyfimhyzd'
a1=[]
for i in a:
    a2 = ord(i)-97
    a1.append(a2)
print a1
aa = ''
for i in a1:
    for j in range(0,26):
        c = (17*j-8)%26  #仿射加密公式，自行更改
        if(c==i):
            aa+=chr(j+97)
print aa

    
