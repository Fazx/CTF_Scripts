# -*- coding: utf-8 -*-
import string
import hashlib
payloads = string.letters+string.digits
for a in payloads:
    for b in payloads:
        for c in payloads:
            s = "TASC"+a+"O3RJMV"+b+"WDJKX"+c+"ZM"
            tmp = hashlib.md5(s).hexdigest()
            if "e9032" in tmp:
                print s
                print tmp