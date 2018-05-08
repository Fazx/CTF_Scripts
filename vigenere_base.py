#encoding=utf-8
str0 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str1 = raw_input("Please input secret key:")#密钥
str2 = raw_input("Please input the cryptograph:")#密文
str2 = str2.upper()
i = 0
str = ''
while i<len(str2):#分块
	str3 = str2[i:i+len(str1)]
	k = 0
	for j in str3:
		str += str0[ord(j)-ord(str1[k])]
		k += 1
	i += len(str1)
print str1