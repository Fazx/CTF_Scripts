#-*-coding:utf-8-*-
import base64
file = open('flagencode.txt','r')
st = file.read()
while True:
	try:
		st = base64.b16decode(st)
	except:
		try:
			st = base64.b32decode(st)
		except:
			st = base64.b64decode(st)
	if(st.find("flag") == 0):
		break
print(st)