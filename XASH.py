from pwn import *
import hashlib

conn = remote('106.75.73.28',20000)
conn.recvuntil('such that ')
cm = conn.recvuntil('(')[:-1]
conn.recvuntil(' = ')
cnum = conn.recvline()[:-1]

print cm
print cnum

co = ''

if cm == 'md5':
    print '======MD5 Bruteforcing======'
    for i in range(100000, 9999999):
        if (hashlib.md5(str(i)).hexdigest())[-6:] == cnum:
            print str(i)
            co = str(i)
            break

if cm == 'sha1':
    print '======SHA1 Bruteforcing======'
    for i in range(100000, 9999999):
        if (hashlib.sha1(str(i)).hexdigest())[-6:] == cnum:
            print str(i)
            co = str(i)
            break

if cm == 'sha224':
    print '======SHA224 Bruteforcing======'
    for i in range(100000, 9999999):
        if (hashlib.sha224(str(i)).hexdigest())[-6:] == cnum:
            print str(i)
            co = str(i)
            break

if cm == 'sha256':
    print '======SHA256 Bruteforcing======'
    for i in range(100000, 99999999):
        if (hashlib.sha256(str(i)).hexdigest())[-6:] == cnum:
            print str(i)
            co = str(i)
            break

if cm == 'sha384':
    print '======SHA384 Bruteforcing======'
    for i in range(100000, 99999999):
        if (hashlib.sha384(str(i)).hexdigest())[-6:] == cnum:
            print str(i)
            co = str(i)
            break

if cm == 'sha512':
    print '======SHA512 Bruteforcing======'
    for i in range(100000, 99999999):
        if (hashlib.sha512(str(i)).hexdigest())[-6:] == cnum:
            print str(i)
            co = str(i)
            break

conn.send(co + '\n')


menu = conn.recv()

print menu

conn.send('I' + '\n')

conn.recvuntil(' = ')

sha1key = conn.recv()[:-1]

print 'sha1key: ' + sha1key

str1 = 'aaaaaaaaaaaaaaaa'
str2 = 'bbbbbbbbbbbbbbbb'

conn.send('G' + '\n')
conn.send(str1 + '\n')
conn.recvuntil(' = ')
xash1 = conn.recv()[:-1]
conn.send('G' + '\n')
conn.send(str2 + '\n')
conn.recvuntil(' = ')
xash2 = conn.recv()[:-1]
print 'xash of str1: ' + xash1
print 'xash of str2: ' + xash2
xxash1 = xash1.decode('hex')
xxash2 = xash2.decode('hex')
xkey = ''

for i in range(16):
	for c in range(256):
		if (ord(xxash1[i]) == ord('a') ^ c) and (ord(xxash2[i]) == ord('b') ^ c):
			xkey += chr(c)
			break

print 'hex(xkey): ' + xkey
print 'sha1 of calc-xkey: ' + hashlib.sha1(xkey).hexdigest()
str1 = b'\x00'*15 + hashlib.md5(xkey).digest()[:1]
str2 = b'\x00'*15

print str1
print str2

conn.send('G' + '\n')
conn.send(str1 + '\n')
conn.recvuntil(' = ')
xash1 = conn.recv()[:-1]
conn.send('G' + '\n')
conn.send(str2 + '\n')
conn.recvuntil(' = ')
xash2 = conn.recv()[:-1]

print 'xash of str1: ' + xash1
print 'xash of str2: ' + xash2

conn.send('S' + '\n')
conn.send(str1.encode('hex') + ',' + str2.encode('hex') + '\n')
print conn.recv()
print conn.recv()


'''
def xash(data, xkey):
	assert len(xkey) == 16
	if len(data) < len(xkey):
		data += md5(xkey).digest()[:len(xkey) - len(data)]
	out = b''
	for n in range(len(data)):
		out += chr( ord(data[n]) ^ ord(xkey[n]) )
	return out.encode('hex')
'''