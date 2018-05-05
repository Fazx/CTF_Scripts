import binascii
real = 0xc4eb31fa
for y in range(100000, 999999):
    if real == (binascii.crc32(str(y)) & 0xffffffff):
        print(y)