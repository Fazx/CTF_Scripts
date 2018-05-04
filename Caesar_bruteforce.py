message = 'roqtp697t95j3'

LETTERS = 'QWERTYUIOPASDFGHJKLZXCVBNM'
letters = 'qwertyuiopasdfghjklzxcvbnm'

for key in range(len(LETTERS)):
    tran = ''
    for i in message:
        if i in LETTERS:
            num = LETTERS.find(i)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            tran = tran + LETTERS[num]
        elif i in letters:
            num = letters.find(i)
            num = num - key
            if num < 0:
                num = num + len(letters)
            tran = tran + letters[num]
        else:
            tran = tran + i
    print('key = %s: %s' % (key, tran.lower()))
