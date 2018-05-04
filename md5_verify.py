#-*-coding:utf-8-*-
import hashlib

flag = "5273e2"

def MD5(data):
	return hashlib.md5(data).hexdigest()


for i in range(1000000):
	st = str(i)
	md5 = MD5(st)
	if(md5[0:6] == flag):
		print(st, md5)
		break
