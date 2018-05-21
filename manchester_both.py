#-*- coding: utf-8 -*-
#!/usr/bin/python
#曼彻斯特和查分曼彻斯特解码
import os
import sys
from Crypto.Util.number import *

def mcdecode(hexstr):
    s = ''
    for i in xrange(len(hexstr) / 2):
        ch = hexstr[i * 2: i * 2 + 2]
        b = bin(int(ch, 16))[2:]
        b = '0' * (8 - len(b)) + b
        s += b
    r = ''
    print 's--> ' + s
    print len(s)

    for i in xrange(len(s)/2):
        c = s[i * 2: i * 2 + 2]
        if c == '01':
            r += '1'
        else:
            r += '0'

    print 'r--> ' + r
    ret = ''
    for i in xrange(len(r) / 8):
        c = r[i * 8: i * 8 + 8][::-1]
        ret += hex(int(c, 2 ))[2:].upper()
    print ret


def cfmcdecode(hexstr):
	s = bin(hexstr)[6:]
	#print s
	r=""
	tmp = 0
	for i in xrange(len(s)/2):
		c = s[i*2]
		if c == s[i*2 - 1]:
			r += '1'
		else:
			r += '0'
	print hex(int(r,2)).upper()

if __name__ == "__main__":
    cfmcdecode(0x3EAAAAA56A69AA556A965A5999596AA95656)
    cfmcdecode(0x3EAAAAA56A69AA55A95995A569AA95565556)
    mcdecode("5555555595555A65556AA696AA6666666955")

