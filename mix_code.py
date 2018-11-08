import binascii

text = 'd87 x65 x6c x63 o157 d109 o145 b100000 d116 b1101111 o40 x6b b1100101 b1101100 o141 d105 x62 d101 b1101001 d46 o40 d71 x69 d118 x65 x20 b1111001 o157 b1110101 d32 o141 d32 d102 o154 x61 x67 b100000 o141 d115 b100000 b1100001 d32 x67 o151 x66 d116 b101110 b100000 d32 d102 d108 d97 o147 d123 x31 b1100101 b110100 d98 d102 b111000 d49 b1100001 d54 b110011 x39 o64 o144 o145 d53 x61 b1100010 b1100011 o60 d48 o65 b1100001 x63 b110110 d101 o63 b111001 d97 d51 o70 d55 b1100010 d125 x20 b101110 x20 b1001000 d97 d118 o145 x20 d97 o40 d103 d111 d111 x64 d32 o164 b1101001 x6d o145 x7e'

solution = ''
text2 = text.split(' ')
for x in text2:
	print x
	if x[0] == 'b': #binary
		solution += chr(int(x[1:],2))
	elif x[0] == 'x': #hexadecimal
		solution += x[1:].decode("hex")
	elif x[0] == 'd': #decimal
		solution += chr(int(x[1:]))
	elif x[0] == 'o': #octal
		solution += chr(int(x[1:],8))

print solution