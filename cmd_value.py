import commands
import os

for i in range(1000,1300):
	cmd = 'Decode.exe -X -P %d mp3.mp3' % i
	a = os.popen(cmd)
	f = open('mp3.mp3.txt')
	content = f.read()
	if 'flag' in content or 'Flag' in content or 'FLAG' in content:
		print content
		break
	f.close()