# -*- coding:utf-8 -*-
import sys
import os
import base64


def get_flag(flag_str):
flag_str.append(base64.b64encode(flag_str[0]))
flag_str.append(base64.b32encode(flag_str[0]))
flag_str.append(base64.b16encode(flag_str[0]))
flag_str.append(flag_str[0].encode('rot13'))
flag_str.append(flag_str[0].encode('hex'))
ascii_flag = ''
for i in flag_str[0]:
ascii_flag += str(ord(i))+','
ascii_flag2 = ''
for i in flag_str[0]:
ascii_flag2 += str(ord(i))+' '
flag_str.append(ascii_flag)
flag_str.append(ascii_flag2)
flag_str.append(bin(int(flag_str[0].encode('hex'),16))[2:])
flag_str.append('http://')
return flag_str

if __name__ == '__main__':
flag_str = get_flag([sys.argv[1]])
for i in flag_str:
os.system('strings %s | grep -i \'%s\'' % (sys.argv[2],i))