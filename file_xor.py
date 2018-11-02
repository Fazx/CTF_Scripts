def xor(str1, str2):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(str1,str2))


if __name__ == '__main__':

    for i in range(20):
        #png_1 = open(sys.argv[1], "rb").read(i)
        png_1 = open("xor.png", "rb").read(i)
        png_2 = open("flag.png", "rb").read(i)
        key = xor(png_1, png_2)

        print key