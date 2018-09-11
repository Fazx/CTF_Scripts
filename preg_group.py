#coding=utf-8
import requests
import re
import base64

url = 'http://120.24.86.145:8002/web6/'
s = requests.Session()
source = s.get(url)

header = source.headers['flag']
flag = base64.b64decode(header)
flag = flag.decode('utf-8')

p = re.match('(.*)(:)(.*)',flag)
payload = {'margin':base64.b64decode(p.group(3))}
r = s.post(url,data = payload)
print(r.text)