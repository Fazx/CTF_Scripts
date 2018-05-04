import base64
while 1:
        filea = open(r'e:\base64.txt','r')
        lines = filea.readlines()
        writefile=open(r'e:\base64.txt','w')
        for i in lines:
                word = i.strip()
                b = base64.decodestring(word)
                print b
                writefile.write(b)
                writefile.write('\n')
        writefile.close()
        filea.close()