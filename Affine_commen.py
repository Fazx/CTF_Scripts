import gmpy2
string = 'achjbnpdfherebjsw'
b=7
for i in (1,9,21,15,3,19,7,23,11,5,17,25):
	flag = ''
	for k in string:
		flag += chr(i*((ord(k)-ord('a'))-b)%26+ord('a'))
	print flag