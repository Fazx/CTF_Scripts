import requests
import sys

host = sys.argv[1]
with open('dir.txt') as f:
    filenames = f.readlines()
for filename in filenames:
    try:
        r = requests.get(host+'/'+filename.strip())
    except:
        print 'error:'+filename
        continue
    if r.status_code != 404:
        print filename,
        print r.status_code
