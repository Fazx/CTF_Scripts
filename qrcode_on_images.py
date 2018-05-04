#! /usr/bin/env python
from PIL import Image
import zbarlight

total_qr_code = 10 * 65
total_y = 10
total_x = 65

im = Image.open('qrcode.png')

for x in range(total_x):
    for y in range(total_y):

        nx = x * 33
        ny = y * 33

        nim = im.crop((nx, ny, nx + 33, ny + 33))

        qr_code = Image.new('RGB', (41, 41), (255, 255, 255))
        qr_code.paste(nim, (5, 5))

        codes = zbarlight.scan_codes('qrcode', qr_code)
        if codes != None:
            codes = codes[0]
            if "GCTF" in codes:
                print 'QR: %s' % codes