import requests
import re

url = 'http://120.24.86.145:8002/qiumingshan/'
s = requests.Session()
source = s.get(url)
expression = re.search(r'(\d+[+\-*])+(\d+)',source.text).group()
result = eval(expression)
post = {'value':result}
r = s.post(url,data = post)
print(r.content)


# import requests,re
# s = requests.Session()

# url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
# html = s.get(url).content

# reg = r'([0-9].+)=<'
# pattern = re.compile(reg)
# match = re.findall(pattern,html)

# payload = {'v': eval(match[0])}
# print s.post(url, data=payload).content