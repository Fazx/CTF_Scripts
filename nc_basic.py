from pwn import *
host = '202.38.95.46'
port = '12009'
s = remote(host, port)
recv = s.recv()
print recv
while True:
    r = s.recv()
    print r
    recv = r.replace('exit()', 'None').replace(
        "__import__('os').system('find ~')", 'None').replace(
        "__import__('time').sleep(100)", 'None').replace(
        'print(\'\\x1b\\x5b\\x33\\x3b\\x4a\\x1b\\x5b\\x48\\x1b\\x5b\\x32\\x4a\')', 'None')
    print recv
    ans = str(eval(recv))
    print ans
    s.sendline(ans)