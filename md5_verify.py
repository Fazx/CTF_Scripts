#-*-coding:utf-8-*-
import hashlib

flag = "b66b9d"

def MD5(data):
	return hashlib.md5(data).hexdigest()


for i in range(1000000):
	st = str(i)
	md5 = MD5(st)
	if(md5[-6:] == flag):
		print(st, md5)
		break
